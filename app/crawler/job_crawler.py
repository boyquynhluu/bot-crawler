from app.crawler.browser import Browser


class JobCrawler:

    def __init__(self):
        self.browser = Browser()

    def crawl(self, url: str):

        try:
            self.browser.start()

            self.browser.open(url)

            print("Page title:", self.browser.page.title())
            print("URL: ", self.browser.page.url)

            # Get all text in the page
            text = self.browser.page.locator("body").inner_text()

            print("\n===== PAGE CONTENT =====")
            print(text[:5000])

            input("Press Enter Continues...")

        finally:
            self.browser.close()
