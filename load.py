import os
import logging
from transform import transform_data
from extract import extract_data

def load_data(df, filename="data/output.csv"):
    # ✅ Ensure the directory exists before writing
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    logging.info(f"Saving data to {filename}...")
    df.to_csv(filename, index=False)
    logging.info("Data saved successfully.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    logging.info("Extracting data from API...")
    raw_data = extract_data()
    logging.info("Data extracted successfully.")
    
    logging.info("Transforming data...")
    transformed = transform_data(raw_data)
    logging.info("Transformation complete.")
    
    load_data(transformed)
