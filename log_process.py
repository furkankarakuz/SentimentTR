from firebase_admin import credentials, firestore
from datetime import datetime
# from config import service_key
from pytz import timezone
import streamlit as st
import firebase_admin
import uuid
import json


def firebase_initialize():
    if "firebase_app" not in st.session_state:
        cred = credentials.Certificate(json.loads(st.secrets["firebase"]["service_key"]))
        st.session_state.firebase_app = firebase_admin.initialize_app(cred)


def add_log(text, label, type="data"):
    if "id_user" not in st.session_state:
        st.session_state.setdefault("id_user", str(uuid.uuid4()))

    db = firestore.client()
    turkey_timezone = timezone("Europe/Istanbul")
    log_time = datetime.now(turkey_timezone).strftime("%Y-%m-%d %H:%M:%S")

    if type == "data":
        db.collection("data_logs").add({
            "id_user": st.session_state["id_user"],
            "action_time": log_time,
            "text": text,
            "label": label
        })

    elif type == "error":
        db.collection("error_logs").add({
            "id_user": st.session_state["id_user"],
            "action_time": log_time,
            "text": text,
        })
