n = int(input())

dictionary = {}

for _ in range(n):
    words = input().split()
    persian, english, french, german = words[0], words[1], words[2], words[3]
    dictionary[english] = persian
    dictionary[french] = persian
    dictionary[german] = persian

sentence = input().split()

language_map = {
    'i': 'english',
    'me': 'english',
    'my': 'english',
    'je': 'french',
    'moi': 'french',
    'mon': 'french',
    'ich': 'german',
    'mich': 'german',
    'mein': 'german',
    'yo': 'spanish',
    'me': 'spanish',
    'mi': 'spanish',
    'io': 'italian',
    'me': 'italian',
    'mio': 'italian',
    'eu': 'portuguese',
    'me': 'portuguese',
    'meu': 'portuguese',
    'ja': 'dutch',
    'mij': 'dutch',
    'mijn': 'dutch',
    'man': 'persian',  # added persian language
    # add more languages here...
}

language = language_map.get(sentence[0].lower())

if language is None:
    print("Unknown language")
    exit()  # or raise an exception

translated_sentence = []
for word in sentence:
    if word in dictionary:
        translated_sentence.append(dictionary[word])
    else:
        translated_sentence.append(word)

print(' '.join(translated_sentence))