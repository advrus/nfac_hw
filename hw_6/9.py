number = int(input("Enter number to check for eveness: "))
is_even = True

if number % 2 ==0:
    is_even = True
else:
    is_even = False

print(f"The {number} is even? {is_even}")