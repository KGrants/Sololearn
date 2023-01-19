price = int(input())
perc = int(input())

res = (lambda x,y:x*y/100)(price, perc)

print(res)
