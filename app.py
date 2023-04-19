import streamlit as st
import joblib
import numpy as np
from deep_translator import GoogleTranslator


# Load the pickled model
model = joblib.load("model.pickle")


# Create a function to get user inputs and make the prediction
def predict_yield(n, p, k, temp, moisture, ph, rainfall):
    # Create a NumPy array from the user input values
    input_data = np.array([n, p, k, temp, moisture, ph, rainfall]).reshape(1, -1)
    # Make the prediction using the loaded model
    predicted_yield = model.predict(input_data)[0]
    return predicted_yield


# Define the Streamlit app
def app():
    st.title("Agro Help Bot")

    # Define the input fields for the user
    n = st.number_input("Tuproq tarkibidagi nitrogen qiymati (N):", value=0, step=1)
    p = st.number_input("Tuproq tarkibidagi fosfor (P):", value=0, step=1)
    k = st.number_input("Tuproq tarkibidagi kaliy (K):", value=0, step=1)
    temp = st.number_input("O'rtacha harorat (°C):", value=0, step=1)
    moisture = st.number_input("Namlik ko'rsatgichlari:", value=0, step=1)
    ph = st.number_input("Tuproqning ishqoriyligi:", value=0, step=1)
    rainfall = st.number_input("Yomg'irgarchilik miqdori (mm):", value=0, step=1)

    # Create a button to trigger the prediction
    if st.button("Predict Yield"):
        # Call the predict_yield function to make the prediction
        predicted_yield = predict_yield(n, p, k, temp, moisture, ph, rainfall)
        # Display the predicted yield to the user
        st.success(f"Sizning ma'lumotlaringizdan kelib chiqib, biz sizga {GoogleTranslator(source='auto',target='uz').translate(predicted_yield )} ekishni maslahat beramiz 😊")


# Run the Streamlit app
if __name__ == "__main__":
    app()
