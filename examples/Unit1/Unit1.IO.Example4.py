#Open file to read
def main():
    file_test = open("test.txt", "r")
    print(file_test.read())
if __name__ == '__main__':
    main()