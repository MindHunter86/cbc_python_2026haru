import pandas as pd

df = pd.read_csv('200.csv',encoding='shift_jis')

print(len(df))
print(df.columns.values)