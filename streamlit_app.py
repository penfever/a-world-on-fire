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

TB = "results/img/tb_vid.mp4"

TB_CAPTION = "Animated demonstration of interactive Tensorboard dashboard"

st.title("A World on Fire: Confronting the Growing Challenge of Wildfire Detection and Suppression")

st.header("Team Members")

st.markdown("Benjamin Feuer, Dennis Pang, Jinyang Xue, Subei Han, Yuvraj Raina")

st.markdown("For more analysis and notebooks containing the code used to generate this project, please visit out [project Github.](https://github.com/penfever/bigdata-proj)")

st.subheader("ABSTRACT")

BLOCK_7 = """
This report aims to succinctly document the existence of a novel and
growing threat in the United States -- the rise of uncontrolled
megafires driven primarily by climate change. It lays out the reasons it
is reasonable to believe that the frequency and intensity of fires is
increasing, and why systemic climate change is the likely culprit for
these changes. Finally, it addresses how recent advances in distributed
technology can potentially lead to successful and timely interventions
by professional firefighting teams.

Below is a summary of the three major points we cover \--

-   I. Recent evidence derived from data released by US Government
    agencies leads us to conclude that wildfires pose an increasing
    threat to the lives and property of United States citizens.

-   II\. This threat is driven by changes at the level of society rather than
    the individual, and as such, we must seek systemic, structural solutions
    to the problem.

-   III\. Distributed deep learning models for image classification as a
    potential method of improving wildfire response times by emergency teams
    and thereby reducing wildfire spread.

Afterwards, we offer a brief conclusion and a list of resources for
further exploration.
"""

st.markdown(BLOCK_7)

st.subheader("Case Study: Dixie Creek")

BLOCK_6 = """
The images below are from a 2021 California wildfire called Dixie Creek. By August 6, it had grown to become the largest single (i.e. non-complex) wildfire in the state's history, and the second-largest overall (after the August Complex fire of 2020),[7][8] bigger than the state of Rhode Island, according to Wikipedia.
"""

DIX_IMG = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Pyrocumulus_cloud_produced_by_the_Dixie_Fire_on_July_22-5865.jpg/2560px-Pyrocumulus_cloud_produced_by_the_Dixie_Fire_on_July_22-5865.jpg"

DIX_CAPT = "The Dixie Creek Wildfire from ground level."

st.markdown(BLOCK_6)

st.image(DIX_IMG, caption=DIX_CAPT)

