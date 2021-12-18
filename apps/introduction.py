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
    image = Image.open('chula_logo.png')
    st.image(image)

    st.title("""Development of a Communication System for Treatment and Rehabilitation of Stroke Patients""")
    st.write(" ------ ")
    st.subheader("""Video Meeting""")
    st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Please click to the link below to set up a video meeting.</p>',
                unsafe_allow_html=True)
    link = "[Video Meeting](https://chulastrokeconference.netlify.app/)"
    st.markdown(link, unsafe_allow_html=True)

    
    
    
    
