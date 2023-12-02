import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from datetime import date

load_dotenv()
YEAR = 2023
DAY = " "
while not (DAY == "" or DAY.isnumeric()):
    DAY = input("Select Date Puzzle or Current Date (PRESS ENTER): ").strip()
if DAY == "":
    CURRENT_DATE = date.today().day
else:
    CURRENT_DATE = DAY

AOC_COOKIE = os.environ["AOC_SESSION"]
BASE_URL = f"https://adventofcode.com/{YEAR}/day/"


# GET QUESTION
page = requests.get(
    f"{BASE_URL}{CURRENT_DATE}",
    cookies={"session": AOC_COOKIE},
)
soup = BeautifulSoup(page.content, "html.parser")

articles = soup.find_all("article")
code = soup.find_all("pre")

for i in range(len(list(articles))):
    partNum = i + 1
    with open(f"./Day {CURRENT_DATE}/question_part{partNum}.md", "w") as f:
        source = md(
            f'<a href="{BASE_URL}{CURRENT_DATE}" target="_blank">{BASE_URL}{CURRENT_DATE}</a>'
        )
        f.write(f"Source: {source}")
        f.write(md(articles[i].prettify()))
        f.close()
    with open(f"./Day {CURRENT_DATE}/example{partNum}.txt", "w") as f:
        f.write(code[i].text.strip())

# GET INPUT
page = requests.get(
    f"{BASE_URL}{CURRENT_DATE}/input",
    cookies={"session": AOC_COOKIE},
)

with open(f"./Day {CURRENT_DATE}/input.txt", "w") as f:
    f.write(page.text)
    f.close()


print("DONE")