st.image(DIXIE_FIRE, caption=CAPTION, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("These shocking images were captured by NASA's high-resolution MODIS imager and converted from GEOTIFF to RGB format crops which you see here. The images are spread out over a series of weeks. Note the massive smoke trail that develops and fades, clearly visible from space.")

st.image(".//media/image18.jpeg", caption="A home burns in Plumas County. Source: NY Times")

"""
Yet, at ground level, the message is all too easy to comprehend.

This year, it was the homes, stores and services Plumas County that were
razed to the ground.

Next year, it could be ours.
"""

st.subheader("SECTION I: Recognizing the Increasing Toll of Wildfires")

BLOCK_8 = """
In order to justify increased action on wildfire prevention, we must
first address the underlying implications of our investigation.

**Do wildfires pose an increasing threat to the lives and property of
United States citizens?**

One possible measure of wildfire threat is a raw frequency count of
wildfires per year, like the one we see here, aggregated from NASA's
[FIRMS dataset](https://firms.modaps.eosdis.nasa.gov/download/). (2021
is omitted throughout this report because for that year, the data remain
incomplete as of this writing.)
"""
st.markdown(BLOCK_8)

st.image(".//media/image1.png", caption="Wildfires per year, 2001-2020")

"""
By this metric, wildfire frequency in 2020 was the 2nd-highest out of
the entire 20-year record, and 60% of the 5 peak years occurred between
2015 and 2020, which represents only 30% of the dataset.

The data on the intensity of these wildfires tells a similar story. We
see that the average fire intensity, as measured by sub-pixel fire
radiative power retrievals (**FRP**)\[Csiszar et al., 2014\] and
apparent brightness, both reached new records in 2020.
"""

st.image(".//media/image2.png", caption="Wildfire FRP per year, 2001-2020")
st.image(".//media/image3.png", caption="Wildfire Apparent Brightness per year, 2001-2020")

"""
By all three of these measures, we can see that wildfires are increasing
in frequency and intensity. It is logical to conclude that more frequent
and more intense wildfires will cause greater damage to life, property
and ecosystem and will require greater resources to combat, and indeed
the evidence bears this out \-- federal wildfire suppression costs in
the United States have spiked from an annual average of about \$425
million from 1985 to 1999 to \$1.6 billion from 2000 to 2019, according
to data from
[NIFC](https://www.nfpa.org/News-and-Research/Publications-and-media/NFPA-Journal/2020/November-December-2020/Features/Wildfire).
In 2017 alone, damage from wildfires across the US exceeded a staggering
[\$18 billion](https://www.iii.org/graph-archive/208963). Other parts of
the world are being hit hard, too. This past summer, Spain suffered the
worst wildfires that [it's seen in 20
years](https://www.theguardian.com/world/2019/jun/27/hundreds-of-firefighters-tackle-blaze-in-north-east-spain),
while [thousands of fires
burned](https://www.nationalgeographic.com/environment/2019/08/amazon-fires-cause-deforestation-graphic-map/)
in the Amazon Rainforest, an increase of [over 80 percent compared to
the same time period last
year](http://queimadas.dgi.inpe.br/queimadas/portal-static/situacao-atual/).
"""

BLOCK_5 = """
According to National Interagency Fire Center data, of the 10 years with the largest acreage burned, all have occurred since 2004, including the peak year in 2015. This period coincides with many of the warmest years on record nationwide (see the U.S. and Global Temperature indicator). The largest increases have occurred during the spring and summer months.
"""

st.markdown(BLOCK_5)

st.image(WF_TREND)

st.markdown("As the damage caused by wildfires intensifies, so does public interest in a more complete understanding of its causes and consequences.")

df_g = pd.read_csv(GF_RES)

df_g["Month"] = df_g["Month"].apply(lambda x: dateutil.parser.parse(x))
df_g["Month"] = df_g["Month"].dt.to_period("Y")
df1 = pd.DataFrame()
dfg_agg = df_g.groupby("Month").max()
dfg_agg = dfg_agg.assign(year=pd.Series([i for i in range(2004, 2022)]).values)
dfg_agg = dfg_agg[["year", "wildfire"]]
fig = px.line(dfg_agg, x="year", y="wildfire", title='Year over year peak interest in wildfires (Google Trends)')
st.plotly_chart(fig)

st.subheader("SECTION II: Understanding Key Wildfire Causes")

"""
In Section I, we showed that wildfires have indeed grown more frequent
and more intense. However, in order to consider how best to combat the
issue, we must consider another aspect of the problem.

**Can we draw any meaningful conclusions about the causes and locations
of these wildfires, and can we use this information to better evaluate
potential solutions?**

To answer this question, we may begin by noting that this increase is
not evenly distributed among all states. Historically, the drier states
west of the Mississippi river have accounted for nearly all of the major
wildfires by acreage burned, and this continues to be true, as this
[NCWG dataset](https://www.kaggle.com/rtatman/188-million-us-wildfires)
shows.
"""

st.image(".//media/image4.png", caption="A map depicting the location of large wildfires, 2000-2020")

"""
Drought-ridden California, in particular, accounts for a
disproportionate share of the increase in 2020, as we can see below in
this [FIRMS dataset](https://firms.modaps.eosdis.nasa.gov/download/)
graph of fire frequency by region (with regions represented as (lat,
long) coordinate pairs).
"""

st.image(".//media/image5.png", caption="A surge in California wildfires in 2020")

"""
Indeed, if we consider the raw increase in number of reported fires
year-over-year, California consistently shows up as a hotspot. 
Using data from NOAA's NIDIS Drought monitor, we can see that the recent
droughts in California correlate closely with peak fire years recorded
in FIRMS.
"""

st.image(".//media/image7.png", caption="NOAA NIDIS Drought Data in California")

"""
These data suggest that an increase in drought conditions is strongly
correlated with an increase in wildfire frequency and intensity, and
that [ongoing conditions](https://climate.nasa.gov/evidence/) leading to
extreme shifts in climate may also be driving the surge in wildfires we
have documented above.

We can further confirm this by considering how regional data on wildfire
causes, sourced from [NIFC WFIGS Wildfire
Locations](https://data-nifc.opendata.arcgis.com/datasets/nifc::wfigs-wildland-fire-locations-full-history/about)
data, influence the problem.

By raw count, human-initiated wildfires exceed that of natural
wildfires. Furthermore, human-initiated wildfires are increasing in
frequency, whereas the frequency of natural wildfires has remained flat.
"""

st.image(".//media/image8.png", caption="NIFC Causes of Wildfires")
st.image(".//media/image9.png", caption="NIFC Causes of Wildfires over time")
st.image(".//media/image10.png", caption="NIFC Causes of Wildfires over time")

"""
This might seem to contradict our earlier conclusions
about drought being a major driver of increasing wildfire intensity.
However, when we look at area burned in this [NCWG
dataset](https://www.kaggle.com/rtatman/188-million-us-wildfires), we
can see that the story is in fact quite different. Lightning alone
accounts for more burned area than all other causes combined, with room
to spare.

The explanation for this is well understood \-- fires started by human
beings tend to occur in populated areas, and are therefore more likely
to be detected and contained before they grow into uncontained
megafires. Fires caused by lightning (and to a lesser extent,
malfunctioning electrical equipment) tend to happen in remote and
inaccessible areas and are more difficult to detect and combat
effectively.
"""

st.image(".//media/image11.png", caption="Burned area aggregated by wildfire cause")

"""
This fact accounts for the following
graph. Alaska is the bottom third of states for wildfire frequency.
However, in terms of acreage burned, it exceeds the bottom twenty states
in the list combined. Alaska's low population and rugged terrain make it
a very difficult environment for firefighters.

Although large uncontrolled forest fires have always been a historical
fact of life, that does not mean that the size and frequency of
wildfires we are seeing today is somehow natural. Indeed, it is likely
that the side-effects of man-made climate change, such as the droughts
we documented above, are driving a vicious cycle in the environment
which itself contributes to further climate change. [Consider that from
1950 until 2009, forest fires in Alaska have released CO2 equal to half
of all carbon emissions from the european
union.](https://www.Dw.Com/en/forest-fires-in-alaska-a-ticking-climate-time-bomb/a-18684423)
Uncontrolled wildfire, natural or not, poses a significant climate
threat when ignored.

Alaska's northerly latitude has previously protected it from large-scale
wildfires -- simply put, where there's ice, there isn't fire. However,
ice coverage has [dropped precipitously in
Alaska](https://www.carbonbrief.org/humans-causing-up-to-two-thirds-arctic-summer-sea-ice-loss-study-confirms)
since the 1970s, and at least 50% of this loss is caused by greenhouse
gas emissions.

Furthermore, there is reason to believe that as Earth's climate
continues to change, so may the regional character of fire distribution
in the United States. According to [NIFC
data](https://data-nifc.opendata.arcgis.com/datasets/nifc::wfigs-wildland-fire-locations-full-history/about),
in 2021, midwestern states have had fire counts similar to those found
in West Coast states in 2014 and 2015. Even more alarmingly, as we can
see in the maps below from 2002 (left) and 2020 (right), the majority of
wildfire burned area is no longer a Western state problem; in 2020, all
but a handful of states saw enough annual burned area to register on the
chart.
"""

st.image(".//media/image12.png", caption="Alaska burn area")
st.image(".//media/image13.png", caption="Alaska burn area")

"""
Overall, the data lead us to conclude that the size and scale of
lightning-caused wildfires is the major driver of the overall increase
in wildfire intensity and acreage burned, which is in turn driven by
changes in Earth's climate. We further conclude that the scope of the
problem is broadening to include areas which were previously protected,
which is likely to continue the vicious cycle of the destruction of
forests, which serve as natural [carbon
sinks](https://www.wri.org/insights/forests-absorb-twice-much-carbon-they-emit-each-year),
and the corresponding release of CO2 into the atmosphere.

The unhappy fact is that the challenges represented by these findings
are predominantly the result of long-term, collective policies and
incentives rather than individual choices. While it remains vitally
important for vacationers to extinguish their campfires and cigarettes
fully before leaving a forest, it will not and cannot make Alaskan
mountain ranges easier to traverse, nor can it stop the polar ice caps
from vanishing.

As such, we contend that systemic solutions are demanded. Governor Gavin
Newsom of California recognized this fact with his [recent dedication of
funds](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjzm4qu2u30AhWVjIkEHSAABNQ4ChAWegQIBRAB&url=https%3A%2F%2Fwww.gov.ca.gov%2F2021%2F04%2F13%2Fgovernor-newsom-signs-landmark-536-million-wildfire-package-accelerating-projects-to-protect-high-risk-communities%2F&usg=AOvVaw090ezI0vcqoykBw5YD8to4)
to wildfire suppression. While national and state policy and budgeting
decisions are well beyond the scope of this report, we can address a
different aspect of the challenge -- the role of deep learning models in
early detection of wildfires.
"""


st.subheader("SECTION III: Taking Action on Wildfires")

BLOCK_2 = """
Wildfires play an important role in natural systems, and their
elimination is neither practical nor desirable. However, containment of
[megafires](https://www.nationalgeographic.org/encyclopedia/megafire/)
could achieve the best of both worlds, preventing unnatural surges while
allowing healthy fires to burn under close monitoring. Unfortunately, it
is impossible to contain a fire if you don't know where it is.

For this reason, it is a well-documented fact that early detection,
partnered with prevention, must form the cornerstones of any successful
wildfire management policy. Even small delays in detection can be very
costly. Megafires can move at speeds of [nearly 15 miles per
hour](https://en.wikipedia.org/wiki/Wildfire) under favorable winds.
"""
st.markdown(BLOCK_2)

st.components.v1.iframe(r'<iframe width="560" height="315" src="https://www.youtube.com/embed/vhJeDYQVtdQ?start=15" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')

"""
At its peak, the Camp Fire is estimated to have burned an area greater
than one [football
field](https://www.cnn.com/2018/11/09/us/wildfires-why-they-spread-so-quickly-wcx/index.html)
(roughly 1.32 acres) in a single second.

[Pano
AI](https://www.sfchronicle.com/travel/article/S-F-startup-uses-AI-to-detect-wildfires-before-16668146.php),
a San Francisco startup, is one of a number of private and public
ventures that are currently attempting to use deep learning algorithms
to detect wildfires quickly. While Pano and U. Nevada's
[ALERT](https://www.alertwildfire.org/) focus on aerial and ground-level
detection, respectively, placing high-definition panoramic cameras and
satellite transmitters everywhere from telephone poles to remote
mountaintops, other systems, like [U.C. Berkeley's
FUEGO](https://fuego.ssl.berkeley.edu/) and [UCSD's
WiFire](https://wifire.ucsd.edu/), have chosen to focus on detecting
wildfires from satellite imagery. Still others have proposed using
[fleets of
drones](https://spectrum.ieee.org/drones-sensors-wildfire-detection) to
sweep high-risk areas.

One thing that all of these solutions have in common is their reliance
on state of the art deep learning models to distinguish images which
contain fires from those which do not. These methods can be extremely
fast and accurate, particularly when they combine image classification
and semantic segmentation models with
[traditional](https://www.mdpi.com/journal/remotesensing/special_issues/biomass_burning_rs)
[algorithmic](https://doi.org/10.1016/j.rse.2016.02.027)
[approaches](https://doi.org/10.1016/j.rse.2015.08.032). Research is
[ongoing](https://www.mdpi.com/journal/remotesensing/special_issues/biomass_burning_rs)
in the area, but results are promising, and data on active fires are
currently collected in real time from
[NASA](https://firms.modaps.eosdis.nasa.gov/download/) and
[NOAA](https://raws.nifc.gov/) satellites, among others.

Our investigation focused on the potential of distributed systems to
improve the speed and accuracy of image classifiers on fire data, since
improvements in these areas could decrease the cost and improve the
utility of all fire detection systems.
"""

st.subheader("Our Methodology")

BLOCK_9 = """
1.  We collected and cleaned three image classification datasets of fire
    / non-fire images. The datasets were chosen to simulate a range of
    natural environments in which a remote sensor could be placed; at
    ground level, in the air, and on a satellite.

2.  We designed and implemented a control group of image classifiers
    using convention ML and DL frameworks (XGBoost and PyTorch,
    respectively)

3.  We re-implemented our models in distributed frameworks. Wherever
    possible, we replicated the hyperparameters and architecture of the
    model. We did, however, adapt the data ingest process to account for
    the unique demands of distributed systems, switching from image
    directories to parquet files in situations where they were
    supported.

4.  We logged the results of our experiments to a remote database and
    compared them.
"""

st.markdown(BLOCK_9)

st.subheader("Key Findings")

BLOCK_10 = """
-   With proper data cleaning and methodology, modern DL and ML models
    are capable of achieving classification accuracy greater than 90% on
    all three types of data, without the benefit of metadata or
    additional algorithmic techniques.

-   On average, the traditional ML boosted tree classifier was generally
    less accurate than deep CNNs -- however, the difference was often
    not large, and careful cleaning and preparation of data it was
    possible to eliminate much of the difference

-   The boosted tree classifier was, on average, between 2x and 3x
    faster than the deep CNNs, on both training and inference.

-   When multispectral data was available (as in the case of the
    Landsat-8 GeoTIFF files), training the classifier on all 10 bands
    was prohibitively slow and led to worse results. The choice of bands
    was pivotal in achieving peak accuracy, particularly the boosted
    tree classifiers, which are not location-invariant. Specifically,
    the use of SWIR data ([bands 6 and
    7](https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites)
    for Landsat-8) improved accuracy dramatically.

-   Google Colab Pro is a poor environment for distributed computing
    experiments because of its lack of support for virtual environments,
    unpredictable hardware assignments and frequent timeouts. Future
    experiments should be conducted on a different cloud service or on
    the HPC.

-   Dask-ml and RAPIDS are considerably less mature than PySpark, and
    remain rough around the edges. For instance, RAPIDS cannot be
    installed in a non-conda environment, and Dask and RAPIDS both lack
    direct support for ANY deep learning framework, although it is
    possible to distribute certain aspects of a PyTorch model manually
    using Dask's joblib (we did not attempt this). However, their
    potential for distributed learning is unparalleled because RAPIDS
    allows the offloading of massive datasets from the GPU to RAM
    without disrupting training -- this means that the size of a RAPIDS
    dataset is (in theory) bounded only by the hardware it is running
    on.

-   PyTorch Lightning includes built-in SLURM support and highlights the
    powerful flexibility of the underlying PyTorch architecture --
    switching from a fully local to a fully distributed environment in
    Lightning involves changing just one line of code, unlike in
    Dask/RAPIDS, where it requires a complete refactor.

-   Even in the completely sub-optimal distributed environment (one
    node, one GPU, remote training) under which these experiments were
    conducted, distributed models were either as fast or faster than
    their non-distributed counterparts (20% faster, on average). We
    attribute this difference to more efficient data processing.

-   Accuracy varied wildly between distributed and non-distributed
    models. We are still trying to account for the reasons for these
    differences -- however, we suspect it has to do with the different
    frameworks either processing the data differently or running with
    different default hyperparameters.
"""

st.markdown(BLOCK_10)

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
     ("Animation", 'Densenet: Ground', 'Resnet: Ground', 'Densenet: Aerial'))

