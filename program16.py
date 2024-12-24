import requests
from bs4 import BeautifulSoup
URL="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
page=requests.get(URL)
print(page.text)
soup=BeautifulSoup(page.text,'html.parser')
results=soup.find(id="ResultsContainer")
job_element=results.find_all("div",class_="card-content")
for job_element in job_element:
    title_element=job_element.find("h2",class_="title")
    company_element=job_element.find("h3",class_="company")
    location_element=job_element.find("p",class_="location")
    print(title_element.textstrip())
    print(company_element.textstrip())
    print(location_element.textstrip())
    print()