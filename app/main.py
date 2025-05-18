import streamlit as st
import pandas as pd
from utils import (
    load_data,
    get_summary_stats,
    create_boxplot,
    create_time_series,
    get_top_regions,
    calculate_correlation,
    get_metric_description
)

# Page config
st.set_page_config(
    page_title="Solar Potential Analysis",
    page_icon="☀️",
    layout="wide"
)

# Title and description
st.title("Solar Potential Analysis Dashboard")
st.markdown("""
This dashboard provides interactive visualizations and analysis of solar potential
across three West African countries: Benin, Sierra Leone, and Togo.
""")

# Sidebar
st.sidebar.header("Controls")

# Country selection
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    ["Benin", "SierraLeone", "Togo"],
    default=["Benin", "SierraLeone", "Togo"]
)

# Metric selection
metric = st.sidebar.selectbox(
    "Select Metric",
    ["GHI", "DNI", "DHI"],
    index=0
)

# Display metric description
st.sidebar.markdown("---")
st.sidebar.markdown(f"**{metric} Description:**")
st.sidebar.info(get_metric_description(metric))

# Load data
@st.cache_data
def load_all_data():
    dfs = []
    for country in selected_countries:
        try:
            df = load_data(country)
            dfs.append(df)
        except Exception as e:
            st.error(f"Error loading data for {country}: {str(e)}")
    return pd.concat(dfs) if dfs else None

# Main content
if selected_countries:
    df = load_all_data()
    
    if df is not None:
        # Create two columns for layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(f"{metric} Distribution")
            fig_box = create_boxplot(df, metric)
            st.plotly_chart(fig_box, use_container_width=True)
            
            st.subheader("Summary Statistics")
            stats = get_summary_stats(df, [metric])
            st.dataframe(stats)
        
        with col2:
            st.subheader("Time Series Analysis")
            fig_ts = create_time_series(df, metric)
            st.plotly_chart(fig_ts, use_container_width=True)
            
            st.subheader("Top Regions")
            top_regions = get_top_regions(df, metric)
            st.dataframe(top_regions)
        
        # Correlation analysis
        st.subheader("Correlation Analysis")
        metrics = ["GHI", "DNI", "DHI"]
        corr_matrix = calculate_correlation(df, metrics)
        st.dataframe(corr_matrix)
        
        # Additional insights
        st.subheader("Key Insights")
        st.markdown("""
        - **Highest Solar Potential**: Benin shows the highest mean GHI (236.23 W/m²)
        - **Most Consistent**: Togo exhibits the most stable solar conditions
        - **Diffuse Radiation**: Sierra Leone has comparable DHI values despite lower overall potential
        """)
else:
    st.warning("Please select at least one country to view the analysis.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Developed for Solar Challenge Week 1</p>
    <p>Data Source: Solar radiation measurements from Benin, Sierra Leone, and Togo</p>
</div>
""", unsafe_allow_html=True)
