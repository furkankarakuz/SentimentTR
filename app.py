from model_process import load_model, tokenizasyon
from log_process import add_log
import streamlit as st

st.set_page_config("SentimentTR", layout="wide")

st.header("SentimentTR")
st.divider()

model, tokenizer = load_model()

col1, col2, col3 = st.columns([2, 1, 2])
text = None

with col1:
    text = st.text_area("Write Your Comment", height=300)
    button = st.button("Predict!")

with col2:
    st.empty()

with col3:
    if button and text:
        result = tokenizasyon(text, model, tokenizer)
        if "error" in result:
            error = result["error"]
            st.error(f"Please write a text containing Turkish words. Check your text. {error}")
            add_log(text, result, "error")
        else:
            predict_label, predict_score = result["predict"][0], result["predict"][1]
            st.subheader(f"Segment : {predict_label}")
            st.subheader(f"Predict Score : {predict_score}")
            st.image(f"images/{predict_label}.gif", use_container_width=300)
            add_log(text, predict_label)
