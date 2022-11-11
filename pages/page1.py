import streamlit as st 
import seaborn as sns
import plotly.express as px
st.set_page_config(page_title="Data Explorer", layout="wide")
st.header("This video is ")
st.text("Hi")
st.header("2nd head")

df=sns.load_dataset('iris')
st.write(df.head())
st.bar_chart(df[['sepal_length']])
tab1,tab2=st.tabs(["Tab 1", "Tab2"])
from shroomdk import ShroomDK
import pandas as pd
import matplotlib.pyplot as plt

# Initialize `ShroomDK` with your API Key
sdk = ShroomDK("00dba474-bd21-4d4d-a9b9-c5eaa08aac33")


# Parameters can be passed into SQL statements 
# via native string interpolation
my_address = "0xD5B130e81C5E2539d86f297E599A5adc127CA853"
sql = f"""
    SELECT 
        nft_address, 
        mint_price_eth, 
        mint_price_usd 
    FROM ethereum.core.ez_nft_mints 
    WHERE nft_to_address = LOWER('{my_address}')
"""

# Run the query against Flipside's query engine 
# and await the results
query_result_set = sdk.query(sql)

# Iterate over the results
# print(pd.DataFrame(query_result_set['records']))
res=(pd.DataFrame(query_result_set.records))
fig=px.line(res[['mint_price_eth']])
st.write(fig)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write('Caption for first chart')
    with col2:
        st.write(fig)
        


