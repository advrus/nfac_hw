def is_vowel():
    vowel = False
    ch = input("Enter character: ")

    if ch.lower() in ("a", "e", "i", "o", "u"):
        vowel = True

    return vowel
print(is_vowel())
