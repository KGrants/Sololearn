import numpy as np
import pandas as pd

lst = [float(x) if x != 'nan' else np.NaN for x in input().split()]
lst_df = pd.Series(lst)
a = lst_df.fillna(lst_df.mean().round(1))
print(a)