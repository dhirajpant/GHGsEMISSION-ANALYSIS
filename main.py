import streamlit as st
import pandas as pd

# Set the title of the Streamlit app
st.title("CO₂ Emission & Temperature Anomaly Analysis Dashboard")
st.image("co2.png", caption="CO₂ Emission")

# Sidebar for navigation with titles
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ("Home", "Preprocessing", "Analysis", "Map", "Conclusion"))

# Home Page
if page == "Home":
    # Header and introductory content
    st.header("Welcome to the CO₂ Emission & Temperature Anomaly Analysis Dashboard")
    
    st.write("""
        This dashboard offers insights into the global CO₂ emissions and temperature anomalies using historical and contemporary datasets. 
        By analyzing carbon dioxide emissions per capita, annual emissions by region, and temperature anomalies, this tool enables 
        a deeper understanding of climate change and its impacts across different parts of the world.
        
        **Why is this important?**
        CO₂ is one of the primary greenhouse gases contributing to global warming. Tracking its emission patterns alongside 
        temperature anomalies provides vital information for policymakers, environmental scientists, and the public to address the 
        climate crisis. This dashboard offers a convenient way to visualize and explore these patterns across the globe.
    """)

    # Section introducing the datasets being used
    st.subheader("About the Data")
    st.write("""
        The data used in this dashboard is derived from globally recognized sources and consists of three primary components:

        1. **CO₂ Emissions Per Capita Dataset**: 
            - This dataset records the amount of CO₂ emissions per person in various countries and regions.
            - This is important for understanding the emissions burden per individual, allowing comparison between nations with different population sizes.
        
        2. **Annual CO₂ Emissions by Region Dataset**: 
            - This dataset provides annual emissions data categorized by region, allowing us to assess emissions trends over time.
            - Regional data helps to identify which areas of the world are contributing the most to global emissions and how emissions are changing as regions develop.
        
        3. **Temperature Anomaly Dataset**: 
            - This dataset tracks deviations from historical average temperatures, known as temperature anomalies.
            - Monitoring temperature anomalies is crucial for understanding how much the Earth's temperature has increased relative to pre-industrial levels, a key indicator of global warming.
    """)

    # Additional details about the datasets and metrics being used in the analysis
    st.subheader("Additional Details")
    st.write("""
        - **CO₂ Emissions Per Capita**: This metric helps assess the amount of CO₂ emitted per person in each country. 
        This is useful for understanding the relative contributions of different countries when accounting for population size.
        
        - **Regional Annual Emissions**: The annual emissions data allow us to track how emissions in different regions have 
        evolved over time, identifying patterns in industrialization and energy consumption.

        - **Temperature Anomalies**: These are deviations in temperature from historical averages. By tracking temperature anomalies, 
        we can assess how much global warming is occurring in different parts of the world.
    """)

    # Section describing the key features of the dashboard
    st.subheader("Key Features of This Dashboard")
    st.write("""
        This dashboard is designed to help users explore CO₂ emission trends and temperature anomalies through various interactive features:
        
        - **Home**: Provides an introduction to the dashboard and an overview of the datasets used in the analysis.
        
        - **Map**: Displays an interactive world map showing CO₂ emissions per country, allowing users to visually compare emissions across different regions.
        
        - **Analysis**: Features visualizations such as line charts and graphs to analyze the trends in CO₂ emissions per capita, regional emissions, and temperature anomalies over time.
        
        - **Conclusion**: Summarizes the key findings from the analysis and discusses the broader implications for climate policies and global sustainability.
    """)


# Analysis Page
elif page == "Analysis":
    import analysis  # Import the analysis module
    analysis.run_analysis()  # Call the function to run the analysis

# Conclusion Page
elif page == "Conclusion":
    import conclusion  # Import the conclusion module
    conclusion.show_conclusion()  # Call the function to show the conclusions

# Map Page
elif page == "Map":
    import map  # Import the Map module
    map.show_map()  # Call the function to show the Map

# Map Page
elif page == "Preprocessing":
    import preprocessing  # Import the Preprocessing module
    preprocessing.show_preprocessing()# Call the function to show the Preprocessing