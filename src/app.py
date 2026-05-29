from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# 1. Waiter (API) banate hain
app = FastAPI(title="Energy Prediction API")

# 2. Chef (Model) aur uske tools (Scaler) ko rasoi me load karte hain
model = joblib.load('../models/xgboost_model.pkl')
scaler = joblib.load('../models/scaler.pkl')

# 3. Menu Card: Customer kya-kya input dega
class EnergyInput(BaseModel):
    temperature: float
    humidity: float
    is_weekend: int
    month: int

# 4. Entry Gate: Jab koi API par aayega toh usko yeh message dikhega
@app.get("/")
def read_root():
    return {"message": "Welcome to Energy Prediction API! 🚀"}

# 5. The Main Order Table: Yahan model prediction karega
@app.post("/predict")
def predict_energy(data: EnergyInput):
    # a. User ke data ko dictionary se dataframe me badlo
    input_data = pd.DataFrame([data.model_dump()])
    
    # b. Data ko Scale (chota) karo
    scaled_data = scaler.transform(input_data)
    
    # c. Model se result poocho
    prediction = model.predict(scaled_data)
    
    # d. Result ko wapas user ko bhej do
    return {"predicted_energy": float(prediction[0])}