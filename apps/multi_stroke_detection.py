# -*- coding: utf-8 -*-
"""
Created October 02, 11:54:08 2021

@author: Thien Le, Postdoc Researcher
"""
import cv2
import numpy as np
import pandas as pd
# Import libraries
import streamlit as st
import tensorflow as tf
from PIL import Image
from tensorflow.keras.applications.vgg19 import preprocess_input as vgg19_preprocess_input


@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model("aimodels/strokedata3_model_vgg19_29August2021.h5")
    return model
@st.cache()
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

with st.spinner('Loading Model Into Memory...'):
    model = load_model()

def app():
    image = Image.open('chula_logo.png')
    st.image(image)
    st.title("""Multiple CT-Brain Images Abnormal Detection""")
    # Create header explaination
    my_expander = st.expander("See explanation", expanded=False)
    with my_expander:
        st.write("""
                 This web-apps receives many CT-brain images and predicts the results as table using backend AI engine.
                 The trained AI engine is based on the pre-trained VGG19 deep learning model.
                 """)
        image = Image.open('example_pics.jpg')
        st.image(image,
                 caption='Example CT-brain images. Source of these images from CQ500 publish dataset (http://headctstudy.qure.ai/dataset)')
    ### Create a table to store the predicted resutls

    df = pd.DataFrame({
        'The image name': [],
        'Predicted result': []
    })
    ###
    map_dict = {0: 'Non interest.',
                1: 'Abnormal at center brain layer',  # hge
                2: 'Abnormal at eyeball brain layer.',  # hge_eyeball
                3: 'Abnormal at top brain layer.',  # hge_top
                4: 'Normal at center brain layer.',  # nonehge
                5: 'Normal at eyeball brain layer.',  # nonehge_eyeball
                6: 'Normal at top brain layer.',  # nonehge_top
                }
    ###
    st.subheader('Choose a CT-brain image and get the detection')
    # Allow multiple images uploading
    uploaded_files = st.file_uploader("Choose CT-brain images", type=["jpg", "png"], accept_multiple_files=True)
    if uploaded_files is not None:
        # Count the uploaded images
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            # df.loc[len(df.index)]=[uploaded_file.name, 'Yes']

            # Convert the file to an opencv image.
            file_bytes = np.asarray(bytearray(bytes_data), dtype=np.uint8)
            opencv_image = cv2.imdecode(file_bytes, 1)
            opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
            resized = cv2.resize(opencv_image, (224, 224))
            resized = vgg19_preprocess_input(resized) / 255
            img_reshape = resized[np.newaxis, ...]

            # Generate the prediction
            prediction = model.predict(img_reshape).argmax()
            if prediction == 0: df.loc[len(df.index)] = [uploaded_file.name, format(map_dict[prediction])]
            if prediction == 4: df.loc[len(df.index)] = [uploaded_file.name, format(map_dict[prediction])]
            if prediction == 5: df.loc[len(df.index)] = [uploaded_file.name, format(map_dict[prediction])]
            if prediction == 6: df.loc[len(df.index)] = [uploaded_file.name, format(map_dict[prediction])]
            if prediction == 1: df.loc[len(df.index)] = [uploaded_file.name, format(map_dict[prediction])]
            if prediction == 2: df.loc[len(df.index)] = [uploaded_file.name, format(map_dict[prediction])]
            if prediction == 3: df.loc[len(df.index)] = [uploaded_file.name, format(map_dict[prediction])]

    st.table(df)

    # Convert to csv file
    csv = convert_df(df)

    st.download_button(
        label="Download the table as CSV",
        data=csv,
        file_name="predicted_results.csv",
        mime="text/csv"
    )

