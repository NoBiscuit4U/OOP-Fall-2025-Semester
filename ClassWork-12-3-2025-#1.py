import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

for i in df.index:
    if df.loc[i, "Duration"] > 120:
        df.loc[i, "Duration"] = 100

    if df.loc[i, "Calories"] < 500:
        df.loc[i, "Calories"] = 510

    df.loc[i, "Average Pulse"] = ((df.loc[i, "Pulse"] + df.loc[i, "Maxpulse"]) / 2)

df.dropna(inplace=True)
plt.scatter(x=df["Duration"], y=df["Calories"])
plt.xlabel("Duration")
plt.ylabel("Calories")
plt.title("Duration Vs. Calories")
plt.show()