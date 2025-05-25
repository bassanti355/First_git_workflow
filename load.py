import os
import logging
from transform import transform_data
from extract import extract_data

def load_data(df, filename="data/output.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # ✅ Make sure 'data/' exists
    logging.info(f"Saving data to {filename}...")
    df.to_csv(filename, index=False)
    logging.info("Data saved successfully.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    raw_data = extract_data()
    transformed = transform_data(raw_data)
    load_data(transformed)
