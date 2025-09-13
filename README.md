# CORD-19 Research Dashboard

A full-stack data application for exploring the COVID-19 Open Research Dataset (CORD-19) metadata.



## 🚀 Live Demo

[![Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://python-framework-assignment-plp-git-lwnn7lhcwgxakr4ezcrrlk.streamlit.app/)

## 📊 Project Overview

This project demonstrates a complete data workflow from raw data to interactive visualization:

1. **Data Loading**: Efficient loading of the large metadata file with caching
2. **Data Cleaning**: Handling missing values, date conversion, and text preprocessing
3. **Exploratory Analysis**: Identifying patterns and relationships in the data
4. **Visualization**: Creating informative and professional visualizations
5. **Web Application**: Building an interactive dashboard with Streamlit

## 🏗️ Project Structure
Frameworks_Assignment/
├── data/ # Contains the metadata.csv file
├── notebooks/ # Jupyter notebooks for exploration and analysis
├── src/ # Python modules for data processing
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── screenshots/ # Visualizations and app screenshots


## 🛠️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Frameworks_Assignment.git
   cd Frameworks_Assignment


## Install dependencies:
```bash
pip install -r requirements.txt

## Run the Streamlit app:

```bash
streamlit run app.py

## 📈 Key Insights
Research Surge: COVID-19 publications increased dramatically in 2020, showing the rapid scientific response to the pandemic

Leading Journals: The BMJ, PLoS ONE, and The Lancet published the most COVID-19 research

Common Themes: The most frequent title keywords were "covid", "patients", "health", and "pandemic"

## 🧠 Technical Highlights
Modular Code: Separated data loading, cleaning, and visualization into reusable modules

Efficient Processing: Implemented caching for better performance with large datasets

Professional Visualizations: Used Seaborn styling and annotations for publication-quality charts

Interactive Dashboard: Created a responsive Streamlit app with filters and multiple views

## 🤔 Reflections:
This project provided valuable experience in the full data science workflow:

Data Engineering Challenges: Handling a large, real-world dataset with many missing values

Analysis Techniques: Implementing both basic and advanced visualizations to extract insights

Application Development: Building an interactive web application for data exploration

Future improvements could include:

Topic modeling of abstracts

Citation network analysis

Integration with the full text of papers
