import pandas as pd

books = pd.DataFrame(
    {
        "Title": [
            "Overengineering",
            "Reverse Engineering",
            "Can't Shower"
        ],
        "Pages": [300, 500, 50],
        "HaveEbook": [False, False, True]
    }
)
#print()

#Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html