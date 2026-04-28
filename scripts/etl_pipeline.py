import pandas as pd

def extract_data(path):
    df = pd.read_csv(path, encoding='latin1')
    df.columns = df.columns.str.strip()
    return df

def clean_data(df):
    df = df.dropna(subset=['Customer ID'])
    df = df.drop_duplicates()
    df = df[df['Quantity'] > 0]
    df = df[df['Price'] > 0]
    
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Customer ID'] = df['Customer ID'].astype(int)
    
    df['TotalPrice'] = df['Quantity'] * df['Price']
    
    df['Year'] = df['InvoiceDate'].dt.year
    df['Month'] = df['InvoiceDate'].dt.month
    df['Day'] = df['InvoiceDate'].dt.day
    
    return df

def save_data(df, path):
    df.to_csv(path, index=False)

def run_pipeline():
    raw_path = "data/raw/online_retail_II.csv"
    processed_path = "data/processed/cleaned_data.csv"
    
    df = extract_data(raw_path)
    df = clean_data(df)
    save_data(df, processed_path)

if __name__ == "__main__":
    run_pipeline()