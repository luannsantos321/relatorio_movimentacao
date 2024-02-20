import pandas as pd
import streamlit as st



mov_regional = pd.read_csv('Movimentação Regional.csv', low_memory=False)
mov_regional2 = mov_regional[['data_criacao_aceite_transacao', 'nome_item', 'deposito_destino_nome']]
    # Tratando data



def movimentacao_CD(mes, aparelho):

    mov_CD2 = mov_CD[['data_criacao_aceite_transacao', 'nome_item', 'deposito_destino_nome']]
    # Tratando data
    data_formatada = []
    for mov in mov_CD2['data_criacao_aceite_transacao']:
        stamp = pd.Timestamp(mov)
        data_formatada.append(f'{stamp.day}/{stamp.month}/{stamp.year}')
    mov_CD2['data_criacao_aceite_transacao'] = data_formatada
    # Escolhendo o mes
    contagem = []
    mes_exemplo = [f'{dia}/{mes}/2023' for dia in range(1, 32)]
    for i, data in enumerate(mov_CD2['data_criacao_aceite_transacao']):
        if data in mes_exemplo:
            contagem.append(mov_CD2.iloc[i, :])
    mes_selecionado = pd.DataFrame(contagem)
    # Pegando por aparelho
    try:
        lista_aparelho = []
        for i, item in enumerate(mes_selecionado['nome_item']):
            if aparelho in item:
                lista_aparelho.append(mes_selecionado.iloc[i, :])
        aparelho_selecionado = pd.DataFrame(lista_aparelho)

        # Agrupando pelo aparelho

        por_quantidade = aparelho_selecionado.value_counts()
        final = aparelho_selecionado.groupby('nome_item').sum()
        contados = pd.DataFrame(aparelho_selecionado.value_counts())
        # grafico = contados.groupby('nome_item').sum().plot.bar(xlabel='Nome dos aparelhos', ylabel='Quantidade Transicionada', grid=True,color='orange');
        return final

    except:
        print(f'Não houve transação {mes}')


st.title('Relatorio Movimentações')



with st.sidebar:
    selecionar = st.sidebar.selectbox('Selecionar', ('Regional', 'CD'))





if selecionar =='Regional':

    st.subheader('Regional')
    mov_regional = pd.read_csv('Formatado.csv')

    tabela = ''
    tabela2 = ''
    mes_select = st.selectbox('Selecionar mes', ('Escolha','9', '10', '11', '12', '01','02'))
    aparelho_select = st.selectbox('Selecionar aparelhos', ('ONU','Roteador','Setup Box'))
    if mes_select == 'Escolha':
        tabela = st.write('Bem vindo ao Regional. Filtre conforme os dados')

    elif mes_select == '9':
        try:
            item = pd.read_csv(f'CSV para streamlit/Regional/Regional{mes_select} - {aparelho_select}.csv')
            valor = pd.read_csv(f'CSV para streamlit/Regional/Numeros{mes_select} Regionais {aparelho_select}.csv')
            tabela2 = st.write(valor)
            tabela = st.write(item)
        except:
            st.write('Erro...')
    elif mes_select == '10':
        try:
            item = pd.read_csv(f'CSV para streamlit/Regional/Regional{mes_select} - {aparelho_select}.csv')
            valor = pd.read_csv(f'CSV para streamlit/Regional/Numeros{mes_select} Regionais {aparelho_select}.csv')
            tabela2 = st.write(valor)
            tabela = st.write(item)
        except:
            st.write('Erro...')

    elif mes_select == '11':
        try:
            item = pd.read_csv(f'CSV para streamlit/Regional/Regional{mes_select} - {aparelho_select}.csv')
            valor = pd.read_csv(f'CSV para streamlit/Regional/Numeros{mes_select} Regionais {aparelho_select}.csv')
            tabela2 = st.write(valor)
            tabela = st.write(item)
        except:
            st.write('Erro...')

    elif mes_select == '12':
        try:
            item = pd.read_csv(f'CSV para streamlit/Regional/Regional{mes_select} - {aparelho_select}.csv')
            valor = pd.read_csv(f'CSV para streamlit/Regional/Numeros{mes_select} Regionais {aparelho_select}.csv')
            tabela2 = st.write(valor)
            tabela = st.write(item)
        except:
            st.write('Erro...')

    elif mes_select == '01':
        try:
            item = pd.read_csv(f'CSV para streamlit/Regional/Regional{mes_select} - {aparelho_select}.csv')
            valor = pd.read_csv(f'CSV para streamlit/Regional/Numeros{mes_select} Regionais {aparelho_select}.csv')
            tabela2 = st.write(valor)
            tabela = st.write(item)
        except:
            st.write('Erro...')

    elif mes_select == '02':
        try:
            item = pd.read_csv(f'CSV para streamlit/Regional/Regional{mes_select} - {aparelho_select}.csv')
            valor = pd.read_csv(f'CSV para streamlit/Regional/Numeros{mes_select} Regionais {aparelho_select}.csv')
            tabela2 = st.write(valor)
            tabela = st.write(item)
        except:
            st.write('Erro...')

