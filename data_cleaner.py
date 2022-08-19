import csv
import pandas as pd

df = pd.read_csv("archive_dataset.csv")

del df["luminosity"]

# don't really know what else to delete
# luminosity also isn't actually in the data but I don't know what to do with it lol

print(list(df))

df.to_csv("main.csv")