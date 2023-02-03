s1 = input().split()
s2 = input().split()
sum = 0

for i in s1:
    if i in s2:
        sum+=1
        
print(sum)
