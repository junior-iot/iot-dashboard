import pandas as pd 
import streamlit as st 
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQo6u0LSpFpxtuIir6mFekHUv2fbOLPfrUkc5636_thMoKvsKzN-R1g4vtjmYgdwroPS2aMLASwIbiS/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url) 
st.title("Monitoramento IoT") 
st.line_chart(df[['temperatura', 'umidade']]) 
st.dataframe(df)
