# Dashboard

# Local
## Setup enviroment

conda create --name main-ds python=3.9

conda activate main-ds

pip install numpy pandas scipy matplotlib 
seaborn jupyter streamlit babel

## Run steamlit app

streamlit run app.py

# Colab
## Setup dependecy

!pip install streamlit

import streamlit as st

## Run steamlit app

upload app.py

!streamlit run app.py & npx localtunnel --port 8501

copy your url 

masukan code External URL setelah HTTP dan sebelum nomor port
