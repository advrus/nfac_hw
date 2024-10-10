def swap():
    str1 = input("Enter swapping word: ")
    str2 = list(str1)
    str2[0], str2[-1] = str2[-1] , str2[0]

    return "".join(str2)
print(swap())

    