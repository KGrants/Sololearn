class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    def __add__(self, other):
        return (self.name +"&"+ other.name +        ' ('+str(self.capacity+other.capacity)+'L)')

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)