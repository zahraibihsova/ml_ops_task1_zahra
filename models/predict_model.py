#this script is for loading model and using it to make predictions
def main():
    print("Load model and run predictions")

if __name__ == "__main__":
    main()
    
#code is not mine the one above is taken from github repository
#the one below is from online sources for model prediction
import pandas as pd
import joblib
import os

def load_and_predict(model_path, new_data):
    print(f"Loading model from '{model_path}'...")
    try:
        # Load the trained model from the specified path.
        loaded_model = joblib.load(model_path)
        print("Model loaded successfully.")

        # Make predictions on new data
        predictions = loaded_model.predict(new_data)
        return predictions

    except FileNotFoundError:
        print(f"Error: Model file '{model_path}' not found. Please train the model first.")
        return None

if __name__ == "__main__":
    # Ensure the model is trained by running 'python models/train_model.py' first.
    try:
        new_data = pd.DataFrame({'feature1': [4, 7], 'feature2': [7, 4]})
        model_path = os.path.join('models', 'trained_model.pkl')

        predictions = load_and_predict(model_path, new_data)

        if predictions is not None:
            print(f"Predictions for new data: {predictions}")
    except Exception as e:
        print(f"An error occurred: {e}")
    