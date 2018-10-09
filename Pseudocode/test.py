while True:
    try:
        number1 = int(input('give me the first number:'))
    except ValueError:
        break;
    try:
        number2 = int(input('give me the second number:'))
    except ValueError:
        break;
    _sum = number1 + number2
    print("The sum is:", _sum)
    if _sum < 10:
        break

