import requests


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)  # Issue HTTP GET request to retrieve HTML data
print(page.text)
