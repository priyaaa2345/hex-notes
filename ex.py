# try exercises here


# every error as same base class  ie,. excepion
class NegativeErrorException(Exception):
    def __init__(self, value):
        self.value = value
        self.message = "negative numbers are not allowed"
        super().__init__(self.message)

    # overriding the base class __str__
    def __str__(self):
        return f"{self.value} ->{self.message}"


# error class
def only_positive_num():
    try:
        x = -10
        if x < 10:
            raise NegativeErrorException(x)
    except NegativeErrorException as err:
        print(err)


if __name__ == "__main__":
    only_positive_num()
