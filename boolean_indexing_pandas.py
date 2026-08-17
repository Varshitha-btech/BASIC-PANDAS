import pandas as pd
s=pd.Series([20,11,17],index=['a','b','c'])
print(s[s>15])
print(s[s%2==0])
