for numero in range(1, 101):
    if numero % 3==0 and numero % 5==0:
        print('Fizzbuzz')
    if numero % 3==0:
     print('fizz')
    if numero % 5==0:
        print('buzz')
    else:
     print(numero)
    