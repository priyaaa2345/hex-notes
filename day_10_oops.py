# class Car:
#     def __init__(self, name, engine, wheels, doors):
#         self.name = name     # self-instance variable
#         self.engine = engine
#         self.wheels = wheels  #initializing instance variable
#         self.doors = doors

#     def horn(self):  # instance method
#         return f'{self.name} "says Vroom Vroom"'


# ferrari = Car("Ferrari", "V8", 4, 2)
# alto = Car("Alto", "v4", 4, 4)
# suzuki = Car("Suzuki", "v3", 4, 4)
# nano = Car("Nano", "v7", 4, 4)
# print(type(ferrari))  # class __main__.Car <class str
# print(ferrari.name, ferrari.wheels)
# print(alto.horn())


# TASK


# class Bank:
#     def __init__(self, acc_no, name, bal):
#         self.acc_no = acc_no
#         self.name = name
#         self.bal = bal


# Amisha = Bank(2342, "Amisha", 50000)
# Mathesh = Bank(5644, "Mathesh", 40000)
# Sai = Bank(3333, "Sai", 60000)

# print(Mathesh.bal)


# task2


# class Bank:
#     def __init__(self, acc_no, name, bal):
#         self.acc_no = acc_no
#         self.name = name
#         self.bal = bal

#     def display_balance(self):
#         return f"your balance is ₹{self.bal:,}"


# Amisha = Bank(2342, "Amisha", 50000)
# Mathesh = Bank(5644, "Mathesh", 40000)
# Sai = Bank(3333, "Sai", 60000)

# print(Amisha.display_balance())


# class Bank:
#     interest_rate = 0.02

#     def __init__(self, acc_no, name, bal):
#         self.acc_no = acc_no
#         self.name = name
#         self.bal = bal

#     def display_balance(self):
#         return f"your balance is ₹{self.bal}"

#     def withdraw(self, balance):
#         if self.bal > balance:
#             self.bal = self.bal - balance
#             return f"Succes!! {self.display_balance()}"

#     def deposit(self, ball):

#         self.bal = self.bal + ball
#         return f"Succes!!{self.display_balance()}"

#     def apply_interest(self):
#         self.bal = self.bal * Bank.interest_rate
#         return f"{self.display_balance()}"


# Amisha = Bank(2342, "Amisha", 50000)
# Mathesh = Bank(5644, "Mathesh", 40000)
# Sai = Bank(3333, "Sai", 60000)

# # print(Mathesh.withdraw(10000))  # taskk 3 # withdraww

# # print(Sai.deposit(15000))  # task 4 deposit

# print(Bank.interest_rate)

# print(Amisha.apply_interest())


# class Circle:
#     #use clss variable to update if it is common across all variables
#     pi = 3.14  # (class variable)  (common across all the instances)

#     def __init__(self, radius):
#         self.radius = radius

#     @staticmethod
#     def perimter(radius):  # static: no class,cant be accessed by self
#         return 2 * Circle.pi * radius

#     @classmethod  # common across all the instances
#     def from_diameter(cls, diameter):  # cls points to the class(CIRCLE)
#         radius = diameter / 2
#         return Circle(radius)

#     def calculate_area(self):
#         return Circle.pi * self.radius**2

#     # normal fn but inside the class


# print(Circle.perimter(2))

# # to access an instance method we need an instance(circle1)
# circle1 = Circle(4)
# print(circle1.calculate_area())

# # class method to construct the obj
# circle_from_dia = Circle.from_diameter(10)
# print(circle_from_dia.calculate_area())


# task total num of bank_acc


# class Bank:
#     interest_rate = 0.02
#     no_of_accounts = 0

#     def __init__(self, acc_no, name, bal):
#         self.acc_no = acc_no
#         self.name = name
#         self.bal = bal
#         Bank.no_of_accounts += 1


# #instance methods
#     def display_balance(self):
#         return f"your balance is ₹{self.bal}"

#     def withdraw(self, balance):
#         if self.bal > balance:
#             self.bal = self.bal - balance
#             return f"Succes!! {self.display_balance()}"

#     def deposit(self, ball):

#         self.bal = self.bal + ball
#         return f"Succes!!{self.display_balance()}"

#     def apply_interest(self):
#         self.bal = self.bal * Bank.interest_rate
#         return f"{self.display_balance()}"

#     @staticmethod  #its in static bcos it is related to bank clas
#     def get_total_no_accounts():
#         return f"In total we have {Bank.no_of_accounts}"

#     # just displays the value...no modiication so static

#     # upd ints rate should be modified..so class methhod
#     @classmethod
#     def update_interest_rate(cls, new_rate):
#         cls.interest_rate = new_rate


# Amisha = Bank(2342, "Amisha", 50000)
# Mathesh = Bank(5644, "Mathesh", 40000)
# Sai = Bank(3333, "Sai", 60000)


# print(Bank.no_of_accounts)
# Bank.update_interest_rate(0.10)

# print(Amisha.apply_interest())
# print(Amisha.display_balance())
