def transform_word(word):
    upper_count = sum(1 for char in word if char.isupper())
    lower_count = len(word) - upper_count
    if upper_count > lower_count:
        return word.upper()
    else:
        return word.lower()

print(transform_word("Hello"))
print(transform_word("WORLD"))
print(transform_word("MixedCase"))