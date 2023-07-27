import random
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"


def main():
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    # print(results.prettify)

    jobs = results.find_all("div", class_="card-content")

    while True:
        i = random.randint(0, len(jobs))
        title = jobs[i].find("h2", class_="title")
        company = jobs[i].find("h3", class_="company")
        location = jobs[i].find("p", class_="location")
        print(title.text, company.text, location.text)

        user_input = input("Do you want another job (y/n)?")
        if user_input != "y":
            break


if __name__ == "__main__":
    main()
