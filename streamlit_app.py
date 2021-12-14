"""
Wildfire Web App
"""

import streamlit as st
import pandas as pd
import dateutil
from PIL import Image
from streamlit_tensorboard import st_tensorboard
import plotly.express as px

DIXIE_FIRE = "results/img/dixie.gif"

IC_RES = "results/csv/xgb_pt.csv"

WF_TREND = "https://www.epa.gov/sites/default/files/2021-04/wildfires_download2_2021.png"

GF_RES = "results/csv/fire_interest.csv"

CAPTION = "Satellite imagery from 2021's Dixie Creek Fire in Oregon"

TB = "results/img/tb_viz.gif"

TB_CAPTION = "Animated demonstration of interactive Tensorboard dashboard"

st.title("Wildfire Analysis")

st.header("Team Members")

st.markdown("Benjamin Feuer, Dennis Pang, Jinyang Xue, Subei Han, Yuvraj Raina")

st.image(DIXIE_FIRE, caption=CAPTION, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

BLOCK_6 = """
The images above are from a 2021 wildfire called Dixie Creek. By August 6, it had grown to become the largest single (i.e. non-complex) wildfire in the state's history, and the second-largest wildfire overall (after the August Complex fire of 2020),[7][8] bigger than the state of Rhode Island, according to Wikipedia.
"""

DIX_IMG = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Pyrocumulus_cloud_produced_by_the_Dixie_Fire_on_July_22-5865.jpg/2560px-Pyrocumulus_cloud_produced_by_the_Dixie_Fire_on_July_22-5865.jpg"

DIX_CAPT = "The Dixie Creek Wildfire from ground level."

st.markdown(BLOCK_6)

st.image(DIX_IMG, caption=DIX_CAPT)

st.markdown("These stunning images are a perfect introduction to the topic of our project -- understanding wildfires.")

st.header("Project Overview")

BLOCK_5 = """
Climate change continues to transform the planet, and it appears wildfire seasons are growing longer and more intense as a consequence. According to National Interagency Fire Center data, of the 10 years with the largest acreage burned, all have occurred since 2004, including the peak year in 2015. This period coincides with many of the warmest years on record nationwide (see the U.S. and Global Temperature indicator). The largest increases have occurred during the spring and summer months.
"""

st.markdown(BLOCK_5)

st.image(WF_TREND)

st.markdown("As the damage caused by wildfires intensifies, so does the interest in a more complete understanding of its causes and consequences.")

df_g = pd.read_csv(GF_RES)

df_g["Month"] = df_g["Month"].apply(lambda x: dateutil.parser.parse(x))
df_g["Month"] = df_g["Month"].dt.to_period("Y")
df1 = pd.DataFrame()
dfg_agg = df_g.groupby("Month").max()
dfg_agg = dfg_agg.assign(year=pd.Series([i for i in range(2004, 2022)]).values)
dfg_agg = dfg_agg[["year", "wildfire"]]
fig = px.line(dfg_agg, x="year", y="wildfire", title='Year over year peak interest in wildfires (Google Trends)')
st.plotly_chart(fig)

st.markdown("Big data techniques and technologies have transformed our understanding of a wide range of topics. Can they do the same for wildfire analysis?")

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

st.markdown("Please select a model to view its Tensorboard. Please note -- this feature may not be enabled on Streamlit Cloud. In that case, only the GIF animation will be available.")

mod_pick = st.radio(
     "Pick a model",
     ('Animation', 'Densenet: Ground', 'Resnet: Ground', 'Densenet: Aerial'))

if mod_pick == 'Animation':
    st.subheader("GIF Animation of Tensorboard Output")
    st.image(TB, caption=TB_CAPTION, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
elif mod_pick == 'Densenet: Ground':
    st.subheader("Densenet: Ground")
    st_tensorboard(logdir="results/tensorboard/densenet", port=6006, width=1080)
elif mod_pick == 'Resnet: Ground':
    st.subheader("Resnet: Ground")
    st_tensorboard(logdir="results/tensorboard/resnet", port=6007, width=1080)
elif mod_pick == "Densenet: Aerial":
    st.subheader("Densenet: Aerial")
    st_tensorboard(logdir="results/tensorboard/densenet_aerial", port=6008, width=1080)

st.markdown("For details on the models and insight into the code, please check out the accompanying notebooks.")