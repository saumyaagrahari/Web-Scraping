# import json
# # from Task_5 import data
# def movie_directors():
#     file_2 = open('Task_5.json','r')
#     read_file = json.load(file_2)
#     list_1 = []
#     for fle in read_file:
#         # print(fle['Original Language:'])
#         if fle ['Genre:'] not in list_1: 
#             list_1.append(fle['Genre:'])
#     dict_1 = {}
#     list_2 = []
#     for dic in list_1:
#         i = 0
#         count = 0
#         while i<len (read_file):
#             if dic == read_file[i]['Genre:']:
#                 count+=1
#             i+=1
#         dict_1.update({dic:count})
#     list_2.append(dict_1)
#     with open('Task_11.json','w') as file:
#         json.dump(list_2,file,indent=4)
#     # print(list_2)
# movie_directors()




from Task_5 import data
import json

def movie_gener():
    list_1 = []
    dict_1 = {}
    for i in data:
        gener = i["Genre:"].split(",")
        for i in gener:
            list_1.append(i)
            print(list_1)
        count = 0
        for j in list_1:
            count+=1
        dict_1.update({j:count})
    with open("task_11.json","w") as file:
        json.dump(dict_1,file,indent=4)
movie_gener()