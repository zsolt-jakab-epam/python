def fibonacci(number):
    fibonacciSeries = [0,1]
    i = 2
    while i <= number:
        fibonacciSeries.append(fibonacciSeries[i-1] + fibonacciSeries[i-2])
        i = i + 1
    return fibonacciSeries[number]

number = int(input("Give a number, I give you the fibonacci: "))
print(fibonacci(number))