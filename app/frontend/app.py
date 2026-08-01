import streamlit as st
import requests

# -----------------------------
# Configuration
# -----------------------------
st.set_page_config(
    page_title="Smart Retail AI",
    page_icon="🛒",
    layout="wide"
)

API_URL = "https://smart-retail-ai-tmm5.onrender.com"

# -----------------------------
# Title
# -----------------------------
st.title("🛒 Smart Retail AI Assistant")
st.markdown("An AI-powered Retail Assistant using Computer Vision, NLP and Generative AI.")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Features")

option = st.sidebar.selectbox(
    "Choose Feature",
    [
        "📷 Face Detection",
        "😊 Review Sentiment",
        "🤖 AI Shopping Assistant"
    ]
)

# =====================================================
# FACE DETECTION
# =====================================================

if option == "📷 Face Detection":

    st.header("📷 Face Detection")

    uploaded_file = st.file_uploader(
        "Upload an Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        st.image(
            uploaded_file,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button("Detect Face"):

            with st.spinner("Detecting faces..."):

                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file,
                        uploaded_file.type
                    )
                }

                try:

                    response = requests.post(
                        f"{API_URL}/vision/detect-face",
                        files=files,
                        timeout=60
                    )

                    if response.status_code == 200:

                        result = response.json()

                        st.success("✅ Face Detection Successful")

                        st.metric(
                            "Faces Detected",
                            result["faces_detected"]
                        )

                        if result["faces_detected"] > 0:

                            st.subheader("Detected Faces")

                            for i, face in enumerate(result["faces"], start=1):

                                st.write(f"### Face {i}")
                                st.write(f"X : {face['x']}")
                                st.write(f"Y : {face['y']}")
                                st.write(f"Width : {face['width']}")
                                st.write(f"Height : {face['height']}")

                        else:
                            st.info("No face detected in the image.")

                    else:

                        st.error(f"API Error ({response.status_code})")
                        st.code(response.text)

                except Exception as e:
                    st.error(str(e))


# =====================================================
# SENTIMENT ANALYSIS
# =====================================================

elif option == "😊 Review Sentiment":

    st.header("😊 Customer Review Sentiment Analysis")

    review = st.text_area(
        "Enter Customer Review",
        placeholder="Example: This product is amazing!"
    )

    if st.button("Analyze Sentiment"):

        if review.strip() == "":
            st.warning("Please enter a review.")

        else:

            with st.spinner("Analyzing Review..."):

                try:

                    response = requests.post(
                        f"{API_URL}/nlp/sentiment",
                        json={
                            "text": review
                        },
                        timeout=60
                    )

                    if response.status_code == 200:

                        result = response.json()

                        st.success("✅ Analysis Complete")

                        st.subheader("Review")
                        st.write(result["review"])

                        st.subheader("Sentiment")

                        if result["sentiment"] == "POSITIVE":
                            st.success("😊 Positive")
                        else:
                            st.error("😞 Negative")

                        st.metric(
                            "Confidence",
                            f"{result['confidence']*100:.2f}%"
                        )

                    else:

                        st.error(f"API Error ({response.status_code})")
                        st.code(response.text)

                except Exception as e:
                    st.error(str(e))


# =====================================================
# AI SHOPPING ASSISTANT
# =====================================================

elif option == "🤖 AI Shopping Assistant":

    st.header("🤖 AI Shopping Assistant")

    question = st.text_area(
        "Ask anything about products",
        placeholder="Example: Suggest a gaming laptop under ₹70,000"
    )

    if st.button("Ask AI"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            with st.spinner("Thinking..."):

                try:

                    response = requests.post(
                        f"{API_URL}/chatbot/chat",
                        json={
                            "question": question
                        },
                        timeout=60
                    )

                    if response.status_code == 200:

                        result = response.json()

                        st.success("✅ Response Generated")

                        st.subheader("🙋 Your Question")
                        st.info(question)

                        st.subheader("🤖 AI Assistant")

                        st.markdown(result["answer"])

                    else:

                        st.error(f"API Error ({response.status_code})")
                        st.code(response.text)

                except Exception as e:
                    st.error(str(e))