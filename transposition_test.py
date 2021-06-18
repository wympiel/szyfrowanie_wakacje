#Program do testowania działania programów szyfrujących i deszysfrujących
import random, sys, transposition_encrypt, transposition_decrypt

def main():
    random.seed(42) # Zdefiniowanie losowej wartości zalążka jako wartości statycznej.

    for i in range(20):   # Przeprowadzenie 20 testów
        # Wygenerowanie losowej wiadomości do zaszyfrowania.

        # Wiadomość będzie miała losowo wybraną długość:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Konwersja ciągu tekstowego wiadomości na listę, której elementy zostaną wymieszane:
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)  # Konwersja listy z powrotem na postać ciągu tekstowego

        print(f'Test # {message[:50]}...', (i + 1))

        # Sprawdzenie wszystkich możliwych kluczy dla każdej wiadomości:
        for key in range(1, int(len(message) /2)):
            encrypted = transposition_encrypt.encrypt_message(key, message)
            decrypted = transposition_decrypt.decrypt_message(key, encrypted)

            # Jeżeli rozszyfrowana wiadomość jest inna niż pierwotna, należy
            # wyświetlić komunikat błędu i zakończyć działanie programu:
            if message != decrypted:
                print(f'Niedopasowanie klucza {key} i wiadomości {message}.')
                print('Rozszyfrowana wiadomość: ' + decrypted)
                sys.exit()

    print('Test zastosowania szyfru przestawieniowego został zaliczony.')

    
if __name__ == '__main__':
    main()
