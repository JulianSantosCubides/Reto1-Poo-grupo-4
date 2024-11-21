# EJERCICIO 1

def calculatorFunction():
    number1 = int(input('Ingresa el primer número: '))
    number2 = int(input('Ingresa el segundo número: '))
    operation = input('Ingresa la operación que quieres ejecturar ("+", "-", "*", "/"): ')

    if (operation == '+'):
        result = number1 + number2
    elif (operation == '-'):
        result = number1 - number2
    elif (operation == '*'):
        result = number1 * number2
    elif (operation == '/'):
        result = number1 / number2

    print('El resultado de la operación es: ', result)

calculatorFunction()