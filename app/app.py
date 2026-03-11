import streamlit as st
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from predictor import predict_sentiment

st.title("Real-Time Sentiment Analysis")

user_input = st.text_area("Enter Text")

if st.button("Analyze"):

    if user_input.strip() != "":
        result = predict_sentiment(user_input)

        if result == "positive":
            st.success("Positive Sentiment 😊")

        elif result == "negative":
            st.error("Negative Sentiment 😡")

        else:
            st.info("Neutral Sentiment 😐")

    else:
        st.warning("Please enter text")