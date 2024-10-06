import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('CO2 emission by countries.csv', encoding='latin1')

def run_analysis():

    st.markdown("### Global CO₂ Emissions Over Time")
    # Set up the plot for cumulative CO2 emissions over time
    plt.figure(figsize=(10, 5))
    df.groupby('Year')['CO2 emission (Tons)'].sum().plot()
    plt.title("Cumulative CO2 Emissions Over Time")
    plt.xlabel("Year")
    plt.ylabel("CO2 Emissions (Tons)")
    
    # Display the first plot in Streamlit
    st.pyplot(plt.gcf())
    
    # Write analysis text
    st.markdown("""
        #### Key Insights:
 
        
        The global CO₂ emissions have increased dramatically over the past century. According to the United States Environmental Protection Agency:

        > "Global carbon emissions from fossil fuels have significantly increased since 1900. Since 1970, CO2 emissions have increased by about 90%, 
        > with emissions from fossil fuel combustion and industrial processes contributing about 78% of the total greenhouse gas emissions increase from 1970 to 2011.
        > Agriculture, deforestation, and other land-use changes have been the second-largest contributors. 
        > Emissions of non-CO2 greenhouse gases have also increased significantly since 1900."
    """)

    st.markdown("### Top CO₂ Emitters")
    # Set up the bar plot for top CO2-emitting countries in 2020
    plt.figure(figsize=(10, 5))
    top_emitters_2020 = df[df['Year'] == 2020].sort_values(by='CO2 emission (Tons)', ascending=False).head(30)
    sns.barplot(x='Country', y='CO2 emission (Tons)', data=top_emitters_2020)
    plt.xticks(rotation=90)
    plt.title("Top 30 CO₂ Emitting Countries in 2020")
    plt.xlabel("Country")
    plt.ylabel("CO₂ Emissions (Tons)")

    # Display the second plot in Streamlit
    st.pyplot(plt.gcf())
    
    # Write the conclusion for the top emitters
    st.markdown("""
        #### Key Insights: 
        
        - The United States and China stand out as the largest CO₂ emitters. The top 5 countries contribute approximately 57% of global emissions.
        - **Global Disparity**: The United States and China dominate emissions by a significant margin, reflective of their industrial capacity and large economies.
        - European countries like Germany and the UK, as well as Japan, show high emissions due to long-standing industrialization.
        - Developing economies, such as India, are emerging contributors to CO₂ emissions, reflecting their growing industrial activities.

        The chart underscores the importance of targeting emission reductions in large emitters while promoting sustainable growth in emerging economies.
    """)

    # Filter data for the top 5 CO2-emitting countries
    df_top5 = df[df['Country'].isin(['United States', 'China', 'Russia', 'Germany', 'United Kingdom'])]
    st.markdown("### CO₂ Emissions Trends for the Top 5 Countries")
    # Set up the line plot for top 5 CO2 emitting countries over time
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Year", y="CO2 emission (Tons)", 
                data=df_top5, hue="Country", style="Country", 
                markers=True, dashes=False)
    plt.title("CO₂ Emissions Over Time: Top 5 Countries")
    plt.xlabel("Year")
    plt.ylabel("CO₂ Emissions (Tons)")

    # Display the third plot in Streamlit
    st.pyplot(plt.gcf())

    # Write insights about the top 5 countries
    st.markdown("""
        ### Key Insights:
        
        - **United States Dominance (Pre-2000)**: The U.S. was the dominant CO₂ emitter throughout the 19th and 20th centuries, with emissions peaking post-World War II due to industrial expansion.
        - **China's Rapid Surge**: From the early 2000s, China's emissions have risen sharply, surpassing the U.S., and continuing to grow due to rapid industrialization.
        - **Germany and the United Kingdom**: Both countries have seen stable or declining emissions post-1980s, reflecting efforts in deindustrialization and emissions reduction policies.
        - **Russia**: Emissions have fluctuated but have not grown as sharply as the U.S. or China.
        - **Global Exponential Growth**: Emissions have grown exponentially since the 1950s, primarily due to industrialization and population growth.
    """)

    st.markdown("### Regional CO₂ Emissions")
    # Display the first image for regional comparisons
    st.image("continental comparision.png", caption="CO₂ Emissions by Region")

    # Write insights for regional comparison
    st.markdown("""
        ### Key Insights: 
        
        - High-income countries historically led global emissions but are now reducing their output.
        - Upper-middle-income countries, notably China, have become the primary source of global emissions, reflecting rapid industrialization.
        - Low-income countries contribute very little to emissions despite their population size, showing disparities in emissions across income groups.
    """)
    st.markdown("### CO₂ Emissions by Income Group")
    # Display the second image for income-based comparison
    st.image("income status comparision.png", caption="CO₂ Emissions by Income Group")

    # Write insights for income-based comparison
    st.markdown("""
        ### Key Insights: 
        
        - **Asia** is now the largest emitter of CO₂, with emissions accelerating post-1950 due to rapid economic growth.
        - **North America and Europe** were early leaders in emissions but have seen a decline due to energy transitions and policies.
        - **Africa and South America** contribute much less to global emissions, though their levels are slowly increasing.
        - The overall trend shows a significant rise in global emissions post-1950, with Asia taking a dominant role in recent decades.
    """)

# Call the function to run the analysis
if __name__ == "__main__":
    run_analysis()
