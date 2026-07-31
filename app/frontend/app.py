import streamlit as st
import requests

st.set_page_config(
    page_title="Smart Retail AI",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Smart Retail AI Assistant")

st.sidebar.title("Features")

option = st.sidebar.selectbox(
    "Choose Feature",
    [
        "📷 Face Detection",
        "😊 Review Sentiment",
        "🤖 AI Shopping Assistant"
    ]
)

# ---------------------------------------------------
# FACE DETECTION
# ---------------------------------------------------
if option == "📷 Face Detection":

    st.header("📷 Face Detection")

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        st.image(
    uploaded_file,
    caption="Uploaded Image",
    width="stretch"
)

        if st.button("Detect Face"):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    uploaded_file.type
                )
            }

            response = requests.post(
                "https://smart-retail-ai-tmm5.onrender.com/vision/detect-face",
                files=files
            )

            if response.status_code == 200:

                result = response.json()

                st.success("✅ Detection Successful")

                st.metric("Faces Detected", result["faces_detected"])

                if result["faces_detected"] > 0:
                    st.write("### Face Coordinates")

                    for idx, face in enumerate(result["faces"], start=1):
                        st.write(f"**Face {idx}**")
                        st.write(f"- X: {face['x']}")
                        st.write(f"- Y: {face['y']}")
                        st.write(f"- Width: {face['width']}")
                        st.write(f"- Height: {face['height']}")

            else:
                st.error("API Error")
                st.write(response.text)

# ---------------------------------------------------
# SENTIMENT ANALYSIS
# ---------------------------------------------------
elif option == "😊 Review Sentiment":

    st.header("😊 Review Sentiment Analysis")

    review = st.text_area(
        "Enter Customer Review",
        placeholder="Example: This product is amazing!"
    )

    if st.button("Analyze Sentiment"):

        if review.strip() == "":
            st.warning("Please enter a review.")

        else:

            response = requests.post(
                "https://smart-retail-ai-tmm5.onrender.com/nlp/sentiment",
                json={"text": review}
            )

            if response.status_code == 200:

                result = response.json()

                st.success("✅ Analysis Complete")

                st.write("### Results")

                st.write(f"**Review:** {result['review']}")

                if result["sentiment"] == "POSITIVE":
                    st.success("😊 Positive Review")
                else:
                    st.error("😞 Negative Review")

                st.metric(
                    "Confidence",
                    f"{result['confidence']*100:.2f}%"
                )

            else:

                st.error("API Error")
                st.write(response.text)

# ---------------------------------------------------
# CHATBOT (placeholder for now)
# ---------------------------------------------------
elif option == "🤖 AI Shopping Assistant":

    st.header("🤖 AI Shopping Assistant")

    question = st.text_area(
        "Ask your shopping question",
        placeholder="Example: Suggest a good gaming laptop under ₹70,000"
    )

    if st.button("Ask AI"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            with st.spinner("Thinking..."):

                response = requests.post(
                    "https://smart-retail-ai-tmm5.onrender.com/chatbot/chat",
                    json={
                        "question": question
                    }
                )

            if response.status_code == 200:

                result = response.json()

                st.success("✅ AI Response")
                st.write("### 🙋 Your Question")
                st.info(result["question"])

                st.write("### 🤖 AI Shopping Assistant")
                st.success(result["answer"])

            else:

                st.error("API Error")
                st.write(response.text)
                