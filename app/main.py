import re
import streamlit as st
import streamlit.components.v1 as components
import requests
import json

st.write("# Classificador BNCC")

message_text = st.text_input("Enter a message for spam evaluation")


def predict(text):
    headers = {
        "accept": "application/json",
    }

    params = {
        "item": text,
    }

    print("Preprocessing...")
    response = requests.get(
        "https://bncc-classifier.herokuapp.com/api/v1/model/classify/item",
        params=params,
        headers=headers,
    )

    return response


if message_text != "":

    print("We have a text input...")
    prediction = st.button("Predict!")

    if prediction:
        response = predict(message_text)
        st.write(json.loads(response.text))
