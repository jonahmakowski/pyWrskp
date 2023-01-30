import matplotlib.pyplot as plt

import io
import os
import datetime
import numpy as np

import PySimpleGUI as sg

import cv2

from feat import Detector

from pathlib import Path

def main():
   
    #downloads_path = str(Path.home()) + "/Downloads" + "/pyFeatData/" + datetime.datetime.now().isoformat()
    downloads_path = os.path.join(Path.home(), "pyWrskp/src/immran-like-code/data" + datetime.datetime.now().strftime('%Y%m%d %H%M%S'))
    os.mkdir(downloads_path)

    sg.theme("DarkBlue")

 

    # define the window layout New Window with Emotion Text Holer, Video and Exit Button

    layout = [[sg.Text("Emotion Detection Demo", size=(40, 1), justification="center", font="Helvetica 20")],[sg.Image(filename="", key="analysis1")],[sg.Image(filename="", key="analysis2")]]

 

    # create the window and show it without the plot

    window = sg.Window('Demo Application - Emotion Detection',layout, location=(800, 400))

 

    # Start Video Capture

    cap = cv2.VideoCapture(0,  cv2.CAP_DSHOW)

    cap.set(3,640) # set Width

    cap.set(4,480) # set Height

   

    #initialize the emotion detector

    #detector

 

    i = 10000

    # Capture frames and detect emotion. Exit if "Exit" button is clicked

    while True:

        event, values = window.read(timeout=20)

        if event == sg.WIN_CLOSED:

            return

        ret, frame = cap.read()

        imgPath = downloads_path +  "\\frameIn" +  str(i) + ".png"

        cv2.imwrite(imgPath, frame)

        detector = Detector(          
            face_model="retinaface",
            landmark_model="mobilefacenet",
            au_model="xgb",
            emotion_model="resmasknet",
            facepose_model="img2pose")

        multi_face_prediction = detector.detect_image(imgPath)

 

        detected_faces = detector.detect_faces(frame)

        detected_landmarks = detector.detect_landmarks(frame, detected_faces)
       
        detected_aus = detector.detect_aus(frame, detected_landmarks)

        detected_emotions = detector.detect_emotions(frame, detected_faces, detected_landmarks)

 

        figs = multi_face_prediction.plot_detections(add_titles=True, muscles=True)
       
        outputPath = downloads_path + "\\frameOut" + str(i) + ".png"

        plt.savefig(outputPath)

        with io.BytesIO() as buffer:  # use buffer memory

            plt.savefig(buffer, format='png')

            buffer.seek(0)

            pltImg = buffer.getvalue()

            window["analysis1"].update(pltImg)

 

        plt.close(figs[0])

        #window["analysis2"].update(figs[1])

        i=i+1

        # Another way to exit

        k = cv2.waitKey(30) & 0xff

        if k == 27: # press 'ESC' to quit

            break

    # Release camera

    cap.release()

    cv2.destroyAllWindows()

 

main()
