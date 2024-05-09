# def to_upper_case(text):
#     return text.upper() + " 😒"


# def main():
#     print(__name__)
#     print(to_upper_case("priya"))


# if __name__ == " __main__":
# main()

from datetime import datetime

# print(datetime.now().weekday())
# print(datetime.now())


# calculate age
# #my code
# def Calculate_age(year):
#     try:
#         if 2024 > year:
#             age = 2024 - year
#             return age
#         else:
#             print("birth year cant be greater than 2024")
#     except ValueError as e:
#         print("year should be int", e)


# year = int(input("enter your year of birth"))
# age = Calculate_age(year)
# # print(f"your age is {age}")


def calculate_age():
    try:
        current = datetime.now().year
        birth = int(input("enter your year"))
        if birth > current:
            print(f"are u from future")
        elif birth <= 0:
            print("no negative values are accepted")
        else:
            age = current - birth
            print(f"your age is {age}")

    except ValueError as err:
        print("invalid number", err)
    except Exception as err:
        print("this catches all !", err)
    finally:
        print("operation successful")


calculate_age()
