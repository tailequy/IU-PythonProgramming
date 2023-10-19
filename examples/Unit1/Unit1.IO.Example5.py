#Using for loop
def main():
    file_test = open("test.txt", "r")
    for item in file_test:
        print(item)
if __name__ == '__main__':
    main()