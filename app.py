import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.viz import *

# Page configuration
st.set_page_config(
    page_title="CORD-19 Research Explorer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .subheader {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-bottom: 1.5rem;
    }
    .metric-label {
        font-weight: bold;
        color: #2ca02c;
    }
    .stButton>button {
        border-radius: 8px;
    }
    /* Dark mode support */
    @media (prefers-color-scheme: dark) {
        .main-header {
            color: #7fbfff;
        }
    }
</style>
""", unsafe_allow_html=True)

# App title
st.markdown('<h1 class="main-header">CORD-19 Research Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader">A professional exploration of COVID-19 academic literature</p>', unsafe_allow_html=True)

# Sidebar with filters and info
with st.sidebar:
    st.header("Data Controls")
    
    # Data loading with spinner
    with st.spinner("Loading dataset..."):
        df_raw = load_data('data/metadata_sample.csv')
    
    if not df_raw.empty:
        with st.spinner("Cleaning data..."):
            df_clean = clean_data(df_raw)
        
        st.success("Data loaded successfully!")
        
        # Filters
        st.header("Filters")
        min_year = int(df_clean['publish_year'].min())
        max_year = int(df_clean['publish_year'].max())
        selected_years = st.slider(
            "Select Year Range:",
            min_year, max_year, (min_year, max_year)
        )
        
        # Journal selector
        top_journals_list = df_clean['journal'].value_counts().head(20).index.tolist()
        selected_journal = st.selectbox(
            "Select a Journal:",
            options=["All"] + top_journals_list
        )
        
        # Show dataset info
        st.header("Dataset Info")
        st.write(f"**Total Papers:** {len(df_clean):,}")
        st.write(f"**Date Range:** {min_year} - {max_year}")
        
    else:
        st.error("Please ensure the data file is in the correct location.")

# Main content area
if not df_raw.empty:
    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Publications", "Content Analysis", "Raw Data"])
    
    with tab1:
        st.header("Overview Metrics")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Papers", f"{len(df_clean):,}") # type: ignore
        with col2:
            st.metric("Earliest Publication", int(df_clean['publish_year'].min())) # type: ignore
        with col3:
            st.metric("Latest Publication", int(df_clean['publish_year'].max())) # type: ignore
        
        # Publications by year
        st.header("Publications Over Time")
        fig = plot_publications_by_year(df_clean, selected_years) # type: ignore
        st.pyplot(fig)
        
        # Key insight
        st.info("""
        **Insight:** The number of COVID-19 related publications increased dramatically in 2020, 
        reflecting the global research response to the pandemic.
        """)
    
    with tab2:
        st.header("Publication Sources")
        
        # Top journals
        col1, col2 = st.columns([2, 1])
        with col1:
            fig = plot_top_journals(df_clean) # type: ignore
            st.pyplot(fig)
        with col2:
            st.subheader("Journal Stats")
            journal_stats = df_clean['journal'].value_counts() # type: ignore
            st.write(f"**Unique Journals:** {len(journal_stats):,}")
            st.write(f"**Papers in Top 10 Journals:** {journal_stats.head(10).sum():,}")
        
        # Top authors (Standout Tip - advanced visualization)
        st.header("Top Authors")
        fig = plot_top_authors(df_clean) # type: ignore
        st.pyplot(fig)
    
    with tab3:
        st.header("Content Analysis")
        
        # Word cloud
        fig = plot_title_wordcloud(df_clean) # type: ignore
        st.pyplot(fig)
        
        # Abstract length distribution
        st.subheader("Abstract Length Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df_clean['abstract_word_count'], bins=30, ax=ax) # type: ignore
        ax.set_xlabel('Word Count')
        ax.set_ylabel('Number of Papers')
        ax.set_title('Distribution of Abstract Lengths', fontweight='bold')
        st.pyplot(fig)
    
    with tab4:
        st.header("Raw Data Preview")
        st.dataframe(df_clean.head(100), use_container_width=True) # type: ignore
        
        # Download button
        csv = df_clean.to_csv(index=False) # type: ignore
        st.download_button(
            label="Download Cleaned Data as CSV",
            data=csv,
            file_name="cord19_cleaned.csv",
            mime="text/csv",
        )

else:
    st.warning("Please load the data to proceed.")