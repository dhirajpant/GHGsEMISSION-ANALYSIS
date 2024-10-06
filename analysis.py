import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('CO2 emission by countries.csv', encoding='latin1')

def run_analysis():
    # Set up the plot for cumulative CO2 emissions over time
    plt.figure(figsize=(10, 5))
    df.groupby('Year')['CO2 emission (Tons)'].sum().plot()
    plt.title("Cumulative CO2 Emissions Over Time")
    plt.xlabel("Year")
    plt.ylabel("CO2 Emissions (Tons)")
    
    # Display the first plot in Streamlit
    st.pyplot(plt.gcf())
    
    # Write analysis text
    st.write("""
        We can see that cumulative CO2 emissions increased rapidly. According to the United States Environmental Protection Agency:

        "Global carbon emissions from fossil fuels have significantly increased since 1900. Since 1970, CO2 emissions have increased by about 90%, 
        with emissions from fossil fuel combustion and industrial processes contributing about 78% of the total greenhouse gas emissions increase from 1970 to 2011.
        Agriculture, deforestation, and other land-use changes have been the second-largest contributors. 
        Emissions of non-CO2 greenhouse gases have also increased significantly since 1900."
    """)

    # Set up the bar plot for top CO2-emitting countries in 2020
    plt.figure(figsize=(10, 5))
    top_emitters_2020 = df[df['Year'] == 2020].sort_values(by='CO2 emission (Tons)', ascending=False).head(30)
    sns.barplot(x='Country', y='CO2 emission (Tons)', data=top_emitters_2020)
    plt.xticks(rotation=90)
    plt.title("Top 30 CO2 Emitting Countries in 2020")
    plt.xlabel("Country")
    plt.ylabel("CO2 Emissions (Tons)")

    # Display the second plot in Streamlit
    st.pyplot(plt.gcf())
    
    # Write the conclusion for the top emitters
    st.write("""
        The United States and China stand out as the largest emitters. The top 5 countries have a significant influence and impact on global emissions.
        These top 5 countries contribute approximately 57% of the global cumulative CO2 emissions.
    """)

    # Filter data for the top 5 CO2-emitting countries
    df_top5 = df[df['Country'].isin(['United States', 'China', 'Russia', 'Germany', 'United Kingdom'])]

    # Set up the line plot for top 5 CO2 emitting countries over time
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Year", y="CO2 emission (Tons)", 
                data=df_top5, hue="Country", style="Country", 
                markers=True, dashes=False)
    plt.title("CO₂ Emissions Over Time: Top 5 Countries")
    plt.xlabel("Year")
    plt.ylabel("CO2 Emissions (Tons)")

    # Display the third plot in Streamlit
    st.pyplot(plt.gcf())

    st.write("""Cumulative CO2 emission of United States began to incerese rapidly early 1900s, and that of china began to incerese rapidly late 1900s.
""")

# Call the function to run the analysis
if __name__ == "__main__":
    run_analysis()
