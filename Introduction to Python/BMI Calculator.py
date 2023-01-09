weigth = float(input())
heigth = float(input())

result = weigth/(heigth*heigth)

if result < 18.5:
    print("Underweight")
elif result >18.5 and result < 25:
    print("Normal")
elif result >=25 and result < 30:
    print("Overweight")
else:
    print("Obesity")