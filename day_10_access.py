# INHERITANCE


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "sound sound"


# class Dog(Animal):
#     def __init__(self, name, speed):
#         super().__init__(name)  # called our base class constructor
#         self.speed = speed

#     def run(self):
#         return "wags tail"

#     def speak(self):  # polymorphism(changes form) : method overriding
#         return "woof woof"  # here the return statmetns changes as per use

#     def speed_bonus(self):
#         return f"{self.name} Running at {self.speed * 2}km/hr"


# toby = Animal("toby")  # toby cant use run bcos its the parent class
# print(toby.speak())

# max = Dog("maxy", 20)
# print(max.name)
# print(max.run())
# print(
#     max.speak()
# )  # but max can use run bcos its the base clas and it can inherit the paernt one
# print(max.speed)
# print(max.speed_bonus())


# taska


# class Bank:
#     _interest_rate = 0.02

#     def __init__(self, acc_no, name, bal):
#         self.acc_no = acc_no
#         self.name = name
#         self._bal = bal

#     def display_balance(self):
#         return f"your balance is ₹{self._bal}"

#     def withdraw(self, balance):
#         if self._bal > balance:
#             self._bal = self._bal - balance
#             return f"Succes!! {self.display_balance()} after withdrawal"

#     def deposit(self, ball):

#         self._bal = self._bal + ball
#         return f"Succes!!{self.display_balance()} after deposit"

#     def apply_interest(self):
#         accumulated_interest = self._bal * self._interest_rate
#         self._bal += accumulated_interest
#         return f"Interest received. {accumulated_interest}"

#     @staticmethod  # dont use: its in static bcos it is related to bank clas
#     def get_total_no_accounts():
#         return f"In total we have {Bank.no_of_accounts}"

#     # just displays the value...no modiication so static

#     # upd ints rate should be modified..so class methhod
#     @classmethod
#     def update_interest_rate(cls, new_rate):
#         cls.interest_rate = new_rate


# # Amisha = Bank(2342, "Amisha", 50000)
# # Mathesh = Bank(5644, "Mathesh", 40000)
# # Sai = Bank(3333, "Sai", 60000)


# # # task
# # class SavingsAccount(Bank):
# #     _interest_rate = 0.05


# # sabesh = SavingsAccount(131, "Sabesh", 80000)
# # priya = Bank(133, "Priya", 20000)

# # print(sabesh.apply_interest())
# # print(sabesh.display_balance())

# # task 6 transaction fee 10rs


# class CurrentAccount(Bank):
#     per_transaction = 10

#     def withdraw(self, balance):
#         total_amount = balance + CurrentAccount.per_transaction
#         return super().withdraw(total_amount)


# tanishq = CurrentAccount(132, "Tanishq", 90000)
# print(tanishq.withdraw(1000))
# print(tanishq.withdraw(10000))

# print(tanishq.display_balance())


# magic methods


class Cat:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed

    # making human readable with magic methid..print internally calls str
    def __str__(self):
        return f"HI im {self.__name} with speed  {self.__speed}"

    def __repr__(self):
        return f"Cat('{self.__name}',{self.__speed})"

    def __add__(self, other):
        return self.__speed + other.__speed

    def speak(self):
        return "meow meow"


x = [5, 67, 6]
print(dir(x))


pichu = Cat("pichu", 30)
print(pichu)
print(repr(pichu))
