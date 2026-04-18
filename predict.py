import joblib

def predict_language():
    # Load the saved pipeline
    try:
        model = joblib.load('models/model_pipeline.pkl')
    except FileNotFoundError:
        print("Error: Model file not found. Run train.py first.")
        return

    user_input = input("Enter text to detect language: ")
    
    if user_input.strip():
        # With the pipeline, we just pass the raw text list
        prediction = model.predict([user_input])
        print(f"Detected Language: {prediction[0]}")
    else:
        print("Please enter valid text.")

if __name__ == "__main__":
    predict_language()