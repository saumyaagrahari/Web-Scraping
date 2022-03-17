from bs4 import BeautifulSoup
import json
import requests
from Task_13 import scrap_movie_details

def actor():
    with open("castmoviedata.json","r") as file:
        data = json.load(file)
        # print(data)
    movie_url_list = []
    for i in data:
        movie_url_list.append(i["movie_link"])
    list_1 = []
    for i in range(20):
        list_1.append(scrap_movie_details(movie_url_list[i]))
    find_dict = {}
    for i in list_1:
        for j in i["cast"]:
            if j not in find_dict:
                find_dict.update({j:[]})
    for i in find_dict:
        for j in list_1:
            if i in j["cast"]:
                for k in j["cast"]:
                    if i==k:
                        continue
                    find_dict[i].append(k)
                    break
    with open("AllActorData_14.json","w") as file:
        json.dump(find_dict,file,indent=4)
actor()