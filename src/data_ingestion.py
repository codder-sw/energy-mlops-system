import pandas as pd
import os

def load_data(file_path):
    """
    Yeh function CSV file ko read karta hai aur Pandas DataFrame return karta hai.
    """
    try:
        # File ko read karne ki koshish kar rahe hain
        df = pd.read_csv(file_path)
        print(f"✅ Data successfully load ho gaya! Total rows: {len(df)}")
        return df
    except Exception as e:
        # Agar file nahi mili ya koi error aaya, toh yeh message aayega (Exception Handling)
        print(f"❌ Error aagaya data load karne me: {e}")
        return None

# Niche wala code sirf tab chalega jab hum is file ko directly run karenge
if __name__ == "__main__":
    # Hamari data file ka rasta (path)
    DATA_PATH = "../data/energy_data.csv"
    
    # Function ko call kar rahe hain
    df = load_data(DATA_PATH)
    
    if df is not None:
        print(df.head())