import pandas as pd
data={
    "name":["varshitha","geethika","sirisha"],
    "marks":[90,89,87],
    "city":["nandigama","vijaywada","kongancherla"],
    }
df=pd.DataFrame(data)
print(df["name"])
print(df[["name","city","marks"]])
print(df.iloc[0])
print(df.iloc[0:3])
print(df.loc[0])
print(df.loc[1:2])
print(df["marks"]>80)
print[(df["marks"]>80 & df["city"]=="Mumbai")]
df.head(2)
df.tail(2)