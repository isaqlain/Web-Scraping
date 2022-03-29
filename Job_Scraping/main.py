from time import time
from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you are not familiar with ")
unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_text)
    soup = BeautifulSoup(html_text,'lxml')
    #print(soup.prettify())
    
    jobs = soup.findAll('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date = job.find('span',class_ = 'sim-posted').span.text
        #print(published_date)
        if 'few' in published_date:
                
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            #print(company_name 
            skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
            #print(skills)
            more_info = job.header.a['href']
            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Comapany Name: {company_name.strip()} \n")
                    f.write(f"Required Skills : {skills.strip()} \n")
                    f.write(f'More info : {more_info} \n')
            print(f'File saved: {index}')       
    
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} minutes ...')
        time.sleep(time_wait * 60)
