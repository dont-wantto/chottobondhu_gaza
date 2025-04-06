import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load the dataset (you'll create this CSV file in the next step)
def load_data():
    data = pd.read_csv('chottobondhu_gaza/sample_data.csv')  # Make sure the path is correct
    return data

# Prepare the dataset for training
def prepare_data(data):
    X = data['text']  # Features (text)
    y = data['label']  # Labels (trauma or no_trauma)
    return X, y

# Train the model
def train_model(X_train, y_train):
    vectorizer = CountVectorizer()  # Convert text to a bag of words
    X_train = vectorizer.fit_transform(X_train)  # Vectorize the text data
    model = MultinomialNB()  # A simple machine learning model
    model.fit(X_train, y_train)  # Train the model
    return model, vectorizer

# Predict whether the text indicates trauma or not
def detect_trauma(text, model, vectorizer):
    text_vectorized = vectorizer.transform([text])  # Vectorize the input text
    prediction = model.predict(text_vectorized)  # Make prediction
    return "⚠️ Possible trauma detected" if prediction == 'trauma' else "No critical signs"

# Main function to load, prepare data, and train the model
def main():
    data = load_data()  # Load data from CSV
    X, y = prepare_data(data)  # Prepare features and labels

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model, vectorizer = train_model(X_train, y_train)  # Train the model

    # Test the model on the test set
    X_test_vectorized = vectorizer.transform(X_test)  # Vectorize the test data
    predictions = model.predict(X_test_vectorized)  # Make predictions
    print(f"Model accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")

    return model, vectorizer

# Run the main function to train the model
if __name__ == "__main__":
    model, vectorizer = main()

    # Now let's use the model to detect trauma in a sample text
    sample_text = "I feel afraid and alone since the bomb exploded."
    print(detect_trauma(sample_text, model, vectorizer))  # This will print the detection result
