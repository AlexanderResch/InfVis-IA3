import pandas as pd

input_file = "openpowerlifting-dataset.csv"

output_file = "openpowerlifting_subset.csv"

print("Loading CSV...")

df = pd.read_csv(input_file, usecols=[
    "Sex",
    "Tested",
    "Country",
    "TotalKg",
    "Dots",
    "Date"
])

print("Rows loaded:", len(df))
print("Saving subset...")


df.to_csv(output_file, index=False)

print("Saved as:", output_file)