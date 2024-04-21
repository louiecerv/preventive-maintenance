import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.subheader('Preventive Maintenance Data Analysis')

    st.write('Load the data')

    # Read the CSV file
    df = pd.read_csv('./data/predictive_maintenance.csv')

    st.write('Display the raw data')
    st.write(df)
    st.write(df.shape)

    # Filter the DataFrame to include only rows where failure is equal to 1
    df_failure_1 = df[df['failure'] == 1]
    st.write('Display the data where failure is equal to 1')
    st.write(df_failure_1)
    st.write(df_failure_1.shape)

    # Get unique device IDs where failure is equal to 1
    device_failure_1 = df_failure_1['device'].unique()

    # Filter the original DataFrame to include only rows with device IDs where failure is equal to 1
    filtered_df = df[df['device'].isin(device_failure_1)]

    # Display the filtered DataFrame
    st.write("Filtered DataFrame where device failure==1:")
    st.write(filtered_df)
    st.write(filtered_df.shape)

    # Filter records based on selected metric
    options = ['metric1', 'metric2', 'metric3', 'metric4', 'metric5', 'metric6', 'metric7', 'metric8', 'metric9']
    selected_metric = st.sidebar.selectbox("Select a metric to filter:", options)

    # Filter the DataFrame by device and calculate the average of specified metrics
    filtered_df_metric = filtered_df.groupby('device').filter(lambda x: (x[selected_metric] != 0).any())

    # Display the data of the devices that have the selected metric != 0
    st.write('Display the data filtered based on the selected metric:')
    st.write(filtered_df_metric)
    st.write(filtered_df_metric.shape)

    # Get unique devices where failure is equal to 1
    options = filtered_df_metric['device'].unique()
    numdevices = len(options)
    st.write('Number of devices:', numdevices)  

    selected_device = st.sidebar.selectbox("Select a device:", options)
    df_device = filtered_df_metric[filtered_df_metric['device'] == selected_device]
    st.write(df_device)
    st.write(df_device.shape)

    # Plot the selected metric
    # Assuming df is your DataFrame with columns date, device, metric1, metric2
    # Make sure 'date' column is in datetime format
    filtered_df_metric['date'] = pd.to_datetime(filtered_df_metric['date'])

    # Set 'date' column as the index
    filtered_df_metric.set_index('date', inplace=True)

    # Filter records based on selected metric
    options = ['metric1', 'metric2', 'metric3', 'metric4', 'metric5', 'metric6', 'metric7', 'metric8', 'metric9']
    selected_metric = st.sidebar.selectbox("Select a metric to plot:", options)

    # Create figure and axis objects
    fig, ax = plt.subplots()

    # Iterate over unique devices and plot metric1
    for device in filtered_df_metric['device'].unique():
        df_device = filtered_df_metric[filtered_df_metric['device'] == device]
        ax.plot(df_device.index, df_device[selected_metric], label=device)

    # Add labels and legend
    ax.set_xlabel('Date')
    ax.set_ylabel('Metric 1')
    ax.set_title('Metric 1 of Devices Over Time')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

if __name__ == '__main__':
    app()   

