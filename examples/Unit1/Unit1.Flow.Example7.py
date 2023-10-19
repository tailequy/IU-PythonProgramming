#for loop with break and continue
def main():
    ebooks = ["python", "perl", "ruby"]
    for item in ebooks:
        if item == "ruby":
            break
        else:
            print(item)
            continue
if __name__ == '__main__':
    main()