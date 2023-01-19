file = open("/usercode/files/books.txt")
input = int(input())
text = file.read()

print(text[:input])

file.close()
