y_true = [int(x) for x in input().split()]
y_pred =  [int(x) for x in input().split()]

from numpy import array
x = [[0.,0.],[0.,0.]]
for i in range(len(y_true)):
    if y_true[i] == 1:
        if y_pred[i] == 1:
            x[0][0] += 1
        else:
            x[1][0] += 1
    else:
        if y_pred[i] == 0:
            x[1][1] += 1
        else:
            x[0][1] += 1
print(array(x))