from bs4 import BeautifulSoup
import requests
import json

# from Task_1 import adventure

def details_movie(movie_url):
    movie_details = []
    movie_dic = {}
    page = requests.get(movie_url)
    # print(page)
    soup = BeautifulSoup(page.text,'html.parser')
    # print(soup)
    movie_dic['name'] = 'BlackPanther'
    movie_bio = soup.find('div',class_='movie_synopsis clamp clamp-6 js-clamp').get_text().split()
    # print(movie_bio)
    movie_dic ['Bio'] = (movie_bio)
    # print(movie_bio)
    title = soup.find_all('div',class_='meta-label subtle')
    # print(title)
    value = soup.find_all('div',class_='meta-value')
    # print(value)
   
    
    for i in range(len(title)):
        movie_dic[str(title[i].get_text().strip())[:-1]] = value[i].get_text().replace(" ","").strip().replace("\n","")
    movie_details.append(movie_dic)

    with open('Task_4.json','w') as file:
        json.dump(movie_details,file,indent=4)

details_movie("https://www.rottentomatoes.com/m/black_panther_2018")

