# Three commits of ETL process

# Commit 1: Extract and Load

import pandas as pd

# Load raw data
df = pd.read_csv("raw_data.csv")

#################################################################################

# Commit 2: Transform

# Normalize column names
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# Handle missing values
df.fillna({"name": "Unknown", "age": df["age"].median(), "purchase_amount": 0}, inplace=True)

# Convert purchase date to uniform format
df["purchasedate"] = pd.to_datetime(df["purchasedate"], errors="coerce")

#################################################################################

# Commit 3: Load

# Save the final processed data into a local file
df.to_csv("final_data.csv", index=False)