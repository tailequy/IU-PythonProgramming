'''
Python has a “pathlib” library to deal with files and paths. To use this library, the
path or file name need to be passed to the “Path()” object using forward slashes
'''
from pathlib import Path
def main():
    folder_path = Path(r"D:/IU University/2023/Programming with Python/Examples")
    file_name = "test.txt"
    file_path_name = folder_path / file_name
    file_test = open(file_path_name, "r")
    for item in file_test:
        print(item)
if __name__ == '__main__':
    main()