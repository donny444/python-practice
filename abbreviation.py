#Dictionary Data Type
abbreviation = {
    "AFK": "Away From Keyboard",
    "BRB": "Be Right Back",
    "BTW": "By The Way",
    "FYI": "For Your Information",
    "IKR": "I Know, Right?",
    "LOL": "Laughing  Out Loud",
    "NSFW": "Not Safe For Work",
    "WFH": "Work From Home",
    "WYATB": "Wish You All The Best"
}

#Key Not Found
print(abbreviation.get("WY", '"IDK" means "I Don\'t Know"\n'))

#Key Found
print(abbreviation.get("NSFW", '"IDK" means "I Don\'t Know"\n'))