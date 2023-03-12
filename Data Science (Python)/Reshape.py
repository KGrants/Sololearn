import numpy as np
r = int(input()) 
lst = [float(x) for x in input().split()]
arr = np.array(lst)
c = len(arr)/r
a = arr.reshape(int(r),int(c))
print(a.round(2))