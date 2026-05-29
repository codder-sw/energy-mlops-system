import streamlit as st
import requests

# Page ki setting
st.set_page_config(page_title="Energy Predictor", page_icon="⚡")

st.title("⚡ AI Energy Consumption Predictor")
st.write("Welcome to the Frontend! Niche details daaliye aur AI se prediction lijiye.")

st.markdown("---")

# User se inputs lene ke liye dabbe (Widgets)
col1, col2 = st.columns(2)

with col1:
    temp = st.number_input("🌡️ Temperature (°C)", min_value=-10.0, max_value=60.0, value=35.5)
    humidity = st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)

with col2:
    is_weekend = st.selectbox("📅 Kya aaj chutti (Weekend) hai?", options=[0, 1], format_func=lambda x: "Haan (1)" if x==1 else "Nahi (0)")
    month = st.slider("📆 Mahina (Month)", min_value=1, max_value=12, value=6)

st.markdown("---")

# Predict Button
if st.button("🚀 Predict Energy", use_container_width=True):
    # API (Waiter) ko order de rahe hain
    api_url = "http://127.0.0.1:8000/predict"
    payload = {
        "temperature": temp,
        "humidity": humidity,
        "is_weekend": is_weekend,
        "month": month
    }
    
    try:
        # Request bhej rahe hain
        response = requests.post(api_url, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"🔮 **Predicted Energy Consumption: {result['predicted_energy']:.2f} Units**")
            st.balloons() # Thoda celebration!
        else:
            st.error("❌ API se theek response nahi aaya.")
            
    except Exception as e:
        st.error("❌ API connect nahi ho rahi. Dhyan rahe ki FastAPI (uvicorn) dusre terminal me chal raha ho!")