# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:53:34 2021
# https://onlinelibrary.wiley.com/doi/full/10.1111/jth.12066
@author: thienle
"""

import streamlit as st
import numpy as np
import pandas as pd

def app():
    st.title("""Stroke LVO Web Application Chulalongkorn University""")
    
    # Using the "with" syntax
    with st.form(key='Patient_characteristics'):
        st.subheader('Patient information')
        patient_name = st.text_input('Patient Name')
        ##
        col1, col2, col3 = st.columns(3)
        
        col1.text_input(label='Citizen ID/Passport')
        col2.selectbox('Thai/Foreigner',['Thai', 'Foreigner'])
        col3.text_input(label = 'Age')
        ##
        col4, col5, col6 = st.columns(3)
        
        col4.selectbox('Gender',['Male', 'Female','Others'],key=1)
        col5.text_input(label = 'Weight(Kg)')
        col6.selectbox('Blood Type',['O+', 'O-', 'A+', 'A-','B+', 'B-','AB+', 'AB-'])
        ##
        st.subheader('Risk factors (pre-existing or newly discovered)')
        col7, col8, col9, col10 = st.columns(4)
        col7.checkbox('Hypertension')
        col8.checkbox('Diabetes mellitus')
        col9.checkbox('Active smoking')
        col10.checkbox('Atrial fibrillation')
        ##
        col11, col12, col13 = st.columns(3)
        col11.checkbox('Heart disease')
        col12.checkbox('Low ejection fraction')
        col13.checkbox('Previous cerebrovascular events')
        ##
        st.subheader('Medication at admission')
        col14, col15 = st.columns(2)
        col14.checkbox('Stroke onset during night sleep')
        col15.checkbox('Unknown stroke onset, not sleep')
        ##
        col16, col17, col18, col19, col20 = st.columns(5)
        col16.checkbox('Antiplatelet')
        col17.checkbox('Anticoagulant')
        col18.checkbox('Antihypertensive')
        col19.checkbox('Hypolipemic')
        col20.checkbox('Antidiabetic')
        ##
        submit_button = st.form_submit_button(label='Submit')
        # Results can be either form or outsite
        if submit_button:
            st.success("The information of patient {} has been recorded.".format(patient_name))
        
