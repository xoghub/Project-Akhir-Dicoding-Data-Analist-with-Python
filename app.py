import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hour = pd.read_csv("hour.csv")
day = pd.read_csv("day.csv")

st.title('Dashboard Project Analisis Data Bike Share')

st.header('Apakah cuaca dan musim mempengaruhi jumlah penyewa sepeda?')
st.subheader('Musim dengan Jumlah Penyewa Sepeda')
season_data = day.groupby(by='season')['cnt'].mean()
season_labels = ['Spring', 'Summer', 'Fall', 'Winter']
fig_bar_season_daily = plt.figure(figsize=(12, 6))
plt.bar(x=season_labels, height=season_data)
plt.xlabel('Season')
plt.ylabel('Mean of Bike Share')
plt.title('The Effect of Seasonality on the Number of Bike Share')
st.pyplot(fig_bar_season_daily)

month_data_day = day.groupby(by='mnth')['cnt'].mean()
fig_bar_month_daily = plt.figure(figsize=(12, 6))
plt.plot(month_data_day)
plt.xlabel('Month', size=15)
plt.ylabel('Mean of Bike Share', size=15)
st.pyplot(fig_bar_month_daily)

season_data = day.groupby(by='season')['temp'].mean()
season_labels = ['Spring', 'Summer', 'Fall', 'Winter']
fig_bar_season_temp_daily = plt.figure(figsize=(12, 6))
plt.bar(x=season_labels, height=season_data)
plt.xlabel('Season')
plt.ylabel('Mean of Temperature')
plt.title('The Temperature on Season')
st.pyplot(fig_bar_season_temp_daily)

st.markdown("""
Musim sangat mempengaruhi jumlah penyewa sepeda. Hal ini diperkuat dengan peningkatan jumlah penyewa pada musim summer dan fall dibandingkan spring dan winter. Selain hal itu, pada musim summer dan fall memiliki temperature yang cukup tinggi dibandingkan spring dan winter yang dapat mempengaruhi kenyamanan penyewa dalam mengendarai sepedanya.

Hal ini pun mempengaruhi jumlah penyewa per bulannya yang menyesuaikan berdasarkan musimnya.
""")

st.subheader('Cuaca dengan Jumlah Penyewa Sepeda')
wathersit_data_daily = day.groupby(by='weathersit')['cnt'].mean()
weathersit_labels = ['Clear', 'Mist and Cloudy', 'Light Snow']
fig_bar_wathersit_daily = plt.figure(figsize=(12, 6))
plt.bar(x=weathersit_labels, height=wathersit_data_daily)
plt.xlabel('Wathersit')
plt.ylabel('Mean of Bike Share')
plt.title('The Effect of Wathersit on the Number of Bike Share on Daily')
st.pyplot(fig_bar_wathersit_daily)

wathersit_data_hour = hour.groupby(by='weathersit')['cnt'].mean()
weathersit_labels = ['Clear', 'Mist and Cloudy', 'Light Snow', 'Heavy Rain']
fig_bar_wathersit_hour = plt.figure(figsize=(12, 6))
plt.bar(x=weathersit_labels, height=wathersit_data_hour)
plt.xlabel('Wathersit')
plt.ylabel('Mean of Bike Share')
plt.title('The Effect of Wathersit on the Number of Bike Share on Hours')
st.pyplot(fig_bar_wathersit_hour)

st.markdown("Cuaca juga memiliki pengaruh yang cukup signifikan terhadap jumlah penyewa yang dimana penyewa lebih memilih menyewa sepeda pada cuaca yang cukup terang (clear) dibandingkan hujan lebat atau bersalju yang cukup ringan.")

st.header('Apakah hari dan kerja mempengaruhi jumlah penyewa sepeda?')

st.text('Jumlah Rata Penyewa Sepeda Setiap harinya')
weekday_data_hour = hour.groupby(by='weekday')['cnt'].mean()
weekday_labels = ['Sunday', 'Monday', 'Tuesday', 'Wendesday', 'Thursday', 'Friday', 'Saturday']
fig_bar_weekday_hour = plt.figure(figsize=(12, 6))
plt.bar(x=weathersit_labels, height=wathersit_data_hour)
plt.xticks(rotation=45)
plt.xlabel('Weekday')
plt.ylabel('Mean of Bike Share')
plt.title('Number of Bike Share Every Day')
st.pyplot(fig_bar_weekday_hour)

st.text('Jumlah Rata Penyewa Sepeda Pada Hari Kerja')
workingday_data_hour = hour.groupby(by='workingday')['cnt'].sum()
workingday_labels = ['Not', 'Yes']
fig_bar_workingday_hour = plt.figure(figsize=(12, 6))
plt.bar(x=workingday_labels, height=workingday_data_hour)
plt.xlabel('Working Day')
plt.ylabel('Mean of Bike Share')
plt.title('Number of Bike Share on Working Day')
st.pyplot(fig_bar_workingday_hour)

st.text('Jumlah Rata Penyewa Sepeda Berdasarkan Jam')
hour_data = hour.groupby(by='hr')['cnt'].sum()
fig_hour_data = plt.figure(figsize=(12, 6))
plt.plot(hour_data)
plt.xlabel('Hour', size=15)
plt.ylabel('Mean of Bike Share', size=15)
plt.title('Mean of Bike Share Based on Hour')
st.pyplot(fig_hour_data)

st.markdown("Hari kerja pula mempengaruhi jumlah penyewa secara keseluruhan dimana hal ini dipertegas oleh kecenderungan orang menyewa pada pukul 8 pagi hingga 10 pagi yang merupkan pukul keberangkatan orang berangkat ke tempat kerja, dan pada pukul 16 sore hingga 20 malam yang merupakan pukul kepulangan orang dari tempat kerja.")

