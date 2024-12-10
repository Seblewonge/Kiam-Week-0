import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import clean_data, visualize_data


# Title of the Dashboard
st.title("📊 Streamlit Data Visualization Dashboard")

# Upload data file
uploaded_file = st.file_uploader("Upload your CSV file for visualization", type=["csv"])

if uploaded_file:
    # Read the uploaded file
    data = pd.read_csv(uploaded_file)

    # Clean data if necessary
    cleaned_data = clean_data(data)

    # Convert only valid numeric columns
    for col in cleaned_data.columns:
        # Only convert columns with numeric types, avoid dates and strings
        try:
            cleaned_data[col] = pd.to_numeric(cleaned_data[col], errors="coerce")
        except Exception as e:
            st.error(f"Could not convert column {col} to numeric: {e}")
    
    # Interactive Widgets
    st.sidebar.header("Interactive Controls")
    
    # Filter only numeric columns to select visualization features
    numeric_columns = cleaned_data.select_dtypes(include=['number']).columns
    if len(numeric_columns) == 0:
        st.error("No numeric columns available for visualization. Please check your uploaded CSV.")
    else:
        feature_to_visualize = st.sidebar.selectbox(
            "Select a numeric column to visualize",
            numeric_columns
        )
    
        # Set slider only to numeric data ranges
        try:
            filter_value = st.sidebar.slider(
                "Set a range for visualization",
                float(cleaned_data[feature_to_visualize].min()),
                float(cleaned_data[feature_to_visualize].max())
            )

            # Filter the data for visualization
            st.subheader("Visual Insights")
            filtered_data = cleaned_data[cleaned_data[feature_to_visualize] >= filter_value]

            # Call the visualization function
            visualize_data(filtered_data, feature_to_visualize)

        except ValueError as e:
            st.error(f"Error with the slider range: {e}")

else:
    st.write("Please upload a CSV file to get started!")
