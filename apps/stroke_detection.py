# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:54:08 2021

@author: thienle
"""
# Import libraries
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input as vgg19_preprocess_input


@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model("aimodels/strokedata3_model_vgg19_29August2021.h5")
    return model

with st.spinner('Loading Model Into Memory...'):
    model = load_model()

def app():
    image = Image.open('D:\OneDrive\streamlitprojects\strokeapps\multi_page_app\chula_logo.png')
    st.image(image)
    st.title("""CT-Brain Image Abnormal Detection""")
    # Create header explaination
    my_expander = st.expander("See explanation", expanded = False)
    with my_expander:
            st.write("""
                 This web-apps detects a CT-brain image is normal or abnormal (with signs of stroke) using backend AI engine.
                 The trained AI engine is based on the pre-trained VGG19 deep learning model.
                     """)
            st.write(""" The abnormal regions (e.g.: Intracerebral haemorrhage, Subarachnoid haemorrhage) are not the same though center brain layer, top brain layer, and eyeball brain layer.""")
            image = Image.open('example_pics.jpg')
            st.image(image,caption='Example CT-brain images. Source of these images from CQ500 publish dataset (http://headctstudy.qure.ai/dataset)')
                
    st.subheader('Choose a CT-brain image and get the detection')
    uploaded_file = st.file_uploader("Upload CT-brain image", type=["jpg", "png"])

    map_dict = {0: 'background.',
            1: 'abnormal at center brain layer', # hge
            2: 'abnormal at eyeball brain layer.', #hge_eyeball
            3: 'abnormal at top brain layer.', #hge_top
            4: 'normal at center brain layer.',#nonehge
            5: 'normal at eyeball brain layer.',#nonehge_eyeball
            6: 'normal at top brain layer.', #nonehge_top
            }
    if uploaded_file is not None:
        # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
        resized = cv2.resize(opencv_image,(224,224))
        # Now do something with the image! For example, let's display it:
        st.image(opencv_image, channels="RGB", use_column_width = False, width=300)
    # If the trained AI model using normalized divide (/255) images, then the images for predicting also divide 255.
        resized = vgg19_preprocess_input(resized)/255 # Normalized the input images by divide 255.
        img_reshape = resized[np.newaxis,...]
    
        Genrate_pred = st.button("Generate Detection")    
        if Genrate_pred:
            prediction = model.predict(img_reshape).argmax()
            if prediction == 0: st.info("The CT-brain image is {}".format(map_dict [prediction]))
            if prediction == 4: st.info("The CT-brain image is {}".format(map_dict [prediction]))
            if prediction == 5: st.info("The CT-brain image is {}".format(map_dict [prediction]))
            if prediction == 6: st.info("The CT-brain image is {}".format(map_dict [prediction]))
            if prediction == 1: st.error("The CT-brain image is {}".format(map_dict [prediction]))
            if prediction == 2: st.error("The CT-brain image is {}".format(map_dict [prediction]))
            if prediction == 3: st.error("The CT-brain image is {}".format(map_dict [prediction]))
        
