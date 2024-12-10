import matplotlib.pyplot as plt
import streamlit as st

def clean_data(data):
    """
    Cleans data by handling anomalies and missing values.
    Example logic: Replace null values with 0
    """
    data.fillna(0, inplace=True)  # Handle nulls
    return data


def visualize_data(data, column_to_plot):
    """
    Visualize data with matplotlib
    """
    fig, ax = plt.subplots()
    data[column_to_plot].plot(kind='hist', ax=ax, title=f"Distribution of {column_to_plot}")
    st.pyplot(fig)
