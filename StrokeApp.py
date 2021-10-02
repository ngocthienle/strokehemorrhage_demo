# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:32:36 2021
The multi-page web application for stroke project- Chula
@author: thienle
"""
import streamlit as st
from PIL import Image
logo_image = Image.open('logo.png')

st.set_page_config(layout="centered", page_title='Stroke Application',
                   page_icon=logo_image)
from multiapp import MultiApp
from apps import stroke_detection, patient, introduction, multi_stroke_detection  # Import the app modules want here.


app = MultiApp()


# Add all your application here
app.add_app("Introduction", introduction.app)
app.add_app("Patient Record", patient.app)
app.add_app("Single CT Detection", stroke_detection.app)
app.add_app("Multiple CTs Detection", multi_stroke_detection.app)
# app.add_app("Video Monitoring", video.app)

# The main app
app.run()
