from bs4 import BeautifulSoup
from app.models.job import Job


def parse_jobs(html: str) -> list[Job]:

    soup = BeautifulSoup(html, "html.parser")

    job_links = soup.select(
        'a.text-it-black.text-hover-red[href*="/it-jobs/"]'
    )

    jobs = []

    for link in job_links:
        card = link.find_parent("div", class_="job-card")  # ancestor Job Card

        if not card:
            continue

        # Title
        title = link.get_text(strip=True)
        # URL
        url = link.get("href")

        # Company
        company = card.select_one(
            'a.text-rich-grey[href*="/companies/"]'
        ).get_text(strip=True)

        # Salary
        salary_element = card.select_one(
            "div.salary.text-success-color"
        )
        salary = (
            salary_element.get_text(" ", strip=True)
            if salary_element
            else None
        )

        # Location
        location_element = card.select_one(
            "div.text-rich-grey.text-truncate"
        )
        location = (
            location_element.get_text(strip=True)
            if location_element
            else None
        )

        # Experience
        experience_element = link.select_one(".experience")
        experience = (
            experience_element.get_text(strip=True)
            if experience_element
            else None
        )

        jobs.append(
            Job(
                title=title,
                company=company,
                salary=salary,
                location=location,
                experience=experience,
                source="ITviec",
                status="New",
                url=url,
            )
        )

    return jobs
