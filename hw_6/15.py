def numbers():
    int_1 = int(input("Enter number #1: "))
    int_2 = int(input("Enter number #2: "))
    quotient = int_1 // int_2
    remainder = int_1 % int_2
    return quotient, remainder
print(numbers())
