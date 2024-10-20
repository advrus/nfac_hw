def is_prime(n: int) -> bool:    
    if n < 2:
        return False
    if n > 3:
        if n % 2 == 0 or n % 3 == 0:
            return False
        else:
            return True
    else:
        return True
    # write your code here
    pass
#print(is_prime(4))

def nth_fibonacci(n: int) -> int:
    # it is already known that first and second fibonacci nums are 0 and 1.
    # so when we search for needed fib number we just go to 3rd, 4th ....nth number by adding 2 previoous numbers
    fib_prev = 1
    fib_prev2 = 0
    fib_n = 0

    if n == 2:
        return 1
    if n == 1:
        return 0

    #fib_n = 0
    for x in range(n-2):
        fib_n = fib_prev + fib_prev2
        fib_prev, fib_prev2 = fib_n, fib_prev    
    return fib_n
    pass

"""
Exercise-3: factorial
Write a function "factorial(n: int) -> int" that takes an integer 'n' and returns the factorial of 'n'.

Example:
factorial(5) -> 120
factorial(6) -> 720
"""


def factorial(n: int) -> int:
    fact_num = 1
    for i in range(1,n+1):
        fact_num *= i
    return fact_num
    
    
    pass
"""
Exercise-4: count_vowels
Write a function "count_vowels(s: str) -> int" that 
takes a string 's' and returns the number of vowels in the string.

Example:
count_vowels("hello") -> 2
count_vowels("world") -> 1
"""

def count_vowels(s: str) -> int:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "O", "U", "I"]
    counter = 0
    s.split()
    for i in s:
        if i in vowels:
            counter += 1
    return counter

    # write your code here
    pass

"""
Exercise-5: sum_of_digits
Write a function "sum_of_digits(n: int) -> int" that 
takes an integer 'n' and returns the sum of its digits.

Example:
sum_of_digits(12345) -> 15
sum_of_digits(98765) -> 35

"""
def sum_of_digits(n: int) -> int:
    nums = 0
    n = abs(n)
    
    while n > 0:
        nums += n % 10
        n = n // 10
    return nums
    # write your code here
    pass


"""
Exercise-6: reverse_string
Write a function "reverse_string(s: str) -> str" that takes a string 's' and returns the string reversed.

Example:
reverse_string("hello") -> "olleh"
reverse_string("world") -> "dlrow"
"""

def reverse_string(s: str) -> str:
    return s[::-1]
    pass

"""
Exercise-7: sum_of_squares
Write a function "sum_of_squares(n: int) -> int" that takes an integer 'n' and 
returns the sum of squares of all integers from 1 to 'n'.

Example:
sum_of_squares(4) -> 30
sum_of_squares(5) -> 55
"""

def sum_of_squares(n: int) -> int:
    counter = 0

    for i in range(n+1):
        counter += i ** 2

    return counter
    # write your code here
    pass

"""
Exercise-8: collatz_sequence_length
Write a function "collatz_sequence_length(n: int) -> int" that takes an 
integer 'n' and returns the length of the Collatz sequence starting with 'n'.

Example:
collatz_sequence_length(6) -> 9
collatz_sequence_length(27) -> 112
"""

def collatz_sequence_length(n: int) -> int:
    counter = 1 # the number itself is also considered as part of length
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            counter += 1
        else:
            n = n * 3 + 1
            counter += 1
    return counter
    # write your code here
    pass

"""
Exercise-9: is_leap_year
Write a function "is_leap_year(year: int) -> bool" that takes an 
integer 'year' and returns True if 'year' is a leap year, and False otherwise.

Example:
is_leap_year(2000) -> True
is_leap_year(1900) -> False
"""

def is_leap_year(year: int) -> bool:

    if year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0 and year % 10 != 0:
        return True
    elif year % 4 == 0:
        return True
    else:
        return False
    # write your code here
    pass

"""
Exercise-10: count_words
Write a function "count_words(s: str) -> int" that takes a string 's' and 
returns the number of words in the string. Assume words are separated by spaces.

Example:
count_words("Hello world") -> 2
count_words("This is a test") -> 4
"""


def count_words(s: str) -> int:
    x = s.split(" ")
    word_count = 0
    for i in x:
        if i != "":
            word_count += 1
    return word_count
    pass


"""
Exercise-11: is_palindrome
Write a function "is_palindrome(s: str) -> bool" that takes a string 's' and 
checks if the string is a palindrome. The function should return True if the 
string is a palindrome, and False otherwise.

Example:
is_palindrome("racecar") -> True
is_palindrome("hello") -> False
"""

