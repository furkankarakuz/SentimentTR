import tensorflow as tf
import streamlit as st
import pickle
from text_process import clean_text, error_check
from log_process import firebase_initialize
from tensorflow.keras.preprocessing.sequence import pad_sequences


int_to_label = {0: "Negative", 1: "Notr", 2: "Positive"}


@st.cache_resource
def load_model():
    firebase_initialize()
    model = tf.keras.models.load_model("model/SentimentTRModel.keras")
    with open("model/tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    return model, tokenizer


def tokenizasyon(text, model, tokenizer):
    cleaned_text = clean_text(text)
    error = error_check(cleaned_text)
    if error:
        return {"error": error}
    else:
        tokenized_text = tokenizer.texts_to_sequences([cleaned_text])
        padded_text = pad_sequences(tokenized_text, maxlen=30)

        predicted_probabilities = model.predict(padded_text, verbose=0)
        predicted_score = round(float(predicted_probabilities.max()), 2)
        predicted_class = predicted_probabilities.argmax(axis=-1)[0]

        predicted_label = int_to_label[predicted_class]
        return {"predict": [predicted_label, predicted_score]}
