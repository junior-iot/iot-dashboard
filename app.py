import pandas as pd 
import streamlit as st 
url = "https://script.google.com/macros/s/AKfycbw_GJ4BnBGCzXK8_kNsUVKH43tsZ22RIR2xxjeDEU6Z7sHK4jifvq0D4woI8Oazx0KE/exec" 
df = pd.read_csv(url) 
st.title("Monitoramento IoT") 
st.line_chart(df[['temperatura', 'umidade']]) 
st.dataframe(df)
