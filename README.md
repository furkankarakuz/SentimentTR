# SentimentTR

SentimentTR is a Turkish sentiment analysis project that classifies texts into **positive, negative, or neutral** sentiments using an LSTM-based deep learning model. The project includes data preprocessing, model training, and deployment on **Streamlit**.

![positive](https://github.com/user-attachments/assets/dfc2b059-4405-424d-8d68-df3c2bde700a)
![negative](https://github.com/user-attachments/assets/94163a6c-10f2-4847-8eb1-c779d20908fe)
![neutral](https://github.com/user-attachments/assets/77488330-638a-4455-b1a5-9fba4f165e76)



## Dataset 📂

The dataset used in this project is sourced from [Hugging Face](https://huggingface.co/datasets/winvoker/turkish-sentiment-analysis-dataset). Before training, extensive preprocessing was applied to improve data quality.

### Preprocessing Steps ⚙️
- Removing numerical terms 🔢❌
- Eliminating punctuation marks ✂️
- Normalizing uppercase/lowercase letters 🔠
- Removing meaningless words 🗑️
- Automatically correcting misspelled words ✍️✅
- Filtering out non-Turkish words 🚫
- Applying stemming to words 🌱

## Model 🧠

A **Long Short-Term Memory (LSTM)** model was built using Keras. The model achieved **95% accuracy** on the validation dataset.

### Training Details 📊
- **Framework:** TensorFlow/Keras
- **Architecture:** LSTM
- **Accuracy:** 95% (Validation Set)
- **Loss Function:** Categorical Crossentropy
- **Optimizer:** Adam


### Additional Features 🛡️
- The application checks whether the entered words are in **Turkish** before processing.
- User comments and sentiment prediction results are stored in **Firebase** for further analysis.

## Demo 🚀

The trained model has been deployed using **Streamlit**. You can test it live here:  
🔗 [SentimentTR Web App](https://sentiment-tr.streamlit.app)

## Installation & Usage 🛠️

Clone the repository and install dependencies:

```bash
# Clone the repo
git clone https://github.com/furkankarakuz/SentimentTR.git
cd SentimentTR

# Install dependencies
pip install -r requirements.txt
```

Run the Streamlit app:
```bash
streamlit run app.py
```

## Contributing 🤝

Contributions are welcome! Feel free to submit issues or pull requests.

## License 📜

This project is licensed under the Apache-2.0 License.
