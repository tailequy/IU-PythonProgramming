def addition_two_number(number_1, number_2=100):
    """
    calculate the addition of two numbers
    :param number_1: first number
    :param number_2: second number
    :return: sum of first number plus
    """
    number_addition = number_1 + number_2
    return(number_addition)
number_1 = 100
number_2 = 200
result = addition_two_number(number_1)
print("The result is: {}".format(result))