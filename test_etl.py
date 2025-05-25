import requests
import pandas as pd
from transform import transform_data

def test_api_response():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200

def test_transform_columns():
    # Sample raw data similar to the API schema
    sample_data = [
        {"id": 1, "name": "John", "email": "john@example.com"},
        {"id": 2, "name": "Alice", "email": "alice@example.com"}
    ]
    df = pd.DataFrame(sample_data)
    transformed = transform_data(df)
    
    # Check required column exists after transformation
    assert 'name' in transformed.columns
    assert len(transformed) == 2
