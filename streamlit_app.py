"""
Wildfire Web App
"""

import streamlit as st
import pandas as pd
from PIL import Image

st.title("Wildfire Analysis")

DIXIE_FIRE = "/mnt/g/My Drive/School/NYU/Big Data Fall 2021/Project/dixie_creek/jpg/dixie.gif"

CAPTION = "Satellite imagery from 2021's Dixie Creek Fire in Oregon"

st.image(DIXIE_FIRE, caption=CAPTION, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.header("Image Classification in Wildfire Analysis")

st.subheader("Without Distributed Computing")

st.subheader("With Distributed Computing")