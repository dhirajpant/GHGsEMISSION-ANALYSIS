import pandas as pd
import streamlit as st
import plotly.express as px

# Load the data
df_emission_region = pd.read_csv('2- annual-co-emissions-by-region.csv')

# Define a function to show the map in Streamlit
def show_map():
    st.header("Map")

    # Create the geo-scatter plot
    fig = px.scatter_geo(
        df_emission_region,
        locations='Code',  # ISO country codes
        locationmode='ISO-3',  # Define the location using country codes
        color='Annual CO₂ emissions',  # Color based on annual emissions
        size='Annual CO₂ emissions',  # Size of markers based on emissions
        hover_name='Entity',  # Hover text shows the country name
        animation_frame='Year',  # If you have multiple years, this will animate over time
        projection='natural earth',  # Map projection
        title='Annual CO₂ Emissions by Country',
        size_max=50  # Set the maximum size of the markers
    )

    # Customize the map's geographical details
    fig.update_geos(
        resolution=50,
        showcoastlines=True, coastlinecolor="RebeccaPurple",
        showland=True, landcolor="LightGreen",
        showocean=True, oceancolor="LightBlue",
        showlakes=True, lakecolor="Blue",
        showrivers=True, rivercolor="Blue"
    )

    # Display the Plotly map in Streamlit using st.plotly_chart
    st.plotly_chart(fig)

# Call the function to run the analysis in the Streamlit app
if __name__ == "__main__":
    show_map()
