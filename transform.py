import pandas as pd
import logging

def transform_data(data):
    logging.info("Transforming data...")
    df = pd.DataFrame(data)
    agg = df.groupby("userId").agg(posts_count=("id", "count")).reset_index()
    logging.info("Transformation complete.")
    return agg

if __name__ == "__main__":
    import extract
    logging.basicConfig(level=logging.INFO)
    raw_data = extract.extract_data()
    df_transformed = transform_data(raw_data)
    print(df_transformed)
