from turtle import title
import requests
from bs4  import BeautifulSoup
url = 'https://codewithharry.com'
r = requests.get(url)
html_content = r.content
print(html_content)

# soup = BeautifulSoup(html_content,'html.parser')
# print(soup)
# print(soup.prettify)

# title = soup.title
# print(title)
# print(type(title))
# print(type(title.string))

# # print(type(soup))     #Beautifulsoup
# # print(type(title))   #tag
# # print(type(title.string))    #NavigableString

# paras = soup.find_all('p')
# print(paras)

# # get the first element in the html page 
# print(soup.find('p'))

# # get the class of httml page
# print(soup.find('p')['class'])

# # find all the element with class lead
# print(soup.find_all('p',class_='lead'))

# # get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

# # get all the anchors tags for the page
# anchors = soup.find_all('a')
# print(anchors)

# # get all the links on the page
# all_link = set()
# for link in anchors:
#     if (link.get('href')!='#'):
#         link = ('https://codewithharry.com'+link.get('href'))
#         all_link.add(link)
#         # print(link.Text)


# import json,requests
# data = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
# text_file = data.text
# # print()
# with open("Movie_data.json","w") as Movie:      
#   json.dump(text_file, Movie, indent=4)         
# # print(data.text)
# movie_list = open("Movie_data.json","r").read()
# movie_data_list = json.loads(movie_list)
# Movie_file = open("Movie_data.json","r").read()  # open and read file
# data = json.loads(Movie_file) 
# print(data.text)


# import requests
# from bs4 import BeautifulSoup

# url = ("https://www.imdb.com/india/top-rated-indian-movies/")

# def main():
#     response = requests.get(url)
#     html = response.text
#     soup = BeautifulSoup(html,'html.parser')
#     movietage = soup.select('td.titleColumn')
#     movie_tag = movietage[0]
#     moviesplit = movie_tag.text.split()
#     print(moviesplit)

