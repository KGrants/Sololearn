class CallCenter:
    def __init__(self):
      self.customers = []

    def is_empty(self):
      return self.customers == []

    def add(self, x):
      self.customers.insert(0, x)

    def next(self):
      return self.customers.pop()


c = CallCenter()

while True:
    n = input()
    if n == 'end':
        break
    c.add(n)

sum = 0

while(len(c.customers)>0):
    a = c.next()
    if (a == "general"):
      sum += 5
    else:
      sum += 10

print(sum)
