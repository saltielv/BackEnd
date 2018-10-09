'''
Calculadora minimalista
Las únicas operaciones que se tendrán disponibles serán suma y resta.

Empezará pidiendo un número seguido del signo y después el segundo,
finalizando con el resultado de la operación correspondiente.
Se mantendrá en un ciclo hasta que se ingrese la palabra "salir":
'''

flag = True
try:
    while True:
        if flag:
            number1 = int(input('Give me the first number:'))
            flag = False
        operation = (input('Give me the operation (+/-):'))
        if operation == 'exit':
            break
        number2 = int(input('Give me the other number:'))
        if operation == '+':
            number1 += number2
        elif operation == '-':
            number1 -= number2
        else:
            raise ValueError('Operation error!')
        print(number1)
except ValueError as error:
    print('Oops!', error)