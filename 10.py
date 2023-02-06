def read_words_for_dictionary():
    words_for_dictionary = []
    dictionary_count = int(input())
    for _ in range(dictionary_count):
        words_for_dictionary.append(input())

    return words_for_dictionary


def create_dictionary(words_for_dictionary):
    dictionary ={}
    for word in words_for_dictionary:
        key = ''
        value = dictionary.get(key, [word]) + [word]
        dictionary.update({key: value})
        for letter in word[::-1]:
            key += letter
            value = dictionary.get(key, [word]) + [word]
            dictionary.update({key: value})

    return dictionary


def read_words():
    words = []
    words_count = int(input())
    for _ in range(words_count):
        words.append(input())

    return words


def find_rifm(word, dictionary):
    key = ''
    rifm_words = dictionary.get(key)
    if rifm_words is not None:
        for rifm_word in rifm_words:
            if rifm_word != word:
                rifm = rifm_word
                break

        for letter in word[::-1]:
            key += letter
            rifm_words = dictionary.get(key)
            if rifm_words is not None:
                for rifm_word in rifm_words:
                    if rifm_word != word:
                        rifm = rifm_word
                        break

    print(rifm)


words_for_dictionary = read_words_for_dictionary()
dictionary = create_dictionary(words_for_dictionary)
words = read_words()

for word in words:
    find_rifm(word, dictionary)

