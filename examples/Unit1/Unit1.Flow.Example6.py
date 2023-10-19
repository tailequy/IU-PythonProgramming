#for loop with break
def main():
    ebooks = ["python", "perl", "ruby"]
    for item in ebooks:
        print(item)
        if item == "perl":
            break
if __name__ == '__main__':
    main()