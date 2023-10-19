def payment_day(working_hours, payment_hour=None):
    '''
    calculate payment by day
    :param working_hours: amount of working hours
    :param payment_hour: payment by hour
    :return: payment by day
    '''
    if payment_hour is not None:
        total_payment = working_hours * payment_hour
    else:
        total_payment = 0
    return total_payment
working_hours = 8
total_payment = payment_day(working_hours)
print("The total payment is: {}".format(total_payment))

#Other values
working_hours = 8
payment_hour = 25
total_payment = payment_day(working_hours, payment_hour)
print("The total payment is: {}".format(total_payment))