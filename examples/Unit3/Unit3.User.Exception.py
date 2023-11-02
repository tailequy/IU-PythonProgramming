class MyException(Exception):
    pass
    #def __init___(self, exception_parameter, exception_message):
    #    super().__init__(self, exception_parameter, exception_message)

def main():
    programming_language = ["JavaScript", "Python", "R", "Ruby", "PHP", "Java",
                            "C#", "C", "C++", "Julia", "Go", "Perl"]
    for item in programming_language:
        if item != "Python":
            raise MyException(item, "My exception was raised with exception argument: {}".format(item))
if __name__ == '__main__':
    main()