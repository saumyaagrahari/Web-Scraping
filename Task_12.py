from bs4 import BeautifulSoup
import json 
import requests

def movie_cast(movie_url):
    cast_list = []
    data = requests.get(movie_url)
    soup = BeautifulSoup(data.text,'html.parser')
    main = soup.find_all('div',class_='panel-body content_body')
    section = main[1].find('div',class_='castSection')
    all = section.find_all('div',class_='cast-item')
    for i in all:
        cast_list.append(i.find('span')['title'])
    with open('castData_12.json','w') as file:
        json.dump(cast_list,file,indent=4)
    return cast_list
data = movie_cast("https://www.rottentomatoes.com/m/black_panther_2018")