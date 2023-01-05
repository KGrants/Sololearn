celsius = int(input())

def conv(c):
    c = 9/5 * c + 32
    return c

fahrenheit = conv(celsius)
print(fahrenheit)