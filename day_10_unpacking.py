# unpacking the list and gets stored in variables

# a = b = c = 10  # multiple variable assignment

# print(a, b, c)


# # matching  by index values #unpacking tuples
# priya, bharath, swetha = ("butterscotch", "vanila", "blackcurent")
# print(priya)
# print(bharath)
# print(swetha)

# jeeva, priya, rathna = ["avan", "naan", "aval"]
# print(jeeva, priya, rathna)

# # or -- unpacking list

# people = ["avan", "naan", "aval"]
# jeeva, priya, rathna = people
# print(people)


# t1, t2, t3, _ = [2, 3, 45, 5]  # this works
# print(t1, t2, t3, _)
# print(t1, t2, t3)


# t1, t2, *t3 = [2, 3, 4, 5, 6, 7, 8]
# print(t1, t2, t3)


# t1, t2, *t3 = (2, 3, 4, 5, 6, 7, 8)       #tuple potalum t3 is  a list
# print(type(t3))
# print(t1, t2, t3)


# task1 for loop

# coord = [(5, 4), (1, 1), (6, 10), (9, 10)]
# cod = []
# for i in coord:
#     x, y = i
#     result = (x**2 + y**2) ** 0.5
#     cod.append(round(result, 1))
# print(cod)


# # task 2 for loop +unpacking

# coord = [(5, 4), (1, 1), (6, 10), (9, 10)]
# cod = []
# for i in coord:
#     x, y = i
#     result = (x**2 + y**2) ** 0.5
#     cod.append(result)
# print(cod)


# or

# unpack in for

# for x,y in coord:

# # task 3 unpacking + list comprehension
# cod = [round((x**2 + y**2) ** 0.5, 2) for x, y in coord]
# print(cod)

# t1, t2, *t3, t4 = (100, 200, 300, 400, 500, 600, 30)
# print(t1, t2, t4)

# marks1 = [70, 80, 60]
# # marks2 = [*marks1]   #to copy
# marks2 = [*marks1, 75, 68]  # to add values if wanted
# marks3 = [100, 60, *marks2]
# print(marks2)
# print(marks3)


# t1 = [80, 90]
# t2 = [50, 60]

# t3 = [*t1, *t2]   #merging multiple lists
# print(t3)


# unpack in dict
# copying dict to another and also we added values in it
movie = {"name": "john", "year": 2000}
movie2 = {**movie, "actor": "kean", "award": "arjuna", "year": 203}  # op : 203
movie3 = {"actor": "john", "year": 2014, **movie}  # op : 2000
print(movie2)
print(movie3)
