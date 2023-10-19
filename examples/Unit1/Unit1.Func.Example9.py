#Nested Functions
def outer_function(x):
    ''' enclosing function
    '''
    def inner_function():
        '''
        nested function
        '''
        # nonlocal x
        x = 5
        print("The x value inside inner function is: {}".format(x))
        x_local = x * 2
        print("The x local value inside inner function is {}".format(x_local))
    inner_function()
    print("The x value outside inner function is: {}".format(x))
def main():
    value = 10
    value_double = outer_function(value)
if __name__ == '__main__':
    main()