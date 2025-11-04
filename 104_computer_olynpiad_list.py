def standardize_name(name):

    parts = name.split('.')
    gender = parts[0]
    name = parts[1]
    lang = parts[2]


    name = name.capitalize()
    return gender, name, lang



def main():

    n = int(input())  
    females = []
    males = []

    for _ in range(n):

        name = input()
        gender, name, lang = standardize_name(name)

        if gender == 'f':
            females.append((name, lang))
        else:
            males.append((name, lang))


    females.sort()
    males.sort()

 


    for name, lang in females:
        print('f', name, lang)
    for name, lang in males:
        print('m', name, lang)


if __name__ == '__main__':
    main()