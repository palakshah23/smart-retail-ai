import cv2
import numpy as np
from PIL import Image
from fastapi import UploadFile
import io


# Load the pre-trained Haar Cascade model for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


async def detect_faces(file: UploadFile):
    # Read the uploaded image into memory
    contents = await file.read()

    # Convert image bytes into a PIL Image
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # Convert PIL Image into a NumPy array
    img = np.array(image)

    # Convert RGB image to BGR (OpenCV uses BGR format)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Convert image to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Store all detected face coordinates
    face_list = []

    for (x, y, w, h) in faces:
        face_list.append({
            "x": int(x),
            "y": int(y),
            "width": int(w),
            "height": int(h)
        })

    # Return the result as JSON
    return {
        "faces_detected": len(face_list),
        "faces": face_list
    }