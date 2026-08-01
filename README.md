# 🛒 Smart Retail AI Assistant

An AI-powered retail assistant built using **FastAPI**, **Streamlit**, **Computer Vision**, **Natural Language Processing (NLP)**, and **Large Language Models (LLMs)**. The application provides three intelligent features: **Face Detection**, **Customer Review Sentiment Analysis**, and an **AI Shopping Assistant**.

---

## 🌐 Live Demo

**🖥️ Frontend (Streamlit):**  
https://smart-retail-ai-frontend.onrender.com

**⚡ Backend API:**  
https://smart-retail-ai-tmm5.onrender.com

**📄 Swagger API Documentation:**  
https://smart-retail-ai-tmm5.onrender.com/docs

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

<img width="1917" height="865" alt="Screenshot 2026-07-31 123739" src="https://github.com/user-attachments/assets/ea1da3c7-efa8-40ba-ba5f-3d92c630241b" />


---

## 📷 Face Detection

<img width="1915" height="858" alt="Screenshot 2026-07-31 123814" src="https://github.com/user-attachments/assets/a2e903a9-9c37-414e-abf4-82dbef71ae56" />
<img width="1915" height="861" alt="Screenshot 2026-07-31 123839" src="https://github.com/user-attachments/assets/95a0bdd1-e9a2-4868-b35e-771d9e8d8e16" />



---

## 😊 Sentiment Analysis

<img width="1913" height="867" alt="Screenshot 2026-07-31 123853" src="https://github.com/user-attachments/assets/7931ea44-0752-4ac2-b7bb-b6e175d7361e" />
<img width="1907" height="865" alt="Screenshot 2026-07-31 124032" src="https://github.com/user-attachments/assets/38fd5113-92d6-49a1-a037-18785221480a" />



---

## 🤖 AI Shopping Assistant

<img width="1913" height="866" alt="Screenshot 2026-07-31 124046" src="https://github.com/user-attachments/assets/72b1544f-6c70-46d8-b771-2512f9fb1a33" />
<img width="1917" height="867" alt="Screenshot 2026-07-31 124243" src="https://github.com/user-attachments/assets/75178a56-3e1d-4ba9-9be0-b398c9090f33" />



---
# API Documentation 

Swagger UI

<img width="1917" height="871" alt="Screenshot 2026-08-01 105825" src="https://github.com/user-attachments/assets/1e20c337-7205-429e-8cf9-2fd2b6371a37" />

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
