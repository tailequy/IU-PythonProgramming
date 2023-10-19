#open file to append
def main():
    file_test = open("test.txt", "a")
    file_test.write("Add this new line to the end of the file test.txt")
    file_test.close()
if __name__ == '__main__':
    main()