import pandas as pd

children = pd.DataFrame(
    {
        "Nickname": [
            "Cake",
            "Aom",
            "Bam"
        ],
        "Age": [19, 18, 19],
        "College": ["MU", "MU", "SU"],
    }
)
print(children["Age"].describe())

muscle = pd.Series(["Bicep", "Tricep", "Quadricep"], name="Muscle")
#print(muscle)

#Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#min-tut-01-tableoriented