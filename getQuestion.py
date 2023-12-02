import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from datetime import date

load_dotenv()

DAY = " "
while not (DAY == "" or DAY.isnumeric()):
    DAY = input("Select Date Puzzle or Current Date (PRESS ENTER): ").strip()
if DAY == "":
    CURRENT_DATE = date.today().day
else:
    CURRENT_DATE = DAY

AOC_COOKIE = os.environ["AOC_SESSION"]
BASE_URL = "https://adventofcode.com/2023/day/"


# GET QUESTION
page = requests.get(
    f"https://adventofcode.com/2023/day/{CURRENT_DATE}",
    cookies={"session": AOC_COOKIE},
)
soup = BeautifulSoup(page.content, "html.parser")

with open(f"./Day {CURRENT_DATE}/question.md", "w") as f:
    source = md(
        f'<a href="https://adventofcode.com/2023/day/{CURRENT_DATE}" target="_blank">https://adventofcode.com/2023/day/{CURRENT_DATE}</a>'
    )
    f.write(f"Source: {source}")
    f.write(md(soup.find("article").prettify()))
    f.close()

# GET INPUT
page = requests.get(
    f"https://adventofcode.com/2023/day/{CURRENT_DATE}/input",
    cookies={"session": AOC_COOKIE},
)

with open(f"./Day {CURRENT_DATE}/input.txt", "w") as f:
    f.write(page.text)
    f.close()


print("DONE")
