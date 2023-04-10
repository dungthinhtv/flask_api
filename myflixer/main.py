from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

# website = "https://phimmoi9.net/z.php?BL=2&QG=&TL=&NC=&trang="
website = "https://myflixer.to/movie?page="
path = "../chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

names = []
links = []
years = []
bgrs = []
ids=[]


for i in range(1,4):
    
    print(i)
    
    driver.get(website + str(i))

    containers = driver.find_elements(by="xpath",value='//div[@class="flw-item"]')


    for container in containers:
        name = container.find_element(by="xpath",value='./div/h2/a').text
        year = container.find_element(by="xpath",value='./div/div/span[@class="fdi-item"]').text
        bgr =  container.find_element(by="xpath",value='./div/img').get_attribute("src")
        link = container.find_element(by="xpath",value='./div/a').get_attribute("href")
        idmf = link[-(len(link)-link.rfind('-')-1):]
        
        names.append(name)
        links.append(link)
        years.append(year)
        bgrs.append(bgr)
        ids.append(idmf)
        
# Exporting data to a CSV file
my_dict = {'name': names,'year': years,'link': links,'bgr': bgrs,'id': ids}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('myflixer_movie.csv')

driver.quit()
