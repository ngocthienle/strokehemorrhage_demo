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
mp_face_mesh = mp.solutions.face_mesh


def app():
    logo = Image.open('chula_logo.png')
    st.image(logo)

    st.title("""Stroke Rehabilitation - Face Tracking""")
    st.write(" ------ ")
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">This apps allows stroke patient uses webcam to tracking their face.</p>', unsafe_allow_html=True)
    # Define and call all the functions when the web-app starts.
    ###
    run = st.checkbox('Open Webcam')
    FRAME_WINDOW = st.image([])

    while run:
        cam = cv2.VideoCapture(0)
        with mp_face_mesh.FaceMesh(max_num_faces=1, min_detection_confidence=0.5,
                                   min_tracking_confidence=0.5) as face_mesh:
            while cam.isOpened():
                success, image = cam.read()
                if not success:
                    st.error("Ignoring empty camera frame.")
                    continue
                    # To improve performance, optionally mark the image as not writeable to
                    # pass by reference.
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = face_mesh.process(image)

                # Draw the face mesh annotations on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Face recognition
                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        mp_drawing.draw_landmarks(
                            image=image,
                            landmark_list=face_landmarks,
                            connections=mp_face_mesh.FACEMESH_TESSELATION,
                            landmark_drawing_spec=None,
                            connection_drawing_spec=mp_drawing_styles
                                .get_default_face_mesh_tesselation_style())

                        mp_drawing.draw_landmarks(
                            image=image,
                            landmark_list=face_landmarks,
                            connections=mp_face_mesh.FACEMESH_CONTOURS,
                            landmark_drawing_spec=None,
                            connection_drawing_spec=mp_drawing_styles
                                .get_default_face_mesh_contours_style())

                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                FRAME_WINDOW.image(image)
        cam.release()