"""
It may be better load all the data but also to take the averages
of each month for each state/county.

Maybe a function that has parameters for state, county, and month number.
County default is blank unless something is enters. Also may not even consider counties at all in the project.
I'll just make it for only state and month for now.

Definitely need a euclidean distance helper function.


"""

import pandas as pd

df = pd.read_csv("data/2020_US_Covid_Mobility.csv")

mobility_cols = [
    "retail_and_recreation",
    "grocery_and_pharmacy",
    "parks",
    "transit_stations",
    "workplaces",
    "residential"
]

# Getting averages of each state for each month of 2020

df_states = df[df["county"].isna()]
df_states["month"] = df_states["date"].str.split("/").str[0].astype(int)
state_month_avg = df_states.groupby(["state", "month"])[mobility_cols].mean()

state_points = []

for (state, month), row in state_month_avg.iterrows():
    vector = row.tolist()
    state_points.append((state, month, vector))

print(state_points)

# Getting averages of each county for each month of 2020 ok lets ignore the counties for now

# df_counties = df[df["county"].isna() == False]
# df_counties["month"] = df_counties["date"].str.split("/").str[0].astype(int)
# county_month_avg = df_counties.groupby(["state", "county", "month"])[mobility_cols].mean()
# county_month_avg = county_month_avg.groupby(level=["state", "month"]).transform(
#     lambda x: x.fillna(x.mean())
# )

# county_points = []

# for (state, county, month), row in county_month_avg.iterrows():
#     vector = row.tolist()
#     county_points.append((state, county, month, vector))
# print(county_points)