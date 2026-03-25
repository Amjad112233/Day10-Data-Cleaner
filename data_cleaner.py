import pandas as pd
import os
data = pd.read_csv("../Month 1/Day 10/dirty_data.csv")

print("\nOriginal Data:")
print(data)

# remove rows with missing values
clean_data = data.dropna()

# remove duplicates
clean_data = clean_data.drop_duplicates()

print("\nCleaned Data")
print(clean_data)

clean_data.to_csv("clean_data.csv", index=False)