import numpy as np
n = int(input())
x = []
for i in range(n):
    x.append([float(x) for x in input().split()])

x1 = np.array([0,0])
x2 = np.array([2,2])

x = np.array(x)
a = []
b = []
for i in range(n):
    if np.sqrt(((x[i]-x1)**2).sum()) <= np.sqrt(((x[i]-x2)**2).sum()):
        a.append(x[i])
    elif np.sqrt(((x[i]-x1)**2).sum()) > np.sqrt(((x[i]-x2)**2).sum()):
        b.append(x[i])

a = np.array(a)
b = np.array(b)

sum_a_1=0
sum_a_2=0
sum_b_1=0
sum_b_2=0

for i in range(len(a)):
    sum_a_1 += a[i][0]
    sum_a_2 += a[i][1]
for i in range(len(b)):
    sum_b_1 += b[i][0]
    sum_b_2 += b[i][1]

if (len(a)!=0):
    sum_a_1/=len(a)
    sum_a_2/=len(a)
    sum_a_1 = sum_a_1.round(2)
    sum_a_2 = sum_a_2.round(2)

if (len(b)!=0):
    sum_b_1/=len(b)
    sum_b_2/=len(b)
    sum_b_1 = sum_b_1.round(2)
    sum_b_2 = sum_b_2.round(2)

c = []
c.append(sum_a_1)
c.append(sum_a_2)

d = []
d.append(sum_b_1)
d.append(sum_b_2)

c = np.array(c)
d = np.array(d)

if len(a) == 0:
    print(None)
else:
    print(c)
if len(b) == 0:
    print(None)
else:
    print(d)
    

