import streamlit as st
import pandas as pd
import plotly.express as px

# Título do aplicativo
st.header("Análise de Anúncios de Veículos")

# Ler os dados
car_data = pd.read_csv("vehicles.csv")

# Botão para histograma
if st.button("Criar histograma"):
    st.write("Histograma da quilometragem (odometer)")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botão para gráfico de dispersão
if st.button("Criar gráfico de dispersão"):
    st.write("Preço x Quilometragem")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)