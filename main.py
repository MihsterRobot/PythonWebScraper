import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)  # Issue HTTP GET request to retrieve HTML data
print(page.text)  # Print HTML data as text

# Using .content instead of .text avoids issues with character encoding
# .content holds raw bytes, which can be decoded better than text representation
# html.parser ensures the appropriate parser is used for HTML content
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")  # Find specific HTML element by ID

# .prettify() formats the parse tree such that each tag is on its own separate line with indentation
print(results.prettify())

# find_all() returns an iterable containing all HTML for all job listings displayed on the page
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    print(job_element.prettify(), end="\n"*2)

print()
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip(), "\n")

# Finds all <h2> elements where contained string matches "Python" exactly
python_jobs = results.find_all("h2", string="Python")

# Prints empty list because exact string "Python" doesn't exist in job listings
print(python_jobs)
