import requests
from bs4 import BeautifulSoup
url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=nigeria'
page=requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

jobs_elem=results.find_all('section',  class_='card-content')

title_list = []
list_dict={
    'titles': 0
    
}
for jobs in jobs_elem:
    title=jobs.find('h2', class_='title')
    company=jobs.find('div', class_='company')
    location=jobs.find('div', class_='location')
    
    if None in (title,company,location):
        continue
    
    title_list.append(title.text)
    list_dict.update(titles= title.text)

print(list_dict)

'''
title_list_stripped=[]
for i in title_list:
    title_list_stripped.append(i.rstrip())
    print(title_list_stripped)
    '''
    

