import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def clean_and_split_data(df):
    """
    Yeh function data ko ML model ke liye ready karta hai.
    """
    print("⏳ Data Preprocessing Start kar rahe hain...")
    
    try:
        # 1. Feature Engineering: Date se 'month' (mahina) nikalna [cite: 14]
        # Kyunki kis mahine me kitni garmi hai, isse energy ka pata chalta hai [cite: 10]
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.month
        
        # 2. X (Input/Features) aur y (Output/Target) ko alag karna
        # 'date' drop kar rahe hain kyunki ML sirf numbers samajhta hai
        X = df.drop(columns=['date', 'energy_consumption'])
        y = df['energy_consumption']
        
        # 3. Train Test Split (80% Padhai, 20% Exam)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # 4. Feature Scaling (Data ko chota karna taaki model fast seekhe)
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        print(f"✅ Preprocessing successful! Training data rows: {X_train_scaled.shape[0]}, Testing data rows: {X_test_scaled.shape[0]}")
        return X_train_scaled, X_test_scaled, y_train, y_test, scaler
        
    except Exception as e:
        print(f"❌ Error aagaya preprocessing me: {e}")
        return None, None, None, None, None

# Testing ke liye (Yahan hum dono files ko jodd rahe hain!)
if __name__ == "__main__":
    # Dhyan do: Hum apni pichli file se data load karne wala function yahan import kar rahe hain!
    from data_ingestion import load_data 
    
    DATA_PATH = "../data/energy_data.csv"
    
    # Pehle data load karo
    df = load_data(DATA_PATH)
    
    # Phir usko preprocess karo
    if df is not None:
        X_train, X_test, y_train, y_test, scaler = clean_and_split_data(df)