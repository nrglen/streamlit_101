import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Mi Aplicación con Visualización de Datos')

# Generar datos de ejemplo
data = np.random.randn(100, 3)
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Mostrar datos en una tabla
st.write('Datos de ejemplo:')
st.write(df.head())

# Visualización
st.write('Gráfico de dispersión de los datos:')
fig, ax = plt.subplots()
ax.scatter(df['A'], df['B'])
st.pyplot(fig)
