num = int(input())


def fibonacci(n):
    fib = [0,1]
    for i in range(n):
        fib.append(fib[i]+fib[i+1])
        print(fib[i])


fibonacci(num)