def math_divide(n1, n2):
    try:
        result = n1 / n2
        return result
    # except:
    #     return "oops an error"

    # for specific msgs
    except ZeroDivisionError:
        return "you cant divide by zero"

    # else: if there is no error

    else:
        print("division was successful")

    # finally : gets executed no mater what
    finally:
        print("operation done")


print(math_divide(10, 5))
print(math_divide(10, 0))
print(math_divide(15, 3))
