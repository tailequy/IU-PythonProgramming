def main():
    # strings are immutable objects
    string_value = "python"
    print(string_value)
    print(string_value[5])
    # an error occurred. string_value[5] can't be changed
    string_value[5] = "m"
    print(string_value[5])
if __name__ == '__main__':
    main()