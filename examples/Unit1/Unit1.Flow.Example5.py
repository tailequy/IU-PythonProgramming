#While loop
def main():
    ebooks = ["python", "perl", "ruby"]
    i = 0
    while ebooks[i] != "ruby":
        print(ebooks[i])
        i += 1
if __name__ == '__main__':
    main()