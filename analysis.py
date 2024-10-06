import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_analysis():
    # Load the dataset
    file_path = 'new_CIT-2023-ch4-upwind-1-hour-20240513.csv'  # Adjust the path as needed
    data = pd.read_csv(file_path)

    # Convert 'datetime_UTC' to datetime format
    data['datetime_UTC'] = pd.to_datetime(data['datetime_UTC'])

    # -------------------------------------
    # 1. Trend Analysis Over Time
    st.subheader("Trend Analysis Over Time")
    plt.figure(figsize=(14, 6))
    plt.plot(data['datetime_UTC'], data['ch4_ppb'], color='blue', label='CH₄ Levels (ppb)')
    plt.title('Trend of CH₄ Levels in 2023')
    plt.xlabel('Date')
    plt.ylabel('CH₄ Levels (ppb)')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(plt)

    # -------------------------------------
    # 2. Diurnal Patterns (Hourly Variations)
    st.subheader("Diurnal Patterns (Hourly Variations)")
    data['hour'] = data['datetime_UTC'].dt.hour  # Extract hour from datetime
    hourly_means = data.groupby('hour')['ch4_ppb'].mean()  # Calculate hourly mean
    plt.figure(figsize=(10, 5))
    plt.plot(hourly_means.index, hourly_means.values, marker='o', color='orange')
    plt.title('Average CH₄ Levels by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Average CH₄ Levels (ppb)')
    plt.xticks(hourly_means.index)
    st.pyplot(plt)

    # -------------------------------------
    # 3. Day of Week / Month Analysis
    st.subheader("Day of Week Analysis")
    data['day_of_week'] = data['datetime_UTC'].dt.day_name()  # Extract day of week
    weekly_means = data.groupby('day_of_week')['ch4_ppb'].mean()  # Calculate mean by day
    order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    plt.figure(figsize=(10, 5))
    sns.barplot(x=weekly_means.index, y=weekly_means.values, order=order, palette='pastel')
    plt.title('Average CH₄ Levels by Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Average CH₄ Levels (ppb)')
    st.pyplot(plt)

    # Monthly Analysis
    data['month'] = data['datetime_UTC'].dt.month_name()  # Extract month name
    monthly_means = data.groupby('month')['ch4_ppb'].mean()  # Calculate mean by month
    plt.figure(figsize=(10, 5))
    monthly_means = monthly_means.reindex(['January', 'February', 'March', 'April', 'May', 
                                            'June', 'July', 'August', 'September', 
                                            'October', 'November', 'December'])  # Order months
    sns.barplot(x=monthly_means.index, y=monthly_means.values, palette='pastel')
    plt.title('Average CH₄ Levels by Month')
    plt.xlabel('Month')
    plt.ylabel('Average CH₄ Levels (ppb)')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # -------------------------------------
    # 4. Distribution of Methane Concentration
    st.subheader("Distribution of Methane Concentration")
    plt.figure(figsize=(8, 5))
    plt.hist(data['ch4_ppb'], bins=30, color='purple', alpha=0.7)
    plt.title('Histogram of CH₄ Levels (ppb)')
    plt.xlabel('CH₄ Levels (ppb)')
    plt.ylabel('Frequency')
    st.pyplot(plt)

    # -------------------------------------
    # 5. Uncertainty and Variability
    st.subheader("Uncertainty and Variability")
    plt.figure(figsize=(10, 5))
    plt.errorbar(data['datetime_UTC'], data['ch4_ppb'], yerr=data['ch4_uncertainty'], fmt='o', ecolor='red', alpha=0.5)
    plt.title('CH₄ Levels with Uncertainty')
    plt.xlabel('Date')
    plt.ylabel('CH₄ Levels (ppb)')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # -------------------------------------
    # 6. Correlation Analysis
    st.subheader("Correlation Analysis")
    correlation_matrix = data[['ch4_ppb', 'ch4_uncertainty', 'ch4_SD_raw', 'ch4_n_raw']].corr()
    # Plot heatmap
    plt.figure(figsize=(10,8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap of Methane Data')
    st.pyplot(plt)  # Change plt.show() to st.pyplot(plt)

# Call the function to run the analysis
if __name__ == "__main__":
    run_analysis()
