def str_to_int():
    string = input("Enter your number as a string: ")
    y = type(string)
    string_to_int = int(string)
    x = type(string_to_int)
    return string_to_int, y,  x

print(str_to_int())
