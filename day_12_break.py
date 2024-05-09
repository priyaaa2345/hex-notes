# def skip_even():
#     for num in range(1, 11):
#         if num % 2 == 0:
#             break #check with continue too
#         print(num)
#     print("execution continues")


# skip_even()


# def print_nums():
#     for num in range(1, 10):
#         if num == 5:
#             continue  # skips 5thh iteration so theres no 5 in op
#         print(num)
#     print("exeution continues")


# print_nums()


# task 1
# find the first negative value

# #with break
# def first_negative(values):
#     for i in values:
#         if i < 0:
#             print(i)
#             break


# # with continue
# def first_negative(values):
#     for i in values:
#         if i > 0:
#             continue
#         return i


# print(first_negative([3, 5, 7, -1, 9, -3]))


# # task2
# def process_until_duplicate(values):
#     store = set()
#     for i in values:
#         if i in store:
#             print("duplicate found,processing stopped ")
#             break
#         store.add(i)
#         print(f"processed {i}")


# if __name__ == "__main__":

#     process_until_duplicate(["apple", "banana", "carrot", "apple", "date", "banana"])


# task 3
def censorship_bot(messages, banned_words):
    for i in messages:
        if banned_words in messages:
            continue
        else:
            return f"Approved message! {i}"


messages = [
    "Hello everyone!",
    "This is a bad word example!",
    "Let's keep our chat clean!",
    "Oops another bad content!",
    "Have a nice day!",
]

banned_words = ["bad", "oops"]

censorship_bot(messages, banned_words)


# Expected output
# Approved message: Hello everyone!
# Approved message: Let's keep our chat clean!
# Approved message: Have a nice day!
