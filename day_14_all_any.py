print(all([True, False, True]))
print(any([True, False, True]))


marks = [50, 40, 20, 90]
if all([mark > 40 for mark in marks]):
    print("pass")

else:
    print("fail")
