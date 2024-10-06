import pandas as pd
import numpy as np
import streamlit as st

# Load the data
emissions_per_capita = pd.read_csv('3- co-emissions-per-capita.csv')
annual_emissions = pd.read_csv('2- annual-co-emissions-by-region.csv')
temperature_anomaly = pd.read_csv('1- temperature-anomaly.csv')

def show_preprocessing():
    st.header("Basic Preprocessing in Data")
    
    # Preview of the datasets to give users a quick glance at the data being used
    st.subheader("Data Preview")
    st.write("Here is a preview of the **CO₂ Emissions Per Capita** dataset:")
    st.dataframe(emissions_per_capita.head())  

    st.write("Here is a preview of the **Annual CO₂ Emissions by Region** dataset:")
    st.dataframe(annual_emissions.head())

    st.write("Here is a preview of the **Temperature Anomaly** dataset:")
    st.dataframe(temperature_anomaly.head())

    # Summary statistics to give users a quick snapshot of the numerical data in the datasets
    st.subheader("Summary Statistics")
    st.write("Summary statistics for key numerical columns:")

    # Displaying summary statistics for the key datasets
    st.write("CO₂ Emissions Per Capita dataset:")
    st.write(emissions_per_capita.describe())

    st.write("Annual CO₂ Emissions by Region dataset:")
    st.write(annual_emissions.describe())

    st.write("Temperature Anomaly dataset:")
    st.write(temperature_anomaly.describe())

    # Handling missing values
    st.subheader("Handling Missing Values")
    st.write("Identifying missing values in the datasets:")
    st.write("CO₂ Emissions Per Capita dataset:")
    st.write(emissions_per_capita.isnull().sum())
    st.write("Annual CO₂ Emissions by Region dataset:")
    st.write(annual_emissions.isnull().sum())
    st.write("Temperature Anomaly dataset:")
    st.write(temperature_anomaly.isnull().sum())

# Call the function to run the analysis
if __name__ == "__main__":
    show_preprocessing
