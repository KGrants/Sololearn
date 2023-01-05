file = open("/usercode/files/books.txt", "r")
for line in file:
    print(line[0] +str(len(line.strip())))

file.close()