# Łamanie szyfru Cezara:

message = 'g2Jwr67Jz2wnJ7nw1nJ0vnq2z2śćM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Iteracja przez wszystkie możliwe klucze:
for key in range(len(SYMBOLS)):
    # Bardzo ważne jest przypisanie pustego ciągu tekstowego zmiennej
    # translated, aby usunąć wartość zmiennej przypisaną w poprzedniej iteracji:
    translated = ''

    # Iteracja przez wszystkie symbole w zmiennej message:
    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            translated_index = symbol_index - key

            # Obsługa zawinięcia:
            if translated_index < 0:
                translated_index = translated_index + len(SYMBOLS)
            #Dołączenie szyfrowanego symbolu:
            translated = translated + SYMBOLS[translated_index]

        else:
            # Dołączenie symbolu bez jego wcześniejszego szyfrowania lub deszyfrowania:
            translated = translated + symbol

    # Wyświetlenie wszystkich możliwych danych wyjściowych:
    print(f'Klucz #{key}:  {translated}')