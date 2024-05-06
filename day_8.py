print("hello, world")
# declare and assign
# ctrl+/

# name = "priya"
# print(name)
# print(type(name))
# # to find data type
# age=20
# print(type(age))

# concat
# print('priya '+'dharshini')
# name=input("enter your name?" )

# fah =input("enter fahrenheit" )
# print(type(fah))
# cel = (float(fah)-32) * 5/9
# print(cel,type(cel))
# print("equivalent of " +fah + "°F " + "is " + str(cel) + "cel ")
# print(f"the equivalent of {fah}°F is {cel}°C")

# agee=input("enter your age")
# print(f"hello, {name}! You are {agee} years old")

# # task 2
# year= int(input("enter your year of birth"))
# age =  2023 - year
# print(f'your age is {age}')
# we can use expr in f string too
# print(f'age is {2024 - int(year)}')

# # task 3
# rad=input("enter the radius")
# area=3.14*float(rad)**2
# print(f'the area of circle with radius {rad} is {area}')

# task 4 build a loader
# input 70
# op 7 equal too

# get = int(input("enter the load"))
# m = get/10

# print('=' * m)
n=int(input("enter the loader number"))
load = n // 10
loader = "{" + "=" * load +  " " * (10 - load) + "}" 
print(loader)