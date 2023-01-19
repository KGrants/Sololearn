n = int(input())

file = open("numbers.txt", "w+")
for i in range(n):
    file.write(str(i+1)+"\n")
file.close()


f = open("numbers.txt", "r")
print(f.read())
f.close()