#open files in Python for reading and writing data: open(mode, [buffering])
#Buffering: ‘0’ to switch buffering off (only allowed in binary mode) ‘1’
# to select line buffering (only usable in text mode) ‘integer > 1’ to indicate the size of a fixed-size chunk buffer
#“r”— read mode, which is used when the file is only being read.
#“w” — write mode, which is used to edit and write new information to the file (any existing
#files with the same name will be erased when this mode is activated).
#“a” — appending mode, which is used to add new data to the end of the file. New information is automatically appended to the end.
#“r+” — special read and write mode, which is used to handle both actions when working with a file.
def main():
    file_test = open("test.txt", "w")
    file_test.write( "Python is a great language.\nSure!\n")
    file_test.close()
if __name__ == '__main__':
    main()