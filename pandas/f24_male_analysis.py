import pandas as pd
import matplotlib.pyplot as plt

players = pd.read_csv("data/CSV/fc24-players/male_players.csv")
#print(players.info())

for method_name in dir(players.plot()):
    if not method_name.startswith("_"):
        print(method_name)


#print(players.loc[players["Nation"] == "Brazil", ["Name", "Club"]]) #Print Brazil players name and club
#print(type(players.loc[players["Nation"] == "Brazil", ["Name", "Club"]])) #Check for pandas datatype: DataFrame

#print(players.loc[players["Position"] == "GK", ["Name"]]) #Print goalkeeper players name
#print(type(players["Position"])) #Check for pandas datatype: Series

#print(players.iloc[0:10, 1:7]) #Print top 10 players
#print(players.iloc[0:10, 1:7].shape) #Check for shape

