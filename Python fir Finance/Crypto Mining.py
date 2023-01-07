import numpy_financial as npf

#price for 2018-2021
price = [-500000, 30000, 80000, 293000, 380000]

print(npf.irr(price))