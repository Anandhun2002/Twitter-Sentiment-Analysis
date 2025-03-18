import streamlit as st
from textblob import TextBlob

# Function to set a background image
def set_background():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://cdn.wallpapersafari.com/88/75/cLUQqJ.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0); /* Transparent header */
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0.8); /* Slight transparency for content */
        color: black;
        border-radius: 10px;
        padding: 10px;
    }
    h1, h2 {
        text-align: center;
        color: white; /* Set text color to white */
    }
    .stButton > button {
        background-color: blue;
        color: white;
        border-radius: 5px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #004aad;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Call the background function
set_background()

# App header
# App header with white font color
st.markdown("<h1 style='color: white;'>TWITTER</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: white;'>Sentiment Analysis</h2>", unsafe_allow_html=True)

# User input
user_input = st.text_input("Enter your text here:", placeholder="Type something about Twitter...")

# Analyze button
if st.button("Analyse"):
    if user_input.strip():
        # Sentiment analysis using TextBlob
        analysis = TextBlob(user_input)
        sentiment_score = analysis.sentiment.polarity

        # Determine sentiment and emoji
        if sentiment_score > 0:
            sentiment = "Positive 😊"
        elif sentiment_score < 0:
            sentiment = "Negative 😡"
        else:
            sentiment = "Neutral 😐"
        
        # Display result
        st.subheader("Sentiment Result")
        st.write(f"The sentiment of the entered text is: **{sentiment}**")
    else:
        st.warning("Please enter some text to analyze.")





