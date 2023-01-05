txt = input().split(" ")
max = ""

for i in txt:
    if len(i)>len(max):
        max = i
#your code goes here
print(max)