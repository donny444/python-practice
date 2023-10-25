import pandas as pd

superheroes = pd.read_csv("data/CSV/superheroes.csv")
israelPalestine = pd.read_csv("data/CSV/Israel-Palestine.csv")
fc24 = pd.read_csv("data/CSV/fc24-players/all_players.csv")

print(superheroes)
print("\n")
print(superheroes.dtypes)
print("\n")
print(israelPalestine)
print("\n")
print(israelPalestine.head())
print("\n")
print(israelPalestine.tail())
print("\n")
print(fc24.info())

#superheroes.to_json("superheroes.json")

#Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html