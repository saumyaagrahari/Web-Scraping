import requests
from bs4 import BeautifulSoup
# import json
# print("saumy@bhey")
#        giving movie rank


url = ("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
# print(url)
page = requests.get(url)
# print(page)
# print(page.text)
soup = BeautifulSoup(page.text, 'html.parser')

movie = []
movie_no = []
movie_name = []
year_of_realease = []
movie_rating = []
movie_urls = []
name, rating, link, position = "", "", "", ""


def scrap_top_list():
    global movie_no, movie_name, year_of_realease, movie_rating, movie_urls, name, rating, link, position

    tbody = soup.find('table', class_="table")
    trs = tbody.find_all('tr')
    for tr in trs:
        try:
          
            position = tr.find('td', class_="bold").get_text().strip()
            movie_no.append(position)
            
            name = tr.find('a', class_="unstyled articleLink").get_text().strip()
            movie_name.append(name)
            
            rating = tr.find('span', class_="tMeterScore").get_text().strip()
            movie_rating.append(rating)
            
            link = tr.find('a').get("href")
            movie_link = 'https://www.rottentomatoes.com' + link
            movie_urls.append(movie_link)
            
        except AttributeError:
            print()
    print(movie_no)
    print(movie_name)
    print(movie_rating)
    print(movie_urls)
    # return movie_rank

#     with open("top_movie.json","w")as file:
#         json.dump(movie,file,indent=4)
#     return movie
# data=movie()
	

scrap_top_list()




