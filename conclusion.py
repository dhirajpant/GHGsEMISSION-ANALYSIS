import streamlit as st

def show_conclusion():
    st.header("Conclusions and Timeline of Global CO₂ Emissions")

    st.write("""
        This section provides a comprehensive look at CO₂ emissions over time and highlights key findings from our analysis. 
        It also showcases ongoing efforts to reduce emissions globally, connecting historical events with actionable insights 
        for today’s climate challenges.
    """)

    # Timeline of CO₂ Emissions and Global Climate Action
    st.subheader("Timeline of CO₂ Emissions and Global Climate Action")

    timeline = [
        {
        "date": "Early 1800s",
        "event": "The Start of Industrialization",
        "description": "The Industrial Revolution begins, fueled by the widespread use of coal and steam power in factories and transportation.",
        "impact": "CO₂ emissions start to rise, marking the beginning of the world’s increasing reliance on fossil fuels for energy production."
        },
        {
        "date": "Early 1900s",
        "event": "Accelerated Industrial Growth in Developed Countries",
        "description": "The U.S. and parts of Europe experience rapid industrialization, with widespread automobile use and electric power grids being developed.",
        "impact": "The U.S. sees a rapid increase in its cumulative CO₂ emissions, becoming one of the largest contributors globally."
        },
        {
        "date": "1950s",
        "event": "The Start of Global Awareness",
        "description": "After World War II, global industrial production surges. Scientists begin to notice rising levels of CO₂ in the atmosphere.",
        "impact": "CO₂ emissions accelerate globally, raising concerns about air pollution and environmental damage."
        },
        {
        "date": "1970s",
        "event": "The Environmental Movement",
        "description": "The environmental movement begins, focusing on the harmful effects of pollution and fossil fuels. The first Earth Day is celebrated in 1970.",
        "impact": "Global awareness grows, but emissions continue to rise, especially in emerging economies."
        },
        {
        "date": "1992",
        "event": "The First Global Climate Agreement",
        "description": "The Earth Summit is held in Rio de Janeiro, leading to the creation of the UNFCCC to stabilize greenhouse gas concentrations.",
        "impact": "Countries agree to work together, but binding targets are not yet established."
        },
        {
        "date": "Late 1990s",
        "event": "China’s Emissions Surge",
        "description": "China experiences massive economic growth and industrialization, rapidly increasing CO₂ emissions.",
        "impact": "China becomes one of the largest contributors to global emissions."
        },
        {
        "date": "2005",
        "event": "The Kyoto Protocol",
        "description": "The Kyoto Protocol goes into effect, setting legally binding targets for developed countries to reduce greenhouse gas emissions.",
        "impact": "Some countries begin adopting cleaner energy practices, but emissions continue to rise."
        },
        {
        "date": "2015",
        "event": "The Paris Agreement",
        "description": "The Paris Agreement is adopted by nearly every country to limit global warming to well below 2°C.",
        "impact": "Countries commit to reducing CO₂ emissions and transitioning to renewable energy sources."
        },
        {
        "date": "Present (2023–2024)",
        "event": "Increasing Global Efforts",
        "description": "Global CO₂ emissions are still rising, but some regions have made significant progress in reducing their emissions.",
        "impact": "Ongoing practices include carbon taxes, net-zero goals, and increased use of green technologies."
        },
        {
        "date": "Future",
        "event": "What Needs to Happen Next",
        "description": "To keep global warming below 1.5°C, emissions need to reach net zero by mid-century (2050).",
        "impact": "Continued reduction of reliance on fossil fuels and increased reforestation efforts are critical."
        }
    ]

    for entry in timeline:
        st.write(f"**{entry['date']}**: {entry['event']}")
        st.write(f"- **Description**: {entry['description']}")
        st.write(f"- **Impact**: {entry['impact']}")
        st.write("")

    # Key Findings
    st.subheader("Key Findings from Analysis")

    st.write("""
        1. **Cumulative CO₂ Emissions**: Since 1970, global carbon emissions from fossil fuels have increased by about 90%. 
        The significant rise is largely due to fossil fuel combustion and industrial processes, which account for approximately 78% of this increase. 
        This finding emphasizes the impact of industrial activities on climate change.

        2. **Major Contributors**: The United States and China are identified as the largest contributors to global CO₂ emissions, 
        with the top five countries collectively accounting for around 57% of total emissions. 
        This highlights the necessity of targeting these major emitters in climate policy discussions.

        3. **Population vs. Emissions**: Despite having only 16% of the global population, high-income countries are responsible for 38% 
        of global CO₂ emissions. In contrast, low-income countries, which make up about 9% of the population, contribute a mere 0.5%. 
        This disparity raises important questions about equity in climate responsibilities.

        4. **Trends in Emissions**: Historical data shows that U.S. CO₂ emissions began to rise sharply in the early 1900s, 
        while China's emissions have surged since the late 1900s, reflecting rapid industrialization. 
        This trend underscores the shift in emission sources over time.

        5. **Ongoing Efforts**: Global initiatives like the Paris Agreement aim to reduce emissions and foster cooperation among nations. 
        Many countries are committing to cleaner energy practices and technologies, indicating a growing recognition of the need for sustainable development.
    """)

    # Conclusion
    st.subheader("Conclusion")

    st.write("""
        In conclusion, the timeline analysis illustrates that while global CO₂ emissions have increased dramatically over the last century, 
        efforts are underway to reduce them. This highlights the urgent need for collective action from all sectors of society. 

        Through collaboration, innovation, and commitment to sustainable practices, we can slow down global warming and protect our planet 
        for future generations. By supporting renewable energy, reducing consumption, and advocating for strong climate policies, 
        we can all play a role in solving this global crisis.

        Our analysis aims to provide clarity and insights into the dynamics of CO₂ emissions, paving the way for informed decisions 
        and actions toward a more sustainable future.
    """)

# Call the function to run the analysis in the Streamlit app
if __name__ == "__main__":
    show_conclusion()
