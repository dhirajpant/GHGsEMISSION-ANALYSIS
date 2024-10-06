import streamlit as st

def show_conclusion():
    st.header("Conclusions from CO₂ Emissions and Temperature Anomalies Analysis")

    st.write("""
        The analysis of CO₂ emissions and temperature anomalies provides critical insights into the relationship 
        between human activity and global warming. This section synthesizes the key findings from the Analysis 
        section and discusses the broader implications for climate policy, sustainability, and the urgent need for action 
        to mitigate the impact of greenhouse gas emissions.
    """)

    # Key Findings
    st.subheader("Key Findings")
    
    st.write("""
        1. **CO₂ Emissions Trends**: 
           The global rise in CO₂ emissions has been particularly rapid since 1900, with a significant 90% increase 
           since 1970, largely driven by fossil fuel combustion and industrial activities. This points to the 
           ongoing and growing challenge of curbing emissions despite international efforts.

        2. **Country Contributions**: 
           The United States and China stand out as the largest cumulative contributors to CO₂ emissions, 
           with the top 5 emitting countries contributing approximately 57% of global emissions. This emphasizes 
           the critical role of these countries in global mitigation efforts.

        3. **Temperature Anomalies**: 
           The analysis of temperature anomalies reveals that global temperatures have been rising significantly 
           compared to historical averages. Regions with higher emissions have seen greater temperature deviations, 
           further solidifying the link between greenhouse gas emissions and global warming.

        4. **Regional Disparities**: 
           While CO₂ emissions and temperature anomalies have risen globally, the impacts are not evenly distributed. 
           Some regions are experiencing more severe temperature shifts, particularly in the Arctic and mid-latitude regions, 
           where warming has outpaced the global average.

        5. **Historical Emissions Surge**: 
           U.S. emissions surged in the early 1900s, coinciding with rapid industrialization, while China's emissions 
           accelerated in the late 1900s, driven by economic expansion. This underscores the historical responsibility 
           and the evolving landscape of emissions over time.

        6. **Non-CO₂ Greenhouse Gases**: 
           Though this analysis focused on CO₂, non-CO₂ gases like methane and nitrous oxide have also contributed 
           significantly to global warming, and their role should not be underestimated in future policy discussions.
    """)

    # Implications and Recommendations
    st.subheader("Implications and Recommendations")

    st.write("""
        The findings from this analysis highlight the urgent need for global action to address CO₂ emissions and 
        limit temperature increases. Several strategies can be employed to mitigate emissions and their impacts:

        - **Strengthened International Collaboration**: 
          Global cooperation is crucial, particularly among the largest emitters. International agreements, such as 
          the Paris Agreement, must be strengthened, with countries committing to more ambitious emission reduction targets.

        - **Investment in Clean Energy**: 
          A transition away from fossil fuels toward renewable energy sources like solar, wind, and hydropower is 
          essential to reduce CO₂ emissions. Investments in green technologies can facilitate this transition 
          and drive economic growth.

        - **Carbon Pricing and Emission Reduction Policies**: 
          Implementing carbon pricing mechanisms, such as carbon taxes or cap-and-trade systems, can incentivize 
          businesses and industries to lower their emissions. Policy reforms targeting high-emission sectors 
          like transportation and manufacturing are essential.

        - **Public Awareness and Behavioral Change**: 
          Raising public awareness of the impacts of CO₂ emissions and encouraging sustainable lifestyle choices 
          can help reduce individual and collective carbon footprints. Education campaigns are key in driving 
          climate-friendly behavior.

        - **Adaptation and Resilience**: 
          As global warming continues, it is essential to invest in climate adaptation strategies to enhance 
          resilience, particularly in vulnerable regions. This includes infrastructure improvements, 
          water resource management, and disaster preparedness.

    """)

    # Conclusion
    st.subheader("Conclusion")

    st.write("""
        In conclusion, the analysis of global CO₂ emissions and temperature anomalies underscores the gravity 
        of the climate crisis. The findings confirm the link between human activities and rising global temperatures, 
        stressing the need for immediate and decisive action. 

        This dashboard serves as a comprehensive tool for understanding emission trends and their impacts, offering 
        valuable insights for researchers, policymakers, and the public. By fostering collaboration and informed decision-making, 
        we can work towards a sustainable future and limit the worst impacts of climate change.

        We hope this analysis empowers you to take part in the global effort to reduce emissions and promote climate resilience.
    """)
