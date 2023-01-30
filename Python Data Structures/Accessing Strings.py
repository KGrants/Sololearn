n = input()
sum = 0
for i in n:
    if i.lower() in "aeiou":
        sum+=1

print(sum)