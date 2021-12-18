# -*- coding: utf-8 -*-
"""
Stroke Rehabilitation tags - Chula
Stroke video detection from Stroke Rehabilitation
@author: thienle
Date: September 30, 2021
"""

# Import libraries
import cv2
import streamlit as st
from PIL import Image
import mediapipe as mp

# Initial face drawing
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

def app():
    logo = Image.open('chula_logo.png')
    st.image(logo)

    st.title("""Stroke Rehabilitation - Hand Tracking""")
    st.write(" ------ ")
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">This apps allows stroke patient uses webcam to tracking their hands.</p>', unsafe_allow_html=True)
    # Define and call all the functions when the web-app starts.
    ###
    run = st.checkbox('Open Webcam')
    FRAME_WINDOW = st.image([])

    while run:
        cam = cv2.VideoCapture(0)
        with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
            while cam.isOpened():
                success, image = cam.read()
                if not success:
                    st.error("Ignoring empty camera frame.")
                    continue
                    # To improve performance, optionally mark the image as not writeable to
                    # pass by reference.
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image)

                # Draw the face mesh annotations on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Draw the hand annotations on the image.
                image.flags.writeable = True
                # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())

                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                FRAME_WINDOW.image(image)
        cam.release()