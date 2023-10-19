#The “Path()” object can explicitly convert a Unix path into a Windows-formatted path
from pathlib import *
def main():
    folder_path = Path(r"D:/IU University/2023/Programming with Python/Examples")
    file_name = "test.txt"
    file_path_name = folder_path / file_name
    path_on_windows = PureWindowsPath(file_path_name)
    print(path_on_windows)
if __name__ == '__main__':
    main()