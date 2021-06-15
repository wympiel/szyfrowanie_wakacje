#Szyfr Cezara:

import pyperclip

#CXiąg tekstowy przeznaczony do szyfrowania i deszyfrowania:
message = 'To jest moja tajna wiadomość'

#Klucz szyfrowania i deszyfrowania:
key = 13

# Określenie trybu pracy - szyfrowanie (encrypt) lub deszyfrowanie (decrypt):
mode = 'encrypt' #Przypisanie wartości encrypt lub decrypt

#Znaki, które można zaszyfrować
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Zmienna przechowująca zaszyfrowaną lub odszyfrowaną postać wiadomości:
translated = ''

for symbol in message:
    # UWAGA: Tylko symbole zdefiniowane w ciągu tekstowym SYMBOLS mogą być szyfrowane i deszyfrowane
    if symbol in SYMBOLS:
        symbol_index = SYMBOLS.find(symbol)

        # Przeprowadzenie szyfrowania i deszyfrowania:
        if mode == 'encrypt':
            translated_index = symbol_index + key
        elif mode == 'decrypt':
            translated_index = symbol_index - key

        # Obsługa zawinięcia, jeżeli zachodzi potrzeba:
        if translated_index >= translated_index - len(SYMBOLS):
            translated_index = translated_index - len(SYMBOLS)
        elif translated_index < 0:
            translated_index = translated_index + len(SYMBOLS)
        translated = translated + SYMBOLS[translated_index]
    else:
        # Dołączenie znaku bez jego wcześniejszego szyfrowania i deszyfrowania:
        translated = translated + symbol

# Wyświetlenie skonwertowanego ciągu tekstowego:
print(translated)
pyperclip.copy(translated)
