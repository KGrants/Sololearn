import string
import sys

def balanced(expression):
    a = []
    for i in expression:
        if i == '(':
            a.append(i)
        if i == ')':
            if len(a)==0:
                return False
            b = a.pop()
            if b == '(':
                continue
            else:
                return False
    if len(a)>0:
        return False
    else:
        return True
    

print(balanced(input()))