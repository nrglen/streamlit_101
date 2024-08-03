import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generar datos de ejemplo
np.random.seed(42)
dates = pd.date_range(datetime.today(), periods=100).tolist()
data = np.random.randn(100).cumsum()

df = pd.DataFrame({
    'Date': dates,
    'Value': data
})

# Configurar la aplicación de Streamlit
st.title('Aplicación de Streamlit con Plotly')

# Crear una layout con dos columnas
col1, col2 = st.columns(2)

# Primera columna con el gráfico de línea de tiempo
with col1:
    st.header('Gráfico de Línea de Tiempo')
    fig = px.line(df, x='Date', y='Value', title='Valor a lo Largo del Tiempo')
    st.plotly_chart(fig)

# Segunda columna con selector de datos y botón
with col2:
    st.header('Selector de Datos y Cálculo')

    # Selector de fecha
    selected_date = st.date_input('Selecciona una fecha', value=datetime.today())
    
    # Selector de valor
    selected_value = st.slider('Selecciona un valor', min_value=float(df['Value'].min()), max_value=float(df['Value'].max()), value=float(df['Value'].mean()))

    # Botón de cálculo
    if st.button('Calcular'):
        # Realizar algún cálculo con los datos seleccionados
        closest_date = min(dates, key=lambda d: abs(d - selected_date))
        closest_value = df[df['Date'] == closest_date]['Value'].values[0]
        st.write(f'Valor más cercano a la fecha seleccionada: {closest_value:.2f}')
        st.write(f'Valor seleccionado: {selected_value:.2f}')
        di
