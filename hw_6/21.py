x = "racecar"

word_length = len(x)
first = int(word_length/2)

first_half = x[:first]
second_half = x[:-first-1:-1]

if first_half==second_half:
    print(f"the word \"{x}\" is a palindrome")
else:
    print(f"the word \"{x}\" is not palindrome")