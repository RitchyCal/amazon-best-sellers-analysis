import pandas as pd


df = pd.read_csv('bestsellers.csv')
df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication", "User Rating": "Rating"}, inplace=True)

