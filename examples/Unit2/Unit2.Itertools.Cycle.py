from itertools import cycle
def main():
    person = cycle(["employee","customer"])
    count = 0
    while(count != 6):
        print(next(person))
        count+=1
if __name__ == '__main__':
    main()