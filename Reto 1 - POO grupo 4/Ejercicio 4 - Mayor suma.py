# Ejercicio 4
def highestConsecutiveSum(numbersList):
    if len(numbersList) < 2:
        return "Error: la lista debe tener al menos dos números para ejecutar esta función."

    max_sum = numbersList[0] + numbersList[1]

    for i in range(1, len(numbersList) - 1):
        sum = numbersList[i] + numbersList[i + 1]
        if sum > max_sum:
            max_sum = sum

    return max_sum

numbers = input('Ingresa la lista números en una sola línea y separados por espacios sin ningún caracter extra: ')
numbersString = numbers.split()
integerNumbers = []
approve = True

# Validar que todos los números ingresados son números enteros
for stringNumber in numbersString:
    try:
        newNumber = int(stringNumber)
        integerNumbers.append(newNumber)
        approve = True
    except:
        print(f'Ingresaste un caracter NO válido en "{stringNumber}"')
        approve = False
        break

if (approve):
    result = highestConsecutiveSum(integerNumbers)
    print("La mayor suma entre dos elementos consecutivos es:", result)
