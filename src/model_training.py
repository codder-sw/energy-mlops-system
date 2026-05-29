from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib # Model save karne ke liye
import os

def train_evaluate_model(X_train, y_train, X_test, y_test):
    """
    Yeh function XGBoost model ko train karta hai aur uska exam (test) leta hai.
    """
    print("🧠 Model Training Start ho rahi hai (XGBoost)...")
    
    try:
        model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
        model.fit(X_train, y_train)
        print("✅ Model Training Complete!")
        
        print("📝 Model ka test chal raha hai...")
        predictions = model.predict(X_test)
        
        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        
        print("\n📊 --- MODEL REPORT CARD ---")
        print(f"Mean Absolute Error (MAE): {mae:.2f}")
        print(f"Accuracy (R2 Score): {r2*100:.2f}%")
        
        return model
        
    except Exception as e:
        print(f"❌ Error aagaya training me: {e}")
        return None

def save_model_and_scaler(model, scaler):
    """
    Yeh function hamare trained model aur scaler dono ko 'models' folder me save karega.
    """
    # Agar models folder nahi hai toh bana do
    os.makedirs("../models", exist_ok=True)
    
    # Model ko save kar rahe hain
    joblib.dump(model, "../models/xgboost_model.pkl")
    # Scaler ko save kar rahe hain (Kyunki naye user data ko bhi chota karna padega)
    joblib.dump(scaler, "../models/scaler.pkl")
    
    print("💾 Model aur Scaler successfully 'models' folder me save ho gaye hain!")

if __name__ == "__main__":
    from data_ingestion import load_data
    from data_preprocessing import clean_and_split_data
    
    df = load_data("../data/energy_data.csv")
    
    if df is not None:
        X_train_scaled, X_test_scaled, y_train, y_test, scaler = clean_and_split_data(df)
        
        if X_train_scaled is not None:
            trained_model = train_evaluate_model(X_train_scaled, y_train, X_test_scaled, y_test)
            
            # Yahan humne naya Save wala function call kiya hai 👇
            if trained_model is not None:
                save_model_and_scaler(trained_model, scaler)