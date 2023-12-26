import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://realpython.github.io/fake-jobs/')
soup = BeautifulSoup(page.content, 'html.parser')

job_position = []
company_name = []
job_location = []

for item in soup.find_all("h2", attrs={'class ' : ' title is-5'}):
    job_position.append(item.text)

for item in soup.find_all("h3", attrs={'class  ':' subtitle is-6 company'}):
    company_name.append(item.text)

for item in soup.find_all("p", attrs={'class ':' location'}):
    job_location.append(item.text)


data = {"Job_position" : job_position,
        "Company_name": company_name,
        "Job_location": job_location
        }

data_table = pd.DataFrame(data)

data_table.to_excel("jobdata.xlsx")

      
      