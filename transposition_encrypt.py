# Szyfr kolumnowy

import pyperclip


def main():
    my_message = 'Zdrowy rozsądek nie jest taki powszechny'
    my_key = 8

    cipher_text = encrypt_message(my_key, my_message)
    # Wyświetlenie szyfrogramu  na ekranie, ze znakiem potoku (|)na końcu,
    # na wypadek gdyby szyfrowana wiadomość kończyła się spacją:
    print(cipher_text + '|')

    # Skopiowanie szyfrogramu do schowka
    pyperclip.copy(cipher_text)


def encrypt_message(key, message):
    # Każdy ciąg tekstowy w szyfrogramie przedstawia kolumnę siatki:
    cipher_text = [''] * key

    # Itreracja przez poszczególne kolumny szyfrogramu:
    for column in range(key):
        current_index = column
        """
        Pętla będzie wykonywana, dopóki wartść current_index nie będzie 
        większa niz liczba okreslające długość wiadomości:
        """
        while current_index < len(message):
            # Znak zanjdujący się w położeniu current_index w zmiennej message
            # zostaje umieszczony na końcu bieżącej kolumny listy szyfrogramu:
            cipher_text[column] += message[current_index]

            # Zwiększenie wartości zmiennej current_index o wartość klucza:
            current_index += key

        # Konwersja listy szyfrogramu na wartość w postaci pojedynczego ciągu tekstowego i jej zwrot:
    return ''.join(cipher_text)


if __name__ == '__main__':
    main()
