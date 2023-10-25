import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("data/CSV/air_quality_no2.csv", index_col=0, parse_dates=True)

air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster"
    }
)
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)

print(air_quality_renamed.head())
#Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html