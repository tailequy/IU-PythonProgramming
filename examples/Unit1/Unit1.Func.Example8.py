x_global = 100
def calculate_double(x):
    global x_local
    x_local= x * 2
    return x_local
def main():
    value = 10
    value_double = calculate_double(value)
    print("The value double in main() is: {}".format(value_double))
    print("The x local in main() is: {}".format(x_local))
if __name__ == '__main__':
    main()
    print("The x global after main() is: {}".format(x_global))