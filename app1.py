import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open('sentiment_model.pkl', 'rb'))

# Create the app title
st.title('Sentiment Analysis App')

# Get user input
user_input = st.text_input("Enter some text:")

# Perform analysis and display results
if st.button('Analyze'):
    # Preprocess the input text (similar to your Colab notebook)
    # ...

    # Predict the sentiment
    sentiment = model.predict([user_input])[0]

    # Display the result
    st.write(f"Sentiment: {sentiment}")