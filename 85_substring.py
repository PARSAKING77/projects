def has_abba(s):
    for i in range(len(s) - 2):
        if s[i:i+2] == "AB" or s[i:i+2] == "BA":
            for j in range(i+2, len(s)):
                if s[j-2:j] == "AB" or s[j-2:j] == "BA":
                    return "YES"
    return "NO"


s = input("")
print(has_abba(s))