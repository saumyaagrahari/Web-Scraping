from bs4 import BeautifulSoup
import requests
import json
from Task_1 import adventure

i = 0
while i<=10:
    url = adventure[i]['movie URL']
    movie_details = []
    def details_movie (link):
        movie_id = ' '
        for id in link[33:]:
            if '/' not in id:
                movie_id+=id
            else:
                break
        file_name = movie_id + '.json'
        dic = {}
        link_1 = requests.get(link)
        # print(link_1)
        soup = BeautifulSoup(link_1.text,'html.parser')
        # print(soup)
        dic ['name'] = soup.find('h1').text
        movie_bio = soup.find('div',class_='movie_synopsis clamp clamp-6 js-clamp').get_text().strip()
        # print(movie_bio)
        dic ['Bio'] = movie_bio
        title = soup.find_all('div',class_='meta-label subtle')
        # print(title)
        value = soup.find_all('div',class_='meta-value')
        for i in range (len(title)):
            dic[str(title[i].get_text().strip())[:-1]] = value[i].get_text().replace(' ','').strip().replace('\n',' ')
        movie_details.append(dic)

        with open(file_name,'w') as file:
            json.dump(movie_details,file,indent=4)
    details_movie(url)
    i+=1




