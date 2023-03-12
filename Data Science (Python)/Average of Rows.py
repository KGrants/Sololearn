import numpy as np

n, p = [int(x) for x in input().split()]


arr=[]
for i in range(n):
    line=input().split()
    arr.append(list(map(float,line)))

values=np.array(arr)

print(np.round(values.mean(axis =1),2))