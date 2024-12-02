import pandas as pd

d = {}


df = pd.read_excel("input.xlsx")

ext = df.loc[0, "format"]

for i in range(len(df)):
    for key in d:
        if key in df.iloc[i,1]:
            df.loc[i, "Screenshot_Url"] = str(d[key] + df.iloc[i,1] + ext)

df = df.drop("format", axis = 1)
df["Screenshot_Url"].fillna("Keyword not found")

df.to_csv("outdf.csv")
