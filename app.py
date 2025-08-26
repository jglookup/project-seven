import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# App header
st.header('Used Vehicles Data Analysis in the US')

# Load the dataset
car_data = pd.read_csv('vehicles_us.csv')

# Checkbox for histogram
if st.checkbox('Show histogram of odometer readings'):
    st.write('Histogram for the "odometer" column')
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(
        title_text='Distribution of Odometer Readings',
        xaxis_title='Odometer (miles)',
        yaxis_title='Count'
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox for scatter plot
if st.checkbox('Show scatter plot: Odometer vs Price'):
    st.write('Scatter plot of "odometer" vs "price"')
    fig_scatter = go.Figure(data=[
        go.Scatter(
            x=car_data['odometer'],
            y=car_data['price'],
            mode='markers',
            marker=dict(opacity=0.6, color='orange')
        )
    ])
    fig_scatter.update_layout(
        title_text='Odometer vs Price',
        xaxis_title='Odometer (miles)',
        yaxis_title='Price (USD)'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)