# -*- coding: utf-8 -*-
"""
Created on Friday, October 01 07:43:53 2021
This the third apps in the Stroke Project: Monintoring and tracking rehabilitation
of stroke patient.
@author: thienle
"""
import streamlit as st
from PIL import Image

def app():
    image = Image.open('D:\OneDrive\streamlitprojects\strokeapps\multi_page_app\chula_logo.png')
    st.image(image)

    st.title("""Development of a Communication System for Treatment and Rehabilitation of Stroke Patients""")
    st.write(" ------ ")
    st.subheader("""Objective""")
    st.write("- Build an AI model that can identify the abnormal regions through many layers of brain: Size, Shape, Location")
    st.write("- Clinical correlation for stroke and large-vessel occlusion detection")
    
    expander_faq = st.expander("More About The Project")
    expander_faq.write("Hi there! If you have any questions about our project, please contact:")
    expander_faq.write("Professor Dr. Watit Benjapolakul: watit.b@chula.ac.th")

    
    
    
    