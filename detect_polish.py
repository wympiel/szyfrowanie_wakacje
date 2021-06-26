# Moduł wykrywania języka polskiego:
# Aby użyć tego programu, należy skorzystać z następujących poleceń:

# Aby użyć tego programu, należy skorzystać z następujących poleceń:
# import detectEnglish
# detectEnglish.isEnglish(dowolnyCiągTekstowy)  # Wartością zwrotną jest True lub False
# (W katalogu programu musi znajdować się plik o nazwie dictionary.txt, zawierający słowa polskie

UPPERLETTERS = 'AĄBCĆDEEFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'


def load_dictionary():
    dictionary_file = open('dictionary_pl2.txt')
    polish_words = {}
    for word in dictionary_file.read().split('\n'):
        polish_words[word] = None
    dictionary_file.close()
    return polish_words


POLISH_WORDS = load_dictionary()


def get_polish_count(message):
    message = message.lower()
    print(message)
    message = remove_non_letters(message)
    possible_words = message.split()

    if not possible_words:
        return 0.0  # Lista jest pusta więc wartością zwrotną jest 0.0
    matches = 0
    for word in possible_words:
        if word in POLISH_WORDS:
            matches += 1
    return float(matches) / len(possible_words)


def remove_non_letters(message):
    letters_only = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            letters_only.append(symbol)
    return ''.join(letters_only)


def is_polish(message, word_percentage=20, letter_percentage=85):
    # Domyślnie 20% słów musi istnieć w pliku słownika,
    # a 85% wszystkich znaków musi być literami i spacjami
    # (nie znakami przestankowymi)

    words_match = get_polish_count(message) * 100 >= word_percentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = float(num_letters) / len(message) * 100
    letters_match = message_letters_percentage >= letter_percentage
    return words_match and letters_match
