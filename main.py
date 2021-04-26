import requests
from bs4 import BeautifulSoup as bs4

url = "https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3&page={page_num}"

num_of_pages = 500
for i in range(500):
    print(i)
    page_url = url.format(page_num=i)
    soup = bs4(requests.get(page_url).content, 'html.parser')
    packages = soup.find_all('a', class_="package-snippet")
    for package in packages:
        package_name = package.find('span', class_="package-snippet__name").text.strip()
        with open("python3_packages.txt", 'a+') as f:
            f.write(package_name+'\n')