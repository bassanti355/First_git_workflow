# test_etl.py

import requests
import pandas as pd
from transform import transform_data

def test_api_response_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200

def test_transform_columns():
    sample_data = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ]
    df = pd.DataFrame(sample_data)
    transformed_df = transform_data(df)
    
    # Example checks
    assert "name" in transformed_df.columns
    assert len(transformed_df) == 2
