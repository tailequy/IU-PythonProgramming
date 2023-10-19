x_global = 100
def calculate_double(x):
    x_local = x * 2
    return x_local
def main():
    value = 10
    global x_global
    x_global = calculate_double(value)
    print("The value double in main() is: {}".format(x_global))
    #print("The x local in main() is: {}".format(x_local))
if __name__ == '__main__':
    main()
    print("The x global after main() is: {}".format(x_global))