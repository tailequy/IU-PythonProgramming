def main():
    list_example = [1, 2, 3, "a", "b", "c"]
    print("An example of a list is: {}".format(list_example))
    tuple_example = (1, 2, 3, "a", "b", "c")
    print("An example of a tuple is: {}".format(tuple_example))
    dictionary_example = {1:"a", 2:"b", 3:"c"}
    print("An example of a dictionary is: {}".format(dictionary_example))
    set_example = set([1, 2, 3, 4, 5])
    print("An example of a set is: {}".format(set_example))
    frozenset_example = frozenset([1, 2, 3, 4, 5])
    print("An example of a frozenset is: {}".format(frozenset_example))
if __name__ == '__main__':
    main()