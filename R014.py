def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) #RECURSIVIDAD POR QUE LA FUNNCION SE LLAMA A SI MISMA

print(factorial(5)) 