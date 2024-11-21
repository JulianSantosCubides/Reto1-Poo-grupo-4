# EJERCICIO 3

def findPrimeNumebrs():
    numbers = input('Ingresa la lista números en una sola línea y separados por espacios sin ningún caracter extra: ')
    primeNumbers = []
    numbersList = numbers.split()
    continueProccess = True

    dividersCounter = 0

    for number in numbersList:
        try:
            number = int(number)
            dividersCounter = 0
            halfNumber = number // 2
            if number == 1 or number == 2:
                dividersCounter = 0
            elif number < 1:
                dividersCounter = 1  # Para que inmediatamente detecte que no es primo
            else:
                for divider in range(2, (halfNumber + 1), 1):
                    if number % divider == 0:
                        dividersCounter += 1

            if (
                    dividersCounter == 0):  # Se utiliza cero, porque no se dividirá ni entre 1, ni entre el mismo número (solo se divide hasta la mitad). Entonces, si es primo, no debería encontrar ningún divisor en este bucle
                if number not in primeNumbers:
                    primeNumbers.append(number)
        except:
            print(f'Ingresaste un caracter NO válido en "{number}"')
            continueProccess = False

    if (continueProccess):
        if len(primeNumbers) > 0:
            print('La lista de números primos es: ', primeNumbers)
        else:
            print('No ingresaste ningún número primo')
    else:
        print('********* Ingresaste caracteres NO válidos, vuelve a intentarlo *********')

findPrimeNumebrs()