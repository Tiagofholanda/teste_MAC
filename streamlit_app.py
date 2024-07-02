import streamlit as st
import pandas as pd

st.title('Verificação de inconsistências lógicas em banco de dados')

st.write('Os códigos a seguir são uma adaptação para Python dos códigos originalmente escritos em VBA para detecção de inconsistências lógicas em bancos de dados de pesquisas cadastrais.')
st.write('Bibliotecas utilizadas: pandas, openpyxl')

uploaded_file1 = st.file_uploader("Escolha o arquivo do Banco de Dados", type=["xlsx"])
uploaded_file2 = st.file_uploader("Escolha o arquivo da Matriz", type=["xlsx"])
uploaded_file3 = st.file_uploader("Escolha o arquivo dos Intervalos", type=["xlsx"])
uploaded_file4 = st.file_uploader("Escolha o arquivo dos Nomes", type=["xlsx"])

if uploaded_file1 and uploaded_file2 and uploaded_file3 and uploaded_file4:
    try:
        # Carregar os arquivos Excel em DataFrames
        df_bd = pd.read_excel(uploaded_file1)
        df_matriz = pd.read_excel(uploaded_file2, header=1)
        df_intervalos = pd.read_excel(uploaded_file3)
        df_nomes = pd.read_excel(uploaded_file4)

        st.write("Banco de Dados:")
        st.dataframe(df_bd.head())

        st.write("Matriz:")
        st.dataframe(df_matriz.head())

        st.write("Intervalos:")
        st.dataframe(df_intervalos.head())

        st.write("Nomes:")
        st.dataframe(df_nomes.head())
    except Exception as e:
        st.error(f"Erro ao carregar os arquivos: {e}")
else:
    st.write("Por favor, carregue todos os arquivos para iniciar a validação.")

