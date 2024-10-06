import streamlit as st

def show_conclusion():
    st.header("Conclusions from Methane Analysis")

    st.write("""
        The analysis of methane (CH₄) levels collected in 2023 from a monitoring station in Pasadena, California, 
        provides valuable insights into the temporal dynamics and variability of methane concentrations. 
        This section synthesizes the key findings from the visualizations presented in the Analysis section 
        and discusses their implications in the context of environmental monitoring and climate change.
    """)

    # Key Findings
    st.subheader("Key Findings")
    
    st.write("""
        1. **Trend Analysis**: 
           The time series analysis revealed a fluctuating trend in CH₄ levels throughout the year. 
           Peaks in concentration were observed during specific months, suggesting potential seasonal influences 
           or episodic events contributing to elevated methane emissions. This highlights the importance 
           of continuous monitoring to identify significant changes in atmospheric methane levels.

        2. **Diurnal Patterns**: 
           The analysis of hourly variations indicated pronounced diurnal patterns in methane concentrations. 
           Average CH₄ levels peaked during specific hours of the day, likely correlating with human activities 
           such as traffic and industrial operations. Understanding these patterns can inform targeted mitigation strategies 
           to minimize emissions during peak times.

        3. **Day of Week and Month Variability**: 
           The analysis by day of the week revealed that CH₄ levels tended to be higher on weekdays compared to weekends. 
           This finding may reflect increased industrial and vehicular activities during the workweek. Additionally, 
           the monthly analysis pointed to certain months exhibiting higher average concentrations, 
           potentially linked to environmental factors such as temperature and precipitation patterns. 

        4. **Distribution of Methane Concentration**: 
           The histogram of CH₄ levels illustrated a right-skewed distribution, indicating that while most measurements 
           are concentrated at lower levels, there are occasional spikes of significantly higher concentrations. 
           Identifying and understanding the sources of these outliers is crucial for effective emissions management.

        5. **Uncertainty and Variability**: 
           The analysis of measurement uncertainty indicated variability in the data that can influence the interpretation 
           of CH₄ levels. It is essential to account for these uncertainties in scientific assessments and policy-making, 
           ensuring that decisions are based on the most reliable data available.

        6. **Correlation Analysis**: 
           The correlation matrix revealed relationships between CH₄ levels and other measured variables. 
           Understanding these correlations can help identify factors contributing to methane emissions and 
           guide further research into emission sources and trends.
    """)

    # Implications and Recommendations
    st.subheader("Implications and Recommendations")

    st.write("""
        The insights gained from this analysis underscore the need for ongoing monitoring and research into methane emissions. 
        As methane is a potent greenhouse gas with significant implications for climate change, understanding its 
        atmospheric dynamics is critical. The following recommendations can help improve future monitoring efforts:

        - **Enhanced Monitoring**: 
          Continued and expanded monitoring of methane levels across different locations and times can provide a more 
          comprehensive understanding of emissions sources and trends. Implementing real-time monitoring systems 
          could facilitate quicker responses to anomalous spikes in methane concentrations.

        - **Data Integration**: 
          Integrating methane data with meteorological and traffic data can enhance the analysis, providing insights 
          into how environmental factors influence CH₄ levels. This integrated approach can improve the accuracy of predictive models.

        - **Community Awareness and Engagement**: 
          Engaging local communities and industries in methane monitoring initiatives can promote awareness of emission sources 
          and encourage practices that reduce methane emissions. Educational programs can be developed to inform 
          the public about the impacts of methane on air quality and climate change.

        - **Policy Development**: 
          The findings from methane analyses should inform policymakers in developing regulations aimed at reducing emissions. 
          Policies that promote cleaner technologies and practices, particularly in high-emission industries, are vital for addressing methane emissions.

        - **Future Research**: 
          Future research should focus on understanding the underlying causes of methane concentration spikes, 
          including potential sources and mitigation strategies. Investigating the impact of weather patterns 
          on methane levels could also provide valuable insights into managing emissions during specific conditions.

    """)

    # Conclusion
    st.subheader("Conclusion")

    st.write("""
        In conclusion, the analysis of methane data collected in Pasadena, California, highlights the complex nature 
        of methane emissions and their variability over time. As climate change continues to pose significant threats 
        to our environment, understanding and addressing methane emissions is crucial. 

        This dashboard serves as a valuable tool for researchers, policymakers, and the community to engage with 
        methane data and its implications. By fostering collaboration and knowledge-sharing, we can work together 
        to develop effective strategies for mitigating methane emissions and their impacts on climate change.

        We hope this analysis has provided clarity and insights into methane dynamics, paving the way for 
        informed decisions and actions toward a more sustainable future.
    """)

