#for loop
def main():
    ebooks = ["python", "perl", "ruby"]
    #for item in ebooks:
    #    print("The eBook is: {}".format(item))
    for item in  range(len(ebooks)):
        print("The eBook is: {}".format(ebooks[item]))
if __name__ == '__main__':
    main()
    for i in range(0,10,2):
        print(i)