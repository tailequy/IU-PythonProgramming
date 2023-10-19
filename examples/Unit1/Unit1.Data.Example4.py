def main():
    # string length using len() method
    string_0 = "Python is becoming the worlds most popular programming language today"
    print(len(string_0))
    # string concatenation using + sign
    string_1 = "Python is becoming the worlds most " + "popular programming language today"
    print(string_1)
    # string concatenation using join() method
    string_2 = "".join(("Python is becoming the worlds most " , "popular programming language today"))
    print(string_2)
    # substrings (or splices) using [start, start + length]
    # get 'Python' word from the start
    string_3 = string_0[0:6]
    print(string_3)
    # remove 'Python' word from the start
    string_4 = string_0[7:]
    print(string_4)
    # remove 'today' word from the end
    string_5 = string_0[:-6]
    print(string_5)
    # select 'programming' word only
    string_6 = string_0[43:54]
    print(string_6)
    # count how many times letter 'a' is in string
    string_7 = string_0.count("a")
    print(string_7)
    # find what position 'language' word starts
    string_8 = string_0.find("language")
    print(string_8)
    # remove any whitespace from the start to end
    string_9 = string_0.strip()
    print(string_9)
    # convert to lower case
    string_10 = string_0.lower()
    print(string_10)
    # convert to upper case
    string_11 = string_0.upper()
    print(string_11)
    # replace 'Python' word with 'Java'
    string_12 = string_0.replace("Python", "Java")
    print(string_12)
    # split string into substring in 'most' word
    string_13 = string_0.split("most")
    print(string_13)
    # check if 'popular' word is in string
    string_14 = "popular" in string_0
    print(string_14)
    # check if 'POPULAR' word is in string
    string_15 = "POPULAR" not in string_0
    print(string_15)
if __name__ == '__main__':
    main()