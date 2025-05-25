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

#####################################################################################

# Commit 4: Data Validation
# Check for duplicates
duplicates = df.duplicated().sum()
if duplicates > 0:
    print(f"Warning: {duplicates} duplicate rows found.")
else:
    print("No duplicate rows found.")

# Check for missing values
missing_values = df.isnull().sum()
if missing_values.any():
    print("Warning: Missing values found in the following columns:")
    print(missing_values[missing_values > 0])
else:
    print("No missing values found.")
    