# from pprint import pprint
from Task_1 import adventure_movie
from Task_2 import top_movie
import json

dec_arg = top_movie(adventure_movie())


def group_by_decade(movies):
    moviedec = {}
    decade_year = []                   #[2010, 1950, 1920, 2020, 1930, 1970, 2000, 1940, 1960, 1980, 1990]
    for index in movies:
        Mod = index % 10    # mod = 3
        decade = index - Mod  # decade 1970
        if decade not in decade_year:
            decade_year.append(decade)   # it is creating list of decates
    decade_year.sort()
    for decade in decade_year:
        moviedec[decade] = []
    
    for moviedec_key in moviedec:
        dec10 = moviedec_key + 9    # dec10 = 1959
        for values in movies:
            if values >= moviedec_key and values <= dec10:   # 2018 >= 2010      2018 <= 2019
                moviedec[moviedec_key].append(movies[values])

    with open('top_movie_3.json', 'w') as file:
        json.dump(moviedec, file, indent=4)
    return moviedec

group_by_decade(dec_arg)














# from pprint import pprint
# from Task_1 import adventure_movie
# from Task_2 import top_movie
# import json

# dec_arg = adventure_movie()
# dec = top_movie(dec_arg)

# def group_by_decade(movies):
#     moviedec = {}
#     list1 = []
#     for index in movies: 
#         # print("index",index)
#         Mod = index % 10    # mod = 3
#         # print(Mod)
#         decade = index - Mod  # decade 1970
#         if decade not in list1:
#             list1.append(decade)   # it is creating list of decates
#             # print(list1)
#         list1.sort()
#         for i in list1:
#             moviedec[i] = []
#         for i in moviedec:
#             dec10 = i + 9    # dec10 = 1959
#             for x in movies:
#                 if x <= dec10 and x >= i:   # dec10 = e.g 1959 or i = e.g 1950
#                     for v in moviedec[i].append(v):
#                         print(v)
#             with open('top_movie_3.json','w') as file:
#                 json.dump(moviedec,file,indent=4)
#             return moviedec
#                                         # pprint(moviedec)
# group_by_decade(dec_arg)






