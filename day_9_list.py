list = [1, 2, 3, 4, 44, 55, 33]
# print(len(list))
# print(type(list))    #list
# print(list[2])       #index
# print(list[0:4])     #first 4 values
# print(list[::-1])    #reverses

# list.append(78)      # to add integers

# list.insert(4,46)    #to insert at particular index
# print(list)

# groc=[100,200,300,400]    # to add 2 list into one

# groce=[450,333,454]
# output=[groc+groce]
# print(output)

# output.pop()                #to delete

# pri=[10,20,30]
# pri_copy=pri                 #they'll have the same memory address
# pric1=[10,20,30]             #copy by reference
# pri_copy.append(600)
# pri.append(700)
# pric1.append(800)

# print(pri,pri_copy,pric1)

# p1=[3,4,5,2]
# p2=p1.copy()                   #copy by value
# print(p2)

# p3=p1[:]                        # another method to copu

# print(id(p1),id(p2),p3)            #to check

# h1 = [22, 3, 4, 5, 44]
# h1.remove(3)  # remove
# # print(h1)
# st = "i love python"
# print(st[::3])

# clo=['gold']*3
# # print(clo)

# shop='vanila,lime,choc'
# shop1=shop.split(',')
# print(shop1,shop1[1])


# # list- st:join
# avatar = ["ire", "water"]
# print(",".join(avatar))

# ex

# scram= ' world the save to time no is there'
# scram1 = ' '.join(scram.split()[::-1])
# print(scram1)


# replacing values
# avatar = ["fire", "water", "earth", "air"]
# avatar[1:3] = ["diamaond", "platinumm", "golf"]
# print(avatar)


# TUPLE
person = ("me", "she", "he")
print(person[0])

# methods available
print(person.count("he"))
print(person.index("me"))
print(len(person))  # len works becos we didtn modify the tuple
