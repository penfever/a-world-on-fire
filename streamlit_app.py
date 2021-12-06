"""
Wildfire Web App
"""

import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_tensorboard import st_tensorboard

st.title("Wildfire Analysis")

st.header("Team Members")

st.markdown("Benjamin Feuer, Dennis Pang, Jinyang Xue, Subei Han, Yuvraj Raina")

DIXIE_FIRE = "results/img/dixie.gif"

IC_RES = "results/csv/xgb_pt.csv"

CAPTION = "Satellite imagery from 2021's Dixie Creek Fire in Oregon"

st.image(DIXIE_FIRE, caption=CAPTION, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.header("Project Overview")

st.markdown("In this project, we explore the enormous climate and imagery datasets now publicly available for researchers and extract unique lessons and actionable insights.")

st.markdown("For more analysis and notebooks containing the code used to generate this project, please visit out [project Github.](https://github.com/penfever/bigdata-proj)")

BLOCK = """
Questions we explore include --

* Why was the 2021 fire season so unusual? (Why are fires spreading faster? Why are they burning hotter? Why are they changing direction and speed more rapidly than in prior years? Why are traditional methods of fire modeling and containment proving less
effective than in prior years?)

* What are some unique ways to visualize the human and financial toll of these fires, using big data tools?

* What can we expect in 2022 and beyond, if current trends continue? (Should we expect more? How many? Where? What new regions might become wildfire hotspots as warming continues?)
"""

st.markdown(BLOCK)

st.header("Image Classification in Wildfire Analysis")

BLOCK_2 = """
Wildfire imagery can tell us a lot about fire behavior. Specifically, it can help spot them early, before they spread and become more difficult to control. 
We will employ state of the art image classification methods on wildfire imagery datasets, using popular frameworks such as PyTorch and XGBoost.
We will compare the results we can achieve using distributed computing techniques to the results we can achieve without distributed computing methods.
"""

st.markdown(BLOCK_2)

st.subheader("Without Distributed Computing")

BLOCK_3 = """
Without distributed computing methods, our entire dataset has to be loaded into the RAM of a single node. This is not always possible, and even when it is possible, it is much slower.
"""

st.markdown(BLOCK_3)

df = pd.read_csv(IC_RES)

df_wdc = df[['name', 'dataset', 'acc', 'runtime']].where(~df["distributed"]).dropna(how="all").sort_values(by=['dataset'])

df_wdc

st.subheader("With Distributed Computing (XGBoost / Dask / RAPIDS)")

BLOCK_4 = """
Distributed computing techniques enable us to generate results faster, and in some cases more accurately as well -- because we are able to distribute the load across multiple nodes, we can pick optimal settings for hyperparameters like batch size, which are usually constrained by the amount of GPU memory we have available.
"""

st.markdown(BLOCK_4)

df_dc = df[['name', 'dataset', 'acc', 'runtime']].where(df["distributed"]).dropna(how="all").sort_values(by=['dataset'])

df_dc

st.subheader("With Distributed Computing (PyTorch Lightning)")

st.subheader("Densenet: Ground")

st_tensorboard(logdir="results/tensorboard/densenet", port=8501, width=1080)

st.subheader("Resnet: Ground")

st_tensorboard(logdir="results/tensorboard/resnet", port=8501, width=1080)

st.subheader("Densenet: Aerial")

st_tensorboard(logdir="results/tensorboard/densenet_aerial", port=8501, width=1080)