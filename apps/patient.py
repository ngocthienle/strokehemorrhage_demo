# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:53:34 2021
# https://onlinelibrary.wiley.com/doi/full/10.1111/jth.12066
@author: thienle
"""

import streamlit as st
from PIL import Image
import datetime


def app():
    image = Image.open(chula_logo.png')
    st.image(image)
    today = datetime.date.today()

    # Using the "with" syntax
    with st.form(key='Patient_info',clear_on_submit=True):
        st.subheader('Date/Time of Consultation')
        st.markdown("""
            <style>
            .big-font {
                font-size:20px !important;
            }
            </style>
            """, unsafe_allow_html=True)
        col21, col22 = st.columns(2)
        col21.date_input('Date of Consultation', today)
        col22.time_input('Time', key=int)

        col23, col24 = st.columns(2)
        hospital = col23.selectbox('Hospital',
                                   ('King Chulalongkorn Memorial Hospital', 'Nopparat Rajathanee Hospital',
                                    'BMA General (Klang) Hospital',
                                    "Kluaynamthai Hospital", "Kluaynamthai 2 Hospital", "BNH Hospital",
                                    "Benchakitti Park Hospital", "Mahaesak Hospital",
                                    "The Bangkok Christian Hospital", "Phetkasem 2 Hospital", "Sukumvit Hospital",
                                    "Theptarin Hospital", "Piyavate Hospital",
                                    "Burachat Chaiyakon Hospital", "Lat Krabang Hospital", "Wetchakarunrasm Hospital",
                                    "Charoen Krung Pracharak Hospital",
                                    ))
        col24.number_input(label='Hospital No.', min_value= 0, step=1)

        col1, col2 = st.columns(2)
        col1.number_input(label='Age', min_value= 0, step=1)
        col2.selectbox('Gender', ['Male', 'Female', 'Others'])
        st.selectbox('Time Onset', ['Clear Onset', 'Unknown Onset'])
        ##
        st.subheader('Clinical data')
        st.markdown('<p class="big-font">Time-course</p>',
                    unsafe_allow_html=True)
        col7, col8, col9, col10 = st.columns(4)
        col7.checkbox('Wake-up')
        col8.checkbox('Peak at the onset')
        col9.checkbox('Gradual')
        col10.checkbox('Rapidly improve')

        st.markdown('<p class="big-font">Symptoms</p>',
                    unsafe_allow_html=True)
        ##
        col11, col12, col13, col25 = st.columns(4)
        col11.checkbox('Alteration of consciousness')
        col12.checkbox('Right facial weakness')
        col13.checkbox('Left facial weakness')
        col25.checkbox('Right hemiparesis')
        ##
        col14, col15, col26, col27 = st.columns(4)
        col14.checkbox('Left hemiparesis')
        col15.checkbox('Dysarthria')
        col26.checkbox('Dysphasia/aphasia')
        col27.checkbox('Ataxia')
        ##
        col16, col17, col18 = st.columns(3)
        col16.checkbox('Vertigo')
        col17.checkbox('Visual problem')
        col18.checkbox('Others')

        st.markdown('<p class="big-font">Underlying disease</p>',
                    unsafe_allow_html=True)

        col19, col20, col26 = st.columns(3)
        col19.checkbox('Deny U/D')
        col20.checkbox('Hx TIA (same site, within 2 wks)')
        col26.checkbox('Previous TIA')

        col27, col28, col29 = st.columns(3)
        col27.checkbox('Previous stroke')
        col28.checkbox('HT')
        col29.checkbox('DM')

        col30, col31, col32 = st.columns(3)
        col30.checkbox('DLP')
        col31.checkbox('Valvular heart disease')
        af1 = col32.checkbox('AF')

        col33, col34, col35 = st.columns(3)
        col33.checkbox('Coronary heart disease')
        col34.checkbox('CKD')
        col35.checkbox('Peripheral arterial disease')

        col36, col37, col38 = st.columns(3)
        col36.checkbox('Obesity')
        col37.checkbox('Smoking')
        col38.checkbox('Other')

        col39, col40, col41 = st.columns(3)
        col39.number_input('Systolic BP (mmHg)', min_value= 0, step=1)
        col40.number_input('Diastolic BP (mmHg)', min_value= 0, step=1)
        col41.number_input('Heart rate', min_value= 0, step=1)

        col42, col43, col44, col45 = st.columns(4)
        col42.checkbox('Regular')
        col43.checkbox('AF ')
        col44.checkbox('Irregular')
        col45.checkbox('N/A')

        st.markdown('<p class="big-font">EKG 12 leads</p>',
                    unsafe_allow_html=True)
        col46, col47, col48, col49 = st.columns(4)
        col46.checkbox('Normal')
        ekg12_af = col47.checkbox('AF  ')
        col48.checkbox('Abnormal')
        ekg12 = col49.checkbox('N/A ')
        #
        st.subheader('NIHSS Item')
        st.number_input('NIHSS Score', min_value=0, step=1)
        ##
        st.markdown('<p class="big-font">1a. LOC</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = Alert and responsive')
        st.checkbox('1 = Arousable to minor stimulation')
        st.checkbox('2 = Arousable only to painful stimulation')
        st.checkbox('3 = Reflex responses or unarousable')
        ##
        st.markdown('<p class="big-font">1b. LOC question</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = Both correct')
        st.checkbox('1 = One correct (or dysarthria, intubated, forein lang)')
        st.checkbox('2 = Neither correct')
        ##
        st.markdown('<p class="big-font">1c. Commands</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = Both correct ')
        st.checkbox('1 = One correct')
        st.checkbox('2 = Neither correct ')
        ##
        st.markdown('<p class="big-font">2. Best gaze</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = Normal ')
        st.checkbox('1 = One correct ')
        st.checkbox('2 = Neither correct  ')
        ##
        st.markdown('<p class="big-font">3. Visual field</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = No visual loss')
        st.checkbox('1 = Partial hemianopia')
        st.checkbox('2 = Complete hemianopia')
        st.checkbox('3 = Bilateral hemianopia or blindness')
        ##
        st.markdown('<p class="big-font">4. Facial palsy</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = Normal  ')
        st.checkbox('1 = Minor')
        st.checkbox('2 = Partial')
        st.checkbox('3 = Complete')
        st.markdown('<p class="big-font">5a. Motor arm (right)</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = No drift x 10 secs')
        st.checkbox('1 = Drift but does not hit bed')
        st.checkbox('2 = Some antigravity effort')
        st.checkbox('3 = No antigravity at all')
        st.checkbox('4 = No movement at all')
        st.checkbox('UN due to amputation, fusion, fx')

        st.markdown('<p class="big-font">5b. Motor arm (left)</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = No drift x 10 secs ')
        st.checkbox('1 = Drift but does not hit bed ')
        st.checkbox('2 = Some antigravity effort ')
        st.checkbox('3 = No antigravity at all ')
        st.checkbox('4 = No movement at all ')
        st.checkbox('UN due to amputation, fusion, fx ')

        st.markdown('<p class="big-font">6a. Motor leg (right)</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = No drift x 5 secs')
        st.checkbox('1 = Drift but does not hit bed  ')
        st.checkbox('2 = Some antigravity effort  ')
        st.checkbox('3 = No antigravity at all  ')
        st.checkbox('4 = No movement at all  ')
        st.checkbox('UN due to amputation, fusion, fx  ')

        st.markdown('<p class="big-font">6b. Motor leg (left)</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = No drift x 5 secs ')
        st.checkbox('1 = Drift but does not hit bed   ')
        st.checkbox('2 = Some antigravity effort   ')
        st.checkbox('3 = No antigravity at all   ')
        st.checkbox('4 = No movement at all   ')
        st.checkbox('UN due to amputation, fusion, fx   ')

        st.markdown('<p class="big-font">7. Limb ataxia</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = No ataxia')
        st.checkbox('1 = Ataxia in upper or lower extremity')
        st.checkbox('2 = Ataxia in upper AND lower extremity')
        st.checkbox('UN due to amputation, fusion, fx    ')

        st.markdown('<p class="big-font">8. Sensory</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = Normal   ')
        st.checkbox('1 = Mild-to-mod unilateral loss')
        st.checkbox('2 = Total loss')

        st.markdown('<p class="big-font">9. Best language</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = Normal    ')
        st.checkbox('1 = Mild-mod aphasia')
        st.checkbox('2 = Severe aphasia')
        st.checkbox('3 = Mute, global aphasia, coma')

        st.markdown('<p class="big-font">10. Dysarthria</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = Normal     ')
        st.checkbox('1 = Mild-mod')
        st.checkbox('2 = Severe')
        st.checkbox('UN = intubation or mech barrier')

        st.markdown('<p class="big-font">11. Extinction/Neglect</p>',
                    unsafe_allow_html=True)
        st.checkbox('0 = Normal, none detected. (vis loss alone)')
        st.checkbox('1 = Neglects or extinguishes to double simult stimulation in any modality')
        st.checkbox('2 = Profound neglect in more than one modality')

        st.subheader('Brain Imaging and Treatment')
        st.markdown('<p class="big-font">CT Brain result</p>',
                    unsafe_allow_html=True)
        col50, col51= st.columns(2)
        col50.checkbox('Normal CT result')
        col51.checkbox('Abnormal CT result')
        st.markdown('<p class="big-font">ASPECT Score</p>',
                    unsafe_allow_html=True)
        st.number_input('ASPECT Score', min_value=0, step=1)

        st.markdown('<p class="big-font">CTA brain and neck</p>',
                    unsafe_allow_html=True)
        col52, col53, col54= st.columns(3)
        col52.checkbox('Normal CTA')
        col53.checkbox('Abnormal CTA')
        col54.checkbox('Not done CTA')

        st.markdown('<p class="big-font">CT Perfusion</p>',
                    unsafe_allow_html=True)
        col55, col56 = st.columns(2)
        col55.checkbox('Done perfusion')
        col56.checkbox('Not done perfusion')

        st.markdown('<p class="big-font">Contraindication for Intravenous thrombolysis</p>',
                    unsafe_allow_html=True)
        col57, col58 = st.columns(2)
        col57.checkbox('Yes')
        col58.checkbox('No')

        st.markdown('<p class="big-font">Contraindication for Intravenous thrombolysis</p>',
                    unsafe_allow_html=True)
        col59, col60, col61, col62, col63 = st.columns(5)
        col59.checkbox('Antiplatelet')
        col60.checkbox('Anticoagulant')
        col61.checkbox('Antihypertensive')
        col62.checkbox('Statin')
        col63.checkbox('Others   ')

        submit_button = st.form_submit_button(label='Submit')
        # Results can be either form or outsite
        if submit_button:
            st.success("The information of patient from {} has been recorded.".format(hospital))
                       
