# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 07:43:53 2021
This the third apps in the Stroke Project: Monintoring and tracking rehabilitation
of stroke patient.
@author: thienle
"""
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import numpy as np
import pandas as pd

def app():
    st.title("""Stroke Video Monitoring Chulalongkorn University""")
    webrtc_streamer(key="example")