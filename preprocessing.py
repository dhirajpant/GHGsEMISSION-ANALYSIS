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

    # Fill missing values with mean or drop rows with missing data
    st.write("Filling missing values with the mean (if any):")
    emissions_per_capita.fillna(emissions_per_capita.mean(), inplace=True)
    annual_emissions.fillna(annual_emissions.mean(), inplace=True)
    temperature_anomaly.fillna(temperature_anomaly.mean(), inplace=True)
    st.write("Missing values have been handled.")

    # Feature engineering: Creating new features (Example: Year-over-year emission change)
    st.subheader("Feature Engineering")
    st.write("Creating a new feature for annual emissions change in the 'Annual CO₂ Emissions by Region' dataset.")
    annual_emissions['YoY Emission Change'] = annual_emissions['Emissions'].pct_change()
    st.write(annual_emissions.head())

    # Data normalization
    st.subheader("Data Normalization")
    st.write("Normalizing the 'CO₂ Emissions Per Capita' dataset using min-max scaling:")
    emissions_per_capita['CO2 Per Capita (Normalized)'] = (emissions_per_capita['CO2 Per Capita'] - emissions_per_capita['CO2 Per Capita'].min()) / (emissions_per_capita['CO2 Per Capita'].max() - emissions_per_capita['CO2 Per Capita'].min())
    st.write(emissions_per_capita.head())

    # Handling outliers: Example of identifying outliers in 'CO₂ Emissions Per Capita'
    st.subheader("Outlier Detection")
    st.write("Identifying potential outliers using the interquartile range (IQR) method:")
    Q1 = emissions_per_capita['CO2 Per Capita'].quantile(0.25)
    Q3 = emissions_per_capita['CO2 Per Capita'].quantile(0.75)
    IQR = Q3 - Q1
    outliers = emissions_per_capita[(emissions_per_capita['CO2 Per Capita'] < (Q1 - 1.5 * IQR)) | (emissions_per_capita['CO2 Per Capita'] > (Q3 + 1.5 * IQR))]
    st.write(outliers)

    # Data transformation: Example of log transformation on 'CO₂ Per Capita'
    st.subheader("Data Transformation")
    st.write("Applying log transformation to reduce skewness in the 'CO₂ Emissions Per Capita' dataset:")
    emissions_per_capita['CO2 Per Capita (Log Transformed)'] = emissions_per_capita['CO2 Per Capita'].apply(lambda x: np.log(x + 1))
    st.write(emissions_per_capita.head())

# Run the preprocessing page
show_preprocessing()
