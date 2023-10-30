from itertools import count
def main():
    sequence = count(start=2.5, step=0.5)
    while(next(sequence) <= 8):
        print(next(sequence))
if __name__ == '__main__':
    main()