if selecionar =='CD':

    st.subheader('CD')
    mov_regional = pd.read_csv('Formatado.csv')

    tabela = ''
    tabela2 = ''
    mes_select = st.selectbox('Selecionar mes', ('Escolha','9', '10', '11', '12', '01','02'))
    aparelho_select = st.selectbox('Selecionar aparelhos', ('ONU','Roteador','Setup Box'))
    if mes_select == 'Escolha':
        tabela = st.write('Bem vindo ao Regional. Filtre conforme os dados')

    elif mes_select == '9':
        try:
            item = pd.read_csv(f'CSV para streamlit/CD/CD{mes_select} - {aparelho_select}.csv')
            valor = pd.read_csv(f'CSV para streamlit/CD/Numeros{mes_select} CD {aparelho_select}.csv')
            tabela2 = st.write(valor)
            tabela = st.write(item)
        except:
            st.write('Erro...')
    elif mes_select == '10':
        try:
            item = pd.read_csv(f'CSV para streamlit/CD/CD{mes_select} - {aparelho_select}.csv')
            valor = pd.read_csv(f'CSV para streamlit/CD/Numeros{mes_select} CD {aparelho_select}.csv')
            tabela2 = st.write(valor)
            tabela = st.write(item)
        except:
            st.write('Erro...')

    elif mes_select == '11':
        try:
            item = pd.read_csv(f'CSV para streamlit/CD/CD{mes_select} - {aparelho_select}.csv')
            valor = pd.read_csv(f'CSV para streamlit/CD/Numeros{mes_select} CD {aparelho_select}.csv')
            tabela2 = st.write(valor)
            tabela = st.write(item)
        except:
            st.write('Erro...')

    elif mes_select == '12':
        try:
            item = pd.read_csv(f'CSV para streamlit/CD/CD{mes_select} - {aparelho_select}.csv')
            valor = pd.read_csv(f'CSV para streamlit/CD/Numeros{mes_select} CD {aparelho_select}.csv')
            tabela2 = st.write(valor)
            tabela = st.write(item)
        except:
            st.write('Erro...')

    elif mes_select == '01':
        try:
            item = pd.read_csv(f'CSV para streamlit/CD/CD{mes_select} - {aparelho_select}.csv')
            valor = pd.read_csv(f'CSV para streamlit/CD/Numeros{mes_select} CD {aparelho_select}.csv')
            tabela2 = st.write(valor)
            tabela = st.write(item)
        except:
            st.write('Erro...')

    elif mes_select == '02':
        try:
            item = pd.read_csv(f'CSV para streamlit/CD/CD{mes_select} - {aparelho_select}.csv')
            valor = pd.read_csv(f'CSV para streamlit/CD/Numeros{mes_select} CD {aparelho_select}.csv')
            tabela2 = st.write(valor)
            tabela = st.write(item)
        except:
            st.write('Erro...')