count = 0

if mod_pick == "Animation":
    video_file = open(TB, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
elif mod_pick == 'Densenet: Ground':
    st.subheader("Densenet: Ground")
    st_tensorboard(logdir="results/tensorboard/densenet", port=6006, width=1080)
    count += 1
elif mod_pick == 'Resnet: Ground':
    st.subheader("Resnet: Ground")
    st_tensorboard(logdir="results/tensorboard/resnet", port=6007, width=1080)
    count += 1
elif mod_pick == "Densenet: Aerial":
    st.subheader("Densenet: Aerial")
    st_tensorboard(logdir="results/tensorboard/densenet_aerial", port=6008, width=1080)
    count += 1

st.subheader("Conclusions and Future Work")

"""
We consider these results a promising start to understanding the full transformative potential of big data in this area. However, there is more work to be done, including robustifying our classifiers and refining our testing methodology to improve accuracy and consistency. We look forward to pursuing this work in the near future.
"""

st.subheader("Our Team and Our Tools")

BLOCK_11 = """
TEAM

**Ben Feuer** served as the project lead, designed and performed all the
tests in Part III, created the interactive dashboard, created and
maintained the repository, and wrote the final report.

All other team members produced supplemental project reports, which are
available in the repository.

**Subei Han** lead the [FIRMS
dataset](https://firms.modaps.eosdis.nasa.gov/download/) and created all
of the analytics used in Part I, as well as portions of Part II.

**Dennis Pang** and **Jinyang Xue** co-lead the investigation into the
[NIFC
data](https://data-nifc.opendata.arcgis.com/datasets/nifc::wfigs-wildland-fire-locations-full-history/about)
and created portions of the analytics used in Part II.

**Yuvraj Raina** lead the investigation into the [NCWG
dataset](https://www.kaggle.com/rtatman/188-million-us-wildfires) and
created portions of the analytics used in Part II.

TOOLS

All code was written and all models were trained on [Google Colab
Pro](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0waHs4-30AhVZjYkEHfOtASYQFnoECAQQAQ&url=https%3A%2F%2Fcolab.research.google.com%2Fsignup&usg=AOvVaw0l1TdGCKd9vmmpE5Q0Zrk1)
and written in [Jupyter notebooks](jupyter.org).

We used [PySpark](https://spark.apache.org/docs/latest/api/python/)
environment for the majority of our analytics. The techniques we used
included aggregation, pivoting and window functions. When necessary, we
used [miniconda](https://docs.conda.io/en/latest/miniconda.html) within
Colab as an environment manager.

Our graphs and charts were produced using
[Matplotlib](https://matplotlib.org/),
[Seaborn](https://seaborn.pydata.org/),
[Altair](https://altair-viz.github.io/), and [Plotly
Express](https://plotly.com/python/plotly-express/).

We used [Fiona](https://pypi.org/project/Fiona/) and
[RasterIO](https://rasterio.readthedocs.io/en/latest/) to process
geospatial data and images.

Our map visualizations were generated using
[Folium](https://python-visualization.github.io/folium/plugins.html) and
[Plotly Express](https://plotly.com/python/plotly-express/).

Our base classifier models were written in
[PyTorch](https://pytorch.org/) and
[XGBoost](https://xgboost.readthedocs.io/en/stable/).

We used [PyArrow](https://arrow.apache.org/docs/python/index.html) to
generate parquet files for the distributed classifiers.

Our distributed classifiers were written in [PyTorch
Lightning](https://www.pytorchlightning.ai/),
[Dask-ml](https://dask.org/) and
[RAPIDS](https://developer.nvidia.com/rapids).

[MongoDB Atlas](https://www.mongodb.com/atlas/database) and
[Tensorboard](https://www.tensorflow.org/tensorboard) were used to log
the results of the classifiers.

Our interactive dashboard was created using [streamlit](streamlit.io/).

LICENSE

The contents of this report and repository are subject to the [MIT
License](https://opensource.org/licenses/MIT).
"""

st.markdown(BLOCK_11)