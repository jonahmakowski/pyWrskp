import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Loading the pre-trained emotion detector model
model = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")

# Define the emotions
emotions = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

# Defining the function to predict emotions
def predict_emotion(frame):
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

    model.setInput(blob)
    detections = model.forward()

    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the confidence is greater than the minimum confidence
        if confidence > 0.5:
            # compute the (x, y)-coordinates of the bounding box for the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # extract the ROI of the face and then pass the ROI through our emotion detection model to
            # determine the probabilty of each emotion being expressed
            face = frame[startY:endY, startX:endX]

            # Create the recognizer and load the trained model
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read("emotion_recognizer.yml")

            # Perform classification to recognize the emotion
            preds = recognizer.predict(face)

            # Return the emotion label
            return emotions[preds[0]]
    return "Unknown"

# GUI code
root = tk.Tk()
root.title("Emotion Detector")

# Create a label to display the video feed
label = tk.Label(root)
label.pack()

# Start the video capture
cap = cv2.VideoCapture(0)


# Update the GUI with the video feed
def update_frame():
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)
    frame = ImageTk.PhotoImage(frame)
    label.config(image=frame)
    label.image = frame
    root.after(30, update_frame)


# Predict the emotion
def predict_emotion_on_click():
    ret, frame = cap.read()
    emotion = predict_emotion(frame)
    messagebox.showinfo("Emotion", "Your emotion is: " + emotion)


# Add a button to trigger emotion prediction
predict_button = tk.Button(root, text="Predict Emotion", command=predict_emotion_on_click)
#Pack the button and start the GUI
predict_button.pack()
root.after(30, update_frame)
root.mainloop()

#Release the video capture when the GUI is closed
cap.release()
