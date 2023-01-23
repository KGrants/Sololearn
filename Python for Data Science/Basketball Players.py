import numpy as np

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
sd = np.std(players)
mean = np.mean(players)
answer = [x for x in players if mean-sd < x < mean+sd]
print(len(answer))