from collections import OrderedDict

n = int(input())
dictionary = OrderedDict()

for i in range(n):
    word, meaning = input().split()
    dictionary[word] = meaning

sentence = input().split()

translation = []
for word in sentence:
    if word in dictionary:
        translation.append(dictionary[word])
    else:
        translation.append(word)

print(' '.join(translation))