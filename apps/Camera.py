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

def app():
    image = Image.open('chula_logo.png')
    st.image(image)
    st.title("""Video Stroke Rehabilitation Monitoring""")
    st.write(" ------ ")
    st.write("This apps allows user upload the after-stroke rehabilitation video to evaluate the corrected exercises.")
    # Define and call all the functions when the web-app starts.
    ###
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    cam = cv2.VideoCapture(0)

    while run:
        ret, frame = cam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        st.write('Stopped')