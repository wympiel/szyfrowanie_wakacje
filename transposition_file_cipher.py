import time, os, sys, transposition_encrypt, transposition_decrypt


def main():
    input_filename = 'frankenstein.txt'
    # ZACHOWAJ OSTROŻNOŚĆ! Jeżeli plik wymieniony w zmiennej outputFilename
    # już istnieje, ten program nadpisze jego zawartość
    output_filename = 'frankenstein.encrypted.txt'
    my_key = 10
    my_mode = 'szyfrowanie'  # Przypisanie wartości 'szyfrowanie' lub 'deszyfrowanie'

    # Jeżeli plik danych wejściowych nie istnieje, program zakończy działanie
    if not os.path.exists(input_filename):
        print(f'To spowoduje nadpisanie pliku {output_filename}. (K)ontynuować czy (Z)akończyć pracę? ')
        response = input('> ')
        if not response.lower().startswith('k'):
            sys.exit()

    # Odczyt tekstu z pliku danych wejściowych
    file_obj = open(input_filename)
    content = file_obj.read()
    file_obj.close()

    print(f'{my_mode.title()}...')

    # Pomiar czasu operacji szyfrowania i deszyfrowania
    start_time = time.time()
    if my_mode == 'szyfrowanie':
        translated = transposition_encrypt.encrypt_message(my_key, content)
    elif my_mode == 'deszyfrowanie':
        translated = transposition_decrypt.decrypt_message(my_key, content)
    total_time = round(time.time() - start_time, 2)
    print(f'{my_mode.title()} trwało {total_time} sekundy.')

    # Zapisanie przetworzonego tekstu w pliku danych wyjściowych
    output_file_obj = open(output_filename, 'w')
    output_file_obj.write(translated)
    output_file_obj.close()

    print(f'Zakończono {my_mode} pliku {input_filename} ({len(content)}znaki).')

if __name__ == '__main__':
    main()