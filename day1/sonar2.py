import pandas as pd
import numpy as np

s = pd.read_csv('day1/input.txt', sep=" ", header=None)
print(s)
df = s.rolling(3).sum()
df[1] = df[0].shift(-1)
print(df)
print(len(df[df[1] > df[0]]))