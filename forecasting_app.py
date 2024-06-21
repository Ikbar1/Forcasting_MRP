import streamlit as st
import pandas as pd
import numpy as np

# Data penjualan
data = {
    'Tahun': [1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004],
    'Penjualan': [500, 365, 430, 489, 389, 375, 400, 326, 368, 411, 338]
}

df = pd.DataFrame(data)

# Fungsi untuk menghitung SMA
def calculate_sma(data, period):
    return data.rolling(window=period).mean()

# Fungsi untuk menghitung WMA
def calculate_wma(data, weights):
    return data.rolling(window=len(weights)).apply(lambda x: np.dot(x, weights), raw=True)

# Streamlit UI
st.title('Aplikasi Forecasting dengan SMA dan WMA')
st.write('Data Penjualan PT. X')

st.dataframe(df)

# Input periode untuk SMA
period = st.number_input('Masukkan periode untuk SMA', min_value=1, max_value=len(df), value=4)

# Hitung SMA
df['SMA'] = calculate_sma(df['Penjualan'], period)

# Input bobot untuk WMA
weights_input = st.text_input('Masukkan bobot untuk WMA (pisahkan dengan koma)', '0.1,0.2,0.3,0.4')
weights = np.array([float(x) for x in weights_input.split(',')])

# Hitung WMA
df['WMA'] = calculate_wma(df['Penjualan'], weights)

# Tampilkan hasil peramalan
st.write('Hasil Peramalan')
st.dataframe(df)

# Menghitung MAE dan MSE untuk SMA
df['Error_SMA'] = abs(df['Penjualan'] - df['SMA'])
mae_sma = df['Error_SMA'].mean()
df['Error_SMA_squared'] = df['Error_SMA']**2
mse_sma = df['Error_SMA_squared'].mean()

st.write(f"MAE SMA: {mae_sma}")
st.write(f"MSE SMA: {mse_sma}")

# Menghitung MAE dan MSE untuk WMA
df['Error_WMA'] = abs(df['Penjualan'] - df['WMA'])
mae_wma = df['Error_WMA'].mean()
df['Error_WMA_squared'] = df['Error_WMA']**2
mse_wma = df['Error_WMA_squared'].mean()

st.write(f"MAE WMA: {mae_wma}")
st.write(f"MSE WMA: {mse_wma}")

# Menambahkan footer dengan teks di tengah
st.markdown("***")
footer = """
<div style='text-align: center;'>
    <p><b>NIM dan Nama Lengkap Kelompok:</b></p>
    <p><b>21108001</b>: FIRMANSYAH</p>
    <p><b>21120008</b>: FIRRAH AZHARA</p>
    <p><b>23170006</b>: AZHAR RAVI FALAH</p>
    <p><b>23170007</b>: ASYAM IKBAR ARIYANTO</p>
    <p><b>23170009</b>: RANU RAMADHAN</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
