'''
If you would like to return one line from the file, the method “readline()” can be used. The
general syntax of this method is “file.readline(size)” where the “size” parameter is
optional. It represents the number of bytes from the line that will return. The default number
is —1, which indicates the whole line
'''
def main():
    file_test = open("test.txt", "r")
    lines = file_test.readline(6)
    print(lines)
if __name__ == '__main__':
    main()