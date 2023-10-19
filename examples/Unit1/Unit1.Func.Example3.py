def payment_day(working_hours, payment_hour=25):
    '''
    calculate payment by day
    :param working_hours: amount of working hours
    :param payment_hour: payment by hour
    :return: payment by day
    '''
    total_payment = working_hours * payment_hour
    return total_payment
working_hours = 8
# calling function
total_payment = payment_day(working_hours)
print("The total payment is: {}".format(total_payment))