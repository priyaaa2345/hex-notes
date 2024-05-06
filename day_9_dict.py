# person = {"name": "kim taehyung", "age": 25, "nation": "Korea", "aim": "singer"}

# print(person["name"])
# (person["age"]) += 1  # updating
# print(person["age"])


# print(person.keys())  # gets only the key
# print(person.values())  # gets only values


# books = [  # datatype: list in dict
#     {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
#     {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
#     {"title": "Sapiens", "rating": 4.9, "genre": "History"},
#     {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
#     {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
# ]


# # rating>4.7
# result = []
# for i in books:
#     if i["rating"] >= 4.7:
#         result.append(i["title"])
# print(result)

# # or

# result = [i["title"] for i in books if i["rating"] >= 4.7]
# print(result)


# ## SETS

# tech = {"smart", "phone", "tab", "lap"}
# empty_sets = set()
# empt_dict = {}
# print(type(empty_sets))
# print(type(tech))

# tech.add('charger')
# tech.add("smart")    #it wont add ome more time.
# print(tech)

# colors = ["red", "blue", "red", "green", "pink", "blue"]
# color = set()
# for i in colors:
#     color.add(i)
# print(color)
