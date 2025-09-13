import pandas as pd
import re
from datetime import datetime

def clean_text(text):
    """Helper function to clean text data"""
    if pd.isna(text):
        return ""
    # Convert to lowercase and remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', str(text))
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_data(df):
    """Clean and preprocess the CORD-19 dataset"""
    df_clean = df.copy()
    
    # Drop rows with missing critical fields
    df_clean = df_clean.dropna(subset=['title', 'publish_time'])
    
    # Convert publish_time to datetime
    df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
    df_clean = df_clean.dropna(subset=['publish_time'])
    
    # Extract year from publication date
    df_clean['publish_year'] = df_clean['publish_time'].dt.year
    
    # Filter out unrealistic years
    current_year = datetime.now().year
    df_clean = df_clean[(df_clean['publish_year'] > 1900) & (df_clean['publish_year'] <= current_year)]
    
    # Create new features
    df_clean['abstract_word_count'] = df_clean['abstract'].apply(
        lambda x: len(str(x).split()) if pd.notna(x) else 0
    )
    
    # Clean text fields
    df_clean['title_clean'] = df_clean['title'].apply(clean_text)
    
    return df_clean