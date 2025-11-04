def find_proper_nouns(text):
    sentences = text.replace(',', '.').split('.')
    proper_nouns = []
    word_count = 0

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            words = sentence.split()
            for i, word in enumerate(words[1:], 2):
                word = word.rstrip('.').rstrip(',')
                if word and word[0].isupper() and not word.isdigit():
                    proper_nouns.append(f'{word_count + i}:{word}')
            word_count += len(words)

    if not proper_nouns:
        return 'None'
    return '\n'.join(proper_nouns)

text = input()
print(find_proper_nouns(text))