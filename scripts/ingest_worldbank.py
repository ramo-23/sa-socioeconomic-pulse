import requests
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Configuration
PROJECT_ID = 'sa-socioeconomic-pulse' 
DATASET_ID = 'bronze'
TABLE_ID = 'raw_worldbank_data'
KEY_PATH = r'C:\Users\ramse\.gcp\sa-socioeconomic-key.json'

INDICATORS = {
    "SL.UEM.TOTL.ZS": "unemployment_rate",
    "NY.GDP.MKTP.CD": "gdp_usd",
    "FP.CPI.TOTL.ZG": "inflation_rate"
}

def fetch_worldbank_data():
    all_data = []
    base_url = "https://api.worldbank.org/v2/country/ZAF;BRA;NGA/indicator/{}?format=json&per_page=1000"
    
    for code, name in INDICATORS.items():
        response = requests.get(base_url.format(code)).json()
        if len(response) > 1:
            for entry in response[1]:
                all_data.append({
                    "country": entry["country"]["value"],
                    "year": int(entry["date"]),
                    "indicator_name": name,
                    "value": entry["value"]
                })
    return pd.DataFrame(all_data)

# Execution
df = fetch_worldbank_data()
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
client = bigquery.Client(credentials=credentials, project=PROJECT_ID)

job = client.load_table_from_dataframe(df, f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}")
job.result()
print(f"Successfully loaded {len(df)} rows into BigQuery.")