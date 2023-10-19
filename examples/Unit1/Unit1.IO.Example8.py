'''
The contents of a text file can be read without having to mess with opening and looping the file:
'''
from pathlib import Path
def main():
    folder_path = Path(r"D:/IU University/2023/Programming with Python/Examples")
    file_name = "test.txt"
    file_path_name = folder_path / file_name
    print(file_path_name.read_text())
if __name__ == '__main__':
    main()