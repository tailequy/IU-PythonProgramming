def sum_number(*args):
    total_sum = sum(args)
    return total_sum
def main():
    result_1 = sum_number(1, 2, 3, 4, 5)
    print("result_1: {}".format(result_1))
    result_2 = sum_number(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("result_2: {}".format(result_2))
if __name__ == '__main__':
    main()