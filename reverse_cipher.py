# Szyfr odwrotny:

message = 'Trzy osoby mogą zachować tajemnicę, jeśli dwie z nich nie żyją.'
translated = ''
i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
