def main():
    number_list = [1, 2, 3, 4, 5]
    number_list_iter = iter(number_list)
    # print 1
    print(next(number_list_iter))
    # print 2
    print(next(number_list_iter))
    # print 3
    print(next(number_list_iter))
    # print 4
    print(next(number_list_iter))
    # print 5
    print(next(number_list_iter))
    # an error occurred - StopIteration
    print(next(number_list_iter))
if __name__ == '__main__':
    main()