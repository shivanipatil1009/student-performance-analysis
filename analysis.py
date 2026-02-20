# Student Performance Analysis using Python

import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Study_Hours":[2,3,4,5,6,7,8],
    "Marks":[40,45,50,60,65,70,80]
}

df = pd.DataFrame(data)

# Basic analysis
print(df.describe())

# Plot
plt.scatter(df["Study_Hours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