def is_palindrome(s: str) -> bool:
    return s == s[::-1]
    # write your code here
    pass

"""
Exercise-12: sum_of_multiples
Write a function "sum_of_multiples(n: int, x: int, y: int) -> int" that 
takes three integers 'n', 'x', and 'y', and returns the sum of all the 
numbers from 1 to 'n' (inclusive) that are multiples of 'x' or 'y'.

Example:
sum_of_multiples(10, 3, 5) -> 33
sum_of_multiples(20, 7, 11) -> 168 # HERE IS A MISTAKE
"""

def sum_of_multiples(n: int, x: int, y: int) -> int:
    counter = 0
    for i in range(1, n +1):
        if i % x == 0 or i % y == 0:
            counter += i
    
    return counter

    # write your code here
    pass

"""
Exercise-13: gcd
Write a function "gcd(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their greatest common divisor (GCD).

Example:
gcd(56, 98) -> 14
gcd(27, 15) -> 3
"""

def gcd(a: int, b: int) -> int:
    divi = 0
    for i in range(1, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            divi = i 
    return divi
    # write your code here
    pass


"""
Exercise-14: lcm
Write a function "lcm(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their least common multiple (LCM).

Example:
lcm(5, 7) -> 35
lcm(6, 8) -> 24
"""

def lcm(a: int, b: int) -> int:
    i = 1
    if a == 0 and b == 0:
        return 0
    
    while True:
        if i * min(a,b) % a == 0 and i * min(a,b) % b == 0:
            return i * min(a,b)
            #i += 1
            break
        i += 1
    #return number

    # write your code here
    pass


"""
Exercise-15: count_characters
Write a function "count_characters(s: str, c: str) -> int" that 
takes a string 's' and a character 'c', and returns the number of occurrences of 'c' in 's'.

Example:
count_characters("hello world", "l") -> 3
count_characters("apple", "p") -> 2


"""

def count_characters(s: str, c: str) -> int:
    counter = 0
    for i in s:
        if i == c: 
            counter += 1
    return counter
    # write your code here
    pass

"""
Exercise-16: digit_count
Write a function "digit_count(n: int) -> int" that takes an 
integer 'n' and returns the number of digits in 'n'.

Example:
digit_count(123) -> 3
digit_count(4567) -> 4
"""

def digit_count(n: int) -> int:
    counter = 0
    if n == 0:
        return 1
    else:
        while n >= 1:
            if n / 10 > 0:
                counter +=1
                n = n / 10
                #print(n)
            
        return counter
    # write your code here
    pass
"""
Exercise-17: is_power_of_two
Write a function "is_power_of_two(n: int) -> bool" that takes an integer 'n' 
and returns True if 'n' is a power of 2, and False otherwise.

Example:
is_power_of_two(8) -> True
is_power_of_two(10) -> False
"""

def is_power_of_two(n: int) -> bool:
    is_it_TRUE = True
    while n > 1:
        if n % 2 != 0:
            is_it_TRUE = False
        n = n / 2
    return is_it_TRUE
    # write your code here
    pass

"""
Exercise-18: sum_of_cubes
Write a function "sum_of_cubes(n: int) -> int" that takes an integer 'n' 
and returns the sum of the cubes of all numbers from 1 to 'n'.

Example:
sum_of_cubes(3) -> 36
sum_of_cubes(4) -> 100
"""

def sum_of_cubes(n: int) -> int:
    sum_value = 0
    for i in range(n + 1):
        sum_value += i ** 3

    return sum_value
    # write your code here
    pass

"""
Exercise-19: is_perfect_square
Write a function "is_perfect_square(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is a perfect square, and False otherwise.

Example:
is_perfect_square(9) -> True
is_perfect_square(10) -> False

"""
def is_perfect_square(n: int) -> bool:
    square_root = n ** 0.5

    if square_root ** 2 == n:
        return True
    else:
        return False
    
    # write your code here
    pass

"""
Exercise-20: is_armstrong_number
Write a function "is_armstrong_number(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is an Armstrong number, and False otherwise.

Example:
is_armstrong_number(153) -> True
is_armstrong_number(370) -> True
"""

def is_armstrong_number(n: int) -> bool:
    a = str(n)
    number = 0

    for i in a:
        number += int(i) ** len(a)

    if n == number:
        return True
    else:
        return False
    # write your code here
    pass

