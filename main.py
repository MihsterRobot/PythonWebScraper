import requests


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)  # Return HTML data from URL
print(page.text)
