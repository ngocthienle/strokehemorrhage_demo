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
from apps import stroke_detection, patient # Import the app modules you want here.


app = MultiApp()


# Add all your application here
app.add_app("Patient Record", patient.app)
app.add_app("Stroke Detection", stroke_detection.app)

# The main app
app.run()
