import requests
import logging

def extract_data():
    logging.info("Extracting data from API...")
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    response.raise_for_status()
    logging.info("Data extracted successfully.")
    return response.json()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data = extract_data()
