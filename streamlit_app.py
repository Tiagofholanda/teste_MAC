import streamlit as st
import pandas as pd

# Função para análise de preenchimento
def AnalisePreenchimento(df_bd, df_matriz):
    resultado = []

    for coluna in range(1, len(df_matriz.columns)):  # Itera sobre as colunas da matriz
        texto = df_matriz.columns[coluna]  # Obtém o nome da coluna na matriz
        regra = df_matriz.iloc[4, coluna]  # Obtém a regra correspondente na linha 4 da matriz

        if texto in df_bd.columns:
            for linha in range(len(df_bd)):
                valor_celula = df_bd.loc[linha, texto]

                if (regra == "OBRIGATÓRIO" and pd.isna(valor_celula)) or (regra == "VAZIO" and not pd.isna(valor_celula)):
                    motivo = "Preenchimento obrigatório" if regra == "OBRIGATÓRIO" else "Sem preenchimento"
                    resultado.append({
                        'Data_Hora': pd.Timestamp.now(),
                        'Linha': linha+1,
                        'Coluna': texto,
                        'Motivo': motivo,
                        'Regra': regra,
                    })

    resultado = pd.DataFrame(resultado)
    return resultado

# Título do aplicativo
st.title('Análise de Preenchimento de Dados')

# Upload dos arquivos Excel
arquivo_bd = st.file_uploader('Upload do arquivo Excel do banco de dados (.xlsx)', type='xlsx')
arquivo_matriz = st.file_uploader('Upload do arquivo Excel da matriz (.xlsx)', type='xlsx')

# Botão para iniciar análise
if st.button('Iniciar Análise'):

    if arquivo_bd is not None and arquivo_matriz is not None:
        try:
            # Carregar arquivos Excel para DataFrames do pandas
            df_bd = pd.read_excel(arquivo_bd)
            df_matriz = pd.read_excel(arquivo_matriz, header=1)

            # Realizar análise de preenchimento
            resultado_analise = AnalisePreenchimento(df_bd, df_matriz)

            # Criar DataFrame com resultado da análise
            preenchimento = pd.DataFrame(resultado_analise)

            # Exibir resultado da análise
            st.write("\nResultado da Análise:")
            st.write(preenchimento.head())  # Exibir os primeiros registros do DataFrame de preenchimento

        except Exception as e:
            st.warning(f"Erro ao processar os arquivos: {e}")

    else:
        st.warning("Por favor, faça o upload de ambos os arquivos para iniciar a análise.")
