import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data01.csv")
targetrows = []
print("Median House Value:", df["median_house_value"].median())

for i in df.index:
    if df.loc[i, "total_rooms"] < 500:
        df.loc[i, "total_rooms"] = df["total_rooms"].median()

    if df.loc[i, "housing_median_age"] < 25:
        targetrows.append(df.loc[i])

print("Total Rooms Min:", df["total_rooms"].min())
hma_df = pd.DataFrame(targetrows)

print(hma_df)

plt.scatter(x=df["median_house_value"], y=df["median_income"])
plt.xlabel("Median House Value")
plt.ylabel("Median Income")
plt.title("Median House Value Vs. Median Income")
plt.show()