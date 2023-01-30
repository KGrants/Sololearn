text = "Amy has 128 dollars, while David has 54 dollars. Amy is going to the zoo. David watches soccer."
n = input()
u = input()
print(text.count(n))
text=text.replace(n,u)
print(text)