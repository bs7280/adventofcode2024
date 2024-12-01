import pandas as pd
import numpy as np

df = pd.read_csv("input.txt", sep="   ", header=None)
df.columns = ["A", "B"]

val = np.sum(np.abs(df["A"].sort_values().values - df["B"].sort_values().values))

print("Part 1:")
print(val)

similarity_score = 0
for i in df["A"].values:
    if i in df["B"].values:
        matches = i == df["B"].values

        similarity_score += sum(matches) * i

print("Similarity score:")
print(similarity_score)
