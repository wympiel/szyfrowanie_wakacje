import math
import pyperclip


def main():
    my_message = 'Zon wdzitsrseazoą kewdjicyee h kspnr toy'
    my_key = 8

    plaintext = decrypt_message(my_key, my_message)

    # Wyświetlenie znaku potoku (|) na końcu, na wypadek
    # gdyby szyfrowana wiadomość kończyła się spacją
    print(plaintext + '|')
    pyperclip.copy(plaintext)


def decrypt_message(key, message):
    """
    Ta funkcja deszyfrowania będzie symulowała "kolumny" i "wiersze"
    siatki, na której zostanie umieszczony zwykły tekst na podstawie
    listy ciągów tekstowych; najpierw trzeba obliczyć kilka wartości
    """
    # Liczba kolumn siatki
    num_of_columns = int(math.ceil(len(message) / float(key)))

    # Liczba wierszy siatki
    num_of_rows = key
    # Liczba zamazanych kratek w ostatniej kolumnie siatki
    num_of_shade_boxes = (num_of_columns * num_of_rows) - len(message)

    # Każdy ciąg tekstowy w zwykłym tekście repezentuje kolumnę w siatce
    plaintext = [''] * num_of_columns

    # Zmienne column i row wskazują kratkę, w której
    # ma zostać umieszczony następny znak szyfrogramu
    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        column += 1  # Wskazuje następną kolumnę

        # Jeżeli nie ma więcej kolumn LUB bieżąca kratka jest zamazana,
        # należy powrócić do pierwszej kolumny i przejść do następnego wiersza
        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shade_boxes):
            column = 0
            row += 1

    return ''.join(plaintext)


# Jeżeli program transpositionDecrypt.py został uruchomiony (a nie
# zaimportowany jako moduł), należy wywołać funkcję main()
if __name__ == '__main__':
    main()
