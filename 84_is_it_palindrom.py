def is_palindrome(word):
    word = word.lower()  
    return word == word[::-1]


word = input("")
if is_palindrome(word):
    print(f"palindrome.")
else:
    print(f"not palindrome.")