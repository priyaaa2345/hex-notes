# def add(a, b):  # fn declaration / defn
#     return a + b  # fn body

# a,b paramaters 4,6 arguments
# print("the sum is :", add(4, 6))  # fn call


# def driving(name, age, car="Dezire"):  # default value i none is given
#     if age >= 18:
#         return f"{name} eligible for driving. tested with {car}"
#     else:
#         return "try again after u reach 5 feet"


# print(driving("priya", 20, "toyota"))
# print(driving('rathna',18))
# print(driving("bharath", car="honda", age=20))  #kw arguments shld be at last


# ex
library_list = [
    {
        "title": "Python Programming",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True,
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "year": 2020,
        "available": True,
    },
    {
        "title": "Learning Python I",
        "author": "Mark Lutz",
        "year": 2013,
        "available": False,
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "year": 2015,
        "available": True,
    },
    {
        "title": "Adavance Python",
        "author": "Mark Lutz",
        "year": 2015,
        "available": False,
    },
]
book = {"title": "Fluent Python II", "author": "Alex", "year": 2016, "available": True}


# task1  Add Book Function:
# Write a function add_book(library, new_book)


# def add_book(library, new_book):
#     library.append(new_book)


# add_book(library_list, book)
# print(library_list)


# # task 2 search book by author name
# def search_by_author(library, author_name):
#     for book in library:
#         if book["author"] == author_name:
#             print(book)


# print(search_by_author(library_list, "Mark Lutz"))

# task 3 checkout fn
# Write a function check_out_book(library, title) that
# marks a book as not available ,if it exists
# and is available in the library.


# def check_out_book(library, titles):
#     for i in library:
#         if i.get("title") == titles:
#             if i.get("available"):
#                 i["available"] = False
#                 return f" {titles} is  availabe"
#         elif i.get("title") == titles:
#             if i.get("available") == False:
#                 return f" {titles} is  unavailabe"

#         else:
#             return f"sry {titles} doesnt exist"


# print(check_out_book(library_list, "Python Programming"))


# import
from pprint import pprint

# inbuilt fns ( sum max min len round)


# task
movies = [
    {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
    {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
]


# # avg rating
# def get_movie_rating(movies):
#     for i in movies:
#         i["avg_rating"] = sum(i["ratings"]) / len(i["ratings"])
#     return movies


# pprint(get_movie_rating(movies))

# break into 2 fns


# def avgg(movies):
#     for i in movies:
#         return sum(i["ratings"]) / len(i["ratings"])


# def get_movie_rating(movies):
#     for i in movies:
#         i["avg_rating"] = avgg(movies)
#     return movies


# pprint(get_movie_rating(movies))


# print(max(2, 4, 5, 6, 7, 8, 83, 33))

# without using max

# def own_max(*maxx):      #arbitrary num of possitional arguuments
#     max = maxx[0]
#     for num in maxx:  #datatype of max is tuple
#         if num > max:
#             max = num
#     return max


# print(own_max(5, 6, 7, 8))
# print(own_max(5, 6, 7, 8, 99, 76))


# def party(**people):  # arbitrary num of keyword arguemnts
#     print(people.values())
#     print(", ".join(people.values()))


# party(p1="abi", p2="choc", p3="lava")
