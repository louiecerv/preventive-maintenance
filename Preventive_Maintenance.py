import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.subheader('Preventive Maintenance Data Analysis')

    st.write('Load the data')
    df = pd.read_csv('./data/predictive_maintenance.csv')

    # Filter records based on store and item (assuming single values)
    options = df['device'].unique()
    # Create the option box using st.selectbox
    selected_option = st.sidebar.selectbox("Select a device:", options)

    filtered_df = df[df['device'] == selected_option]

    df = filtered_df.copy()

    st.write('Display the data')
    st.write(df)

if __name__ == '__main__':
    app()   

