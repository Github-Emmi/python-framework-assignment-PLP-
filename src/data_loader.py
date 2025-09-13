import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data(path='data/metadata_sample.csv'):
    """Load the CORD-19 metadata with caching for performance"""
    try:
        df = pd.read_csv(path, low_memory=False)
        return df
    except FileNotFoundError:
        st.error("Data file not found. Please ensure metadata.csv is in the data/ directory.")
        return pd.DataFrame()

def explore_data(df):
    """Generate basic exploration info"""
    if df.empty:
        return "No data available"
    
    # Basic info
    buffer = []
    buffer.append(f"Dataset shape: {df.shape}")
    buffer.append(f"Columns: {', '.join(df.columns)}")
    
    # Missing values
    missing = df.isnull().sum().sort_values(ascending=False)
    missing_pct = (missing / len(df) * 100).round(2)
    missing_df = pd.DataFrame({'Missing Values': missing, 'Percentage': missing_pct})
    
    return buffer, missing_df