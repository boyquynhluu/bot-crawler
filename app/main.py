from app.crawler.browser import Browser
from app.services.excel_service import write_jobs_to_excel
from app.parser.job_parser import parse_jobs
from app.auth.login import Login


url = "https://itviec.com/it-jobs/java"


def main():

    browser = Browser()

    try:
        browser.start()

        # Login
        Login(browser)

        browser.open(
            url
        )

        # Parse job from web to Object
        jobs = parse_jobs(browser.page.content())

        # Write job to excel
        write_jobs_to_excel(jobs)

        input("Press Enter to close...")

    finally:
        browser.close()


if __name__ == "__main__":
    main()
