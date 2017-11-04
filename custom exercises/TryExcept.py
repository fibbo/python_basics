def print_dictionary(some_dict):
    try:
        for key, value in some_dict.items():
            print("Key: {} : Value {}".format(key, value))
    except AttributeError:
        print("Caught AttributeError: argument is not a dictionary")



a_dict = {"asdf" : 1, "jkl;" : 2}
a_list = [1,2,3,4,5]
print_dictionary(a_dict)

print_dictionary(a_list)