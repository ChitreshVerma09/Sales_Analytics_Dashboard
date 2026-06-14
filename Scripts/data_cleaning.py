import os
import pandas as pd
import numpy as np

# Setting up relative file paths for data access
RAW_DATA_PATH = os.path.join('Data', 'superstore_raw.csv')
CLEANED_DATA_PATH = os.path.join('Data', 'superstore_cleaned.csv')

def clean_sales_data():
    print("Loading dataset...")
    if not os.path.exists(RAW_DATA_PATH):
        print(f" Error: {RAW_DATA_PATH} not found! Please check the file name.")
        return

    # Load dataset handling specific encoding
    df = pd.read_csv(RAW_DATA_PATH, encoding='latin1')
    print(f" Original Data Shape: {df.shape}")
    
    # 1. Remove duplicate records
    df.drop_duplicates(inplace=True)

    # 2. Handle missing values in Postal Code
    if 'Postal Code' in df.columns:
        df['Postal Code'] = df['Postal Code'].fillna(0).astype(int)
    
    # 3. Standardize Date formats (Convert String to Datetime)
    print(" Converting date formats...")
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
    
    # Drop rows where dates couldn't be parsed properly
    df.dropna(subset=['Order Date', 'Ship Date'], inplace=True)

    # 4. Feature Engineering: Extracting time parts for Power BI
    df['Order Year'] = df['Order Date'].dt.year
    df['Order Month No'] = df['Order Date'].dt.month
    df['Order Month Name'] = df['Order Date'].dt.strftime('%B')
    df['Order Year-Month'] = df['Order Date'].dt.strftime('%Y-%m')

    # 5. Rounding financial metrics (Handling dynamically if Profit exists or not)
    if 'Sales' in df.columns:
        df['Sales'] = df['Sales'].round(2)
        
    if 'Profit' in df.columns:
        df['Profit'] = df['Profit'].round(2)
        df['Cost'] = (df['Sales'] - df['Profit']).round(2)
    else:
        print(" Note: 'Profit' column not found in this dataset. Proceeding with Sales metrics only.")

    # Export the processed dataset to the destination folder
    df.to_csv(CLEANED_DATA_PATH, index=False)
    print(f" Cleaned data successfully saved to: {CLEANED_DATA_PATH}")
    print(f" New Data Shape: {df.shape}")

if __name__ == "__main__":
    clean_sales_data()