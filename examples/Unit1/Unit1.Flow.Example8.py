#Python includes a “pass” statement to define a null operation — when it is executed, nothing happens in the program.
#This statement is used for syntactical purpose when no code needs to be executed.
def print_no_one(value):
    if value == 1:
        pass
    else:
        print(value)
if __name__ == '__main__':
    print_no_one(0)