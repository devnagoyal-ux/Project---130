import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")
print(df.shape)

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df.to_csv('new.csv')