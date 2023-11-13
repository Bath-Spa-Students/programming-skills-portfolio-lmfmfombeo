#Write a Python program that uses the elif statement to determine the season based on the
#month provided as input.
month = input("enter the month :")
if month in ("december","jan" ,"feb"):
    season = "winter"
elif month in ("march","april","may"):
    season = "spring"
elif month in ("june","july","august"):
    season = "summer"
elif month in ("september","october","november"):
    season = "autumn"
else:
    season = "not a vaild month"
print(f"the season for {month.capitalize()} is {season}.")               