# ai_module/predict.py
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open('ai_module/models/disease_model.pkl', 'rb'))

# Example function
def predict_disease(symptoms_list):
    # Convert symptoms to dataframe or features
    input_df = pd.DataFrame([symptoms_list])
    predicted_disease = model.predict(input_df)[0]
    # Map disease to recommended medicines
    disease_medicine_map = {
        "Flu": ["Paracetamol", "Cough Syrup"],
        "Diabetes": ["Metformin"],
        # Add more
    }
    return predicted_disease, disease_medicine_map.get(predicted_disease, [])
