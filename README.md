# 🛒 Smart Retail AI Assistant

An AI-powered retail assistant built using **FastAPI**, **Streamlit**, **Computer Vision**, **Natural Language Processing (NLP)**, and **Large Language Models (LLMs)**. The application provides three intelligent features: **Face Detection**, **Customer Review Sentiment Analysis**, and an **AI Shopping Assistant**.

---

## 🚀 Features

### 📷 Face Detection
- Upload an image
- Detect human faces using OpenCV
- Display the number of faces detected
- Return face coordinates

### 😊 Review Sentiment Analysis
- Analyze customer reviews
- Predict Positive or Negative sentiment
- Display confidence score
- Powered by a Transformer/BERT-based NLP model

### 🤖 AI Shopping Assistant
- Ask shopping-related questions
- Receive AI-generated product recommendations
- Natural language interaction using an LLM

---

# 🏗️ System Architecture

```
                Streamlit Frontend
                        │
                        ▼
                 FastAPI Backend
        ┌──────────┼──────────┐
        ▼          ▼          ▼
 Face Detection  NLP Model  AI Chatbot
      │             │            │
   OpenCV      Transformers     LLM
```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.12 |
| Backend | FastAPI |
| Frontend | Streamlit |
| Computer Vision | OpenCV |
| NLP | Hugging Face Transformers |
| AI Chatbot | LLM API |
| API Server | Uvicorn |
| Data Validation | Pydantic |
| HTTP Requests | Requests |

---

# 📂 Project Structure

```
smart-retail-ai/
│
├── app/
│   ├── frontend/
│   │   └── app.py
│   ├── routers/
│   ├── services/
│   ├── models/
│   ├── utils/
│   └── main.py
│
├── data/
├── trained_models/
├── notebooks/
├── tests/
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-retail-ai.git
cd smart-retail-ai
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

to access Swagger UI.

---

# ▶️ Run Streamlit Frontend

```bash
streamlit run app/frontend/app.py
```

Open

```
http://localhost:8501
```

---

# 🌐 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Home |
| POST | `/vision/detect-face` | Detect faces in an uploaded image |
| POST | `/nlp/sentiment` | Analyze customer review sentiment |
| POST | `/chatbot/chat` | AI shopping assistant |

---

# 📸 Screenshots

## 🏠 Home

_Add screenshot here_

---

## 📷 Face Detection

_Add screenshot here_

---

## 😊 Sentiment Analysis

_Add screenshot here_

---

## 🤖 AI Shopping Assistant

_Add screenshot here_

---

# 📈 Future Enhancements

- Draw bounding boxes on detected faces
- User authentication
- Product recommendation engine
- Database integration
- Voice-based shopping assistant
- Real-time webcam face detection
- Conversation history
- Docker deployment
- Cloud deployment

---

# 🎯 Learning Outcomes

This project demonstrates:

- REST API development
- FastAPI backend development
- Streamlit frontend development
- Computer Vision using OpenCV
- NLP using Transformers
- LLM Integration
- API communication
- End-to-end AI application development

---

# 👩‍💻 Author

**Palak Shah**

Integrated M.Tech (Artificial Intelligence)

VIT Bhopal University

---

# 📄 License

This project is developed for educational and learning purposes.