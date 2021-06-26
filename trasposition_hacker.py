# Łamanie szyfru przestawieniowego:

import pyperclip, detect_polish, transposition_decrypt


def main():
    my_message = """Zon wdzitsrseazoą kewdjicyee h kspnr toy"""

    hacked_message = hack_transposition(my_message)

    if hacked_message is None:
        print('Deszyfrowanie zakończyło się niepowodzeniem.')
    else:
        print('Deszyfrowana wiadomość została skopiowana do schowka.: ')
        print(hacked_message)
        pyperclip.copy(hacked_message)


def hack_transposition(message):
    print('łamanie szyfru....')

    # Program Pythona można zatrzymać w dowolnym momencie przez naciśnięcie klawiszy
    # Ctrl+C (Windows) lub Ctrl+D (macOS i Linux):
    print('Naciśnij klawisze Ctrl+C aby w dowolnym momencie zakończyć działanie programu.')

    # Podejście typu brute force, które w tym programie oznacza iterację przez wszystkie możliwe klucze
    for key in range(1, len(message)):
        print(f'Sprawdzanie klucza # {key}....')

        decrypted_text = transposition_decrypt.decrypt_message(key, message)
        if detect_polish.is_polish(decrypted_text):
            # Użytkownik powinien potwierdzić, czy tekst został deszyfrowany prawidłowo
            print()
            print('Potencjalnie udane złamanie szyfru:')
            print(f'Klucz {key}: {decrypted_text[:100]} ')
            print()
            print('Wpisz D aby zakończyć. Dowolny nny klawisz kontynuuje łamanie szyfru:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decrypted_text

    return None


if __name__ == '__main__':
    main()
