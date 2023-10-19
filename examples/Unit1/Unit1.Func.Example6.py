def print_dictionary(**kwargs):
    for key, value in kwargs.items():
        print("The value of {}: {}".format(key, value))
def main():
    print_dictionary(value1=1, value2="Python", value3=False, value4=3.14)
if __name__ == '__main__':
    main()