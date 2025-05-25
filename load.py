import logging
from transform import transform_data
from extract import extract_data
import pandas as pd

def load_data(df, filename="data/output.csv"):
    logging.info(f"Saving data to {filename}...")
    df.to_csv(filename, index=False)
    logging.info("Data saved successfully.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data = extract_data()
    df = transform_data(data)
    load_data(df)
