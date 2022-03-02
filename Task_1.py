from bs4 import BeautifulSoup
import requests
import json

def adventure_movie():
    adventure_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    adventure_api=requests.get(adventure_url)
    htmlcontent=adventure_api.content
    # print(htmlcontent)
    soup=BeautifulSoup(htmlcontent,"html.parser")
    table_tag=soup.find("table",class_="table")
    tr=table_tag.find_all("tr")
    top_movie=[]
    serial_no=1
    for i in tr:
        movie_rank=i.find_all("td",class_="bold")
        for j in movie_rank:
            rank=j.get_text()
        movie_rating=i.find_all("span",class_="tMeterScore")
        for rate in movie_rating:
            rating=rate.get_text().strip()
        movie_name=i.find_all("a",class_="unstyled articleLink")
        for name in movie_name:
            title=name.get_text().strip()
            list=title.split()
            year=list[-1][1:5]
            year1=int(year)
            name_lenght=len(list)-1
            name=""
            for l in range(name_lenght):
                name+=""
                name+=list[l]
            movie_name=name
        movie_reviews=i.find_all("td",class_="right hidden-xs")
        for rev in movie_reviews:
            reviews=rev.get_text()
        url=i.find_all("a",class_="unstyled articleLink")
        for i in url:
            link=i["href"]
            movie_link="https://www.rottentomatoes.com"+link
            # print(movie_link)
            details={"movie_rank":"","movie_rating":"","movie_name":"","movie_reviews":"","movie URL":"","year":""}
            details["movie_rank"]=rank
            details["movie_rating"]=rating
            details["movie_name"]=movie_name
            details["movie_reviews"]=reviews
            details["movie URL"]=movie_link
            details["year"]=year1
            top_movie.append(details.copy())
            # print(top_movie)

  
    with open('top_movie_1.json','w') as file:
        json.dump(top_movie,file,indent=4)
        return top_movie
adventure=adventure_movie() 
	












# # import json
# # from bs4 import BeautifulSoup
# # import requests

# # url = ("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
# # # print(url)
# # page = requests.get(url)

# # soup = BeautifulSoup(page.text,'html.parser')

# # def scrap_top_list():
# #       maindiv = soup.find('div',class_= 'lister')
# #       tbody = maindiv.find('tbody',class_='lister-list')
# #       trs = tbody.find_all('tr')
# #       movie_rank = []
# #       movie_name = []
# #       year_of_realease = []
# #       movie_ratings = []
# #       movie_urls = []
# #       for tr in trs:
# #         position = tr.find('td',class_='titleColumn').get_text().strip()
# #         rank = ''
# #         for i in position:
# #           if '.' not in i:
# #             rank+=i
# #           else:
# #             break
# #       movie_rank.append(rank)  
# #       title = tr.find('td',class_='titleColumn').a.get_text()
# #       movie_name.append(title)

# #       year = tr.find('td',class_='titleColumn').span.get_text()
# #       year_of_realease.append(year)

# #       imdb_rating = tr.find('td',class_='ratingColumn imdbRating').strong.get_text()
# #       movie_ratings.append(imdb_rating)

# #       link = tr.find('td',class_='titleColumn').a['href']
# #       movie_link = 'https://www.imbd.com'+link
# #       movie_urls.append(movie_link)

# #       Top_Movies = []
# #       details = {'position':'','name':'','year':'','rating':'','url':''}
# #       for i in range(0,len(movie_rank)):
# #         details['position'] = int(movie_rank[i])
# #         details['name'] = str(movie_name)
# #         year_of_realease[i] = year_of_realease[i][1:5]
# #         details['year'] = int(year_of_realease[i])
# #         details['rating'] = float(movie_ratings[i])
# #         details['url'] = movie_urls[i]
# #         Top_Movies.append(details)
# #         details = {'position':'','name':'','year':'','rating':'','url':''}
# #         return (Top_Movies)
# # print(scrap_top_list())



# # with open("movie_data_.json","w")as file_s:
# #   json.dump(Top_Movies,file_s,indent=7)
# #   return (Top_Movies)
# # print(scrap_top_list)




	