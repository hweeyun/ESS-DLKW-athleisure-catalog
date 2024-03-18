# Import python packages
import streamlit as st
# from snowflake.snowpark.context import get_active_session
import pandas as pd
import snowflake.connector

# Write directly to the app
st.title("Zena Amazing Athleisure Catalog")

# Get the current credentials
cnx = st.connection("snowflake")
session = cnx.session()

df = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website")
# st.dataframe(data=df, use_container_width=True)

pd_df = df.to_pandas()


color_list = pd_df['COLOR_OR_STYLE']

color_or_style = st.selectbox('Pick a sweatsuit color or style: ', color_list)

image = pd_df[pd_df['COLOR_OR_STYLE']==color_or_style]['DIRECT_URL'].iloc[0]
st.image(image, caption ='Our warm, comfortable, '+ color_or_style + ' sweatsuit!')


price = pd_df[pd_df['COLOR_OR_STYLE']==color_or_style]['PRICE'].iloc[0]
st.write('Price: ', price)

sizes_avail = pd_df[pd_df['COLOR_OR_STYLE']==color_or_style]['SIZE_LIST'].iloc[0]
st.write('Sizes Available: ', sizes_avail)

bonus = pd_df[pd_df['COLOR_OR_STYLE']==color_or_style]['UPSELL_PRODUCT_DESC'].iloc[0]
st.write('', bonus)
