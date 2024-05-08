# while and for

# count=1
# while count < 5:
#     print(count)
#     count = count + 1

# n = int(input("enter the stars"))
# i = 1
# while i <= n:
#     print("✨" * i)
#     i += 1


# num = int(input("enter the num"))         # reverse order using for
# for count in range(num):
#     print("✨" * num)
#     num = num - 1


n = int(input("enter"))
for i in range(1, n + 1):
    print("✨" * i)


# play = [10, 20, 30]
# for i in range(len(play)):
#     play[i] *= 2
# print(play)


# play = [10, 20, 30]
# emp = []
# for i in range(len(play)):
#     emp.append(play[i] * 2)

# print(play)
# print(emp)

# player_stats = [10, 20, 30]
# power = [
#     stat * 2 for stat in player_stats
# ]  # i wan to double the stats for each stats in player stats
# print(power)
# print(player_stats)


# # # ex 4.1 for loop
# avengers = ["thor", "spider", "iron"]
# result = []
# for i in avengers:
#     result.append(len(i))
# # print(result)

# # ex 4.2
# list comprehension


# result = [(len(i)) for i in avengers]
# print(result)


# example
# large_count = []
# letters_count = [4, 8, 11, 15, 10, 4]
# # for i in letters_count:
# #     if i > 10:
# #         large_count.append(i)
# # print(large_count)

# large_count = [i for i in letters_count if i > 10]
# print(large_count)


# avengers = ["hulk", "Iron man", "black widow", "captain america", "spider man", "thor"]
# aven = []
# for i in avengers:
#     if len(i) > 10:
#         aven.append(i)
# print(aven)


# aven = [i.upper() for i in avengers if len(i) > 10]
# print(aven)
