def anagrams(a, b):
    a_splitted = sorted(list(a))
    b_splitted = sorted(list(b))

    if a_splitted==b_splitted:
        return "The words are anagrams"
    else:
        return "wrong"

print(anagrams("taxi", "xati"))



