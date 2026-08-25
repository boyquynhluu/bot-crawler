from bs4 import BeautifulSoup
import requests

url = "https://itviec.com/it-jobs/java"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/151.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

job_links = soup.select(
    'a.text-it-black.text-hover-red[href*="/it-jobs/"]'
)

print("Found jobs:", len(job_links))

first_job = job_links[0]

element = first_job

with open("job.txt", "w", encoding="UTF-8") as f:
    for i in range(8):
        element = element.parent

        f.write(f"\n===== LEVEL {i + 1} =====\n")
        f.write(f"TAG: {element.name}\n")
        f.write(f"CLASS: {element.get('class')}\n")
        f.write(f"TEXT: {element.get_text(' | ', strip=True)[:1000]}\n")

    print("Total Jobs: 8")
