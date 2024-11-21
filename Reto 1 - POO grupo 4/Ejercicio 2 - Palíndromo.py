# EJERCICIO 2

def palindromevalidation():
    word = input('Ingresa la palabra: ')

    # Convertir a minúsculas para ignorar mayúsculas/minúsculas
    word = word.lower()

    lenght = len(word)
    halfLenght = lenght // 2
    normalPosition = 0
    palindrome = True

    for i in range(lenght - 1, halfLenght, -1):
        if (word[normalPosition] != word[i]):
            palindrome = False
            break
        normalPosition += 1

    if (palindrome):
        print(f'La palabra "{word}" SÍ es un palíndromo')
    else:
        print(f'La palabra "{word}" NO es un palíndromo')

palindromevalidation()