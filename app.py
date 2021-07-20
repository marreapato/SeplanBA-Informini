#STREAMLIT TESTE https://towardsdatascience.com/build-your-first-data-visualization-web-app-in-python-using-streamlit-37e4c83a85db

import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
import openpyxl


#streamlit run C:\Users\atsilva\Desktop\app.py

########################################################################

# Processamento Dados

#lendo excel sem queries
ba = pd.ExcelFile("https://github.com/marreapato/SeplanBA-Informini/blob/main/Indicadores%20para%20pente%20fino_29-06-2021.xlsx/?raw=True",engine="openpyxl")

#indicadores:
#ciencia e tecnologia
ct=pd.read_excel(ba,'301')#ciencia e tecnologia

#cultura
cult=pd.read_excel(ba,'302')#cultura

#desenvolvimento produtivo
des=pd.read_excel(ba,'303')#desenvolvimento produtivo

#desenvolvimento Rural
desr=pd.read_excel(ba,'304')#desenvolvimento rural

#infraestrutura
infr=pd.read_excel(ba,'309')##infraestrutura

###################################################
#Meio ambiente e sustentab
sus=pd.read_excel(ba,'310')

###################################################
#recursos hidricos
hidr=pd.read_excel(ba,'312')

###################################################

#Gestao governamental
ges=pd.read_excel(ba,'315')
##########################################33

#########################################################################

#juntando colunas
ppa_ind = pd.concat([ct,cult,des,desr,infr,sus,hidr,ges])

ppa_ind=ppa_ind.fillna({'Sugestão (manter/alterar/substituir)': 'Sem Sugestão'})

###########################################################################################

#ajustes na situação da reuniao setorial
#nome das colunas

ppa_ind['Situação da Reunião Setorial']=ppa_ind.loc[:,'Síntese Reunião Setorial'].isnull()

#situação das reuniões setoriais
ppa_ind=ppa_ind.replace({'Situação da Reunião Setorial': {True:'Reunião Não Registrada', False:'Houve Reunião'}})

################

#Filtrando falta de reuniao pegar os indices
sem_reuniao_ppa=ppa_ind[ppa_ind['Situação da Reunião Setorial']=='Reunião Não Registrada']

###############################################################################


# Parte Inicial

st.markdown("# Aplicativo Para Apresentação dos Programas do PPA 2020-2023")

st.markdown("Explore as informações referentes aos programas incluídos no PPA")

#Image.open(r'C:\Users\atsilva\Desktop\logo_seplan.png').convert('RGB').save('new.jpeg')

img=Image.open(r'Seplan-BA.jpg')

st.image(img,width=674)

st.markdown("**PPA** São Informações do Plano PluriAnual do Estado da Bahia, referente ao planejamento do estado da Bahia.")

st.markdown("Informações dos Programas do PPA")

#Parte interativa

if st.button("Conheça os Programas da Seplan BA"):
    img=Image.open(r'Programas_PPA.jpg')
    st.image(img,width=700, caption="Programas do PPA 2020-2023")
    #images=Image.open(r'C:\Users\atsilva\Desktop\new.jpeg')
  #  st.image(images,width=600)
    #Ballons
    #st.balloons()
    
st.markdown(
    "Os dados são provenientes da [Seplan-BA](http://www.seplan.ba.gov.br/arquivos/File/ppa/PPA2020_2023/05PPA_2020-2023_Publicado-TABELAS_RECURSOS_E_INDICADORES.pdf)")


st.info("O plano PluriAnual é Realizado de 4 em 4 anos e contém informações referente ao desenvolvimento de todo o estado da Bahia.")
img=Image.open(r'nucleo_territorial_educacao_2018.jpg')
st.image(img,width=700,caption = "fonte: SEI - Superintendência de Estudos Econômicos e Sociais da Bahia (https://www.sei.ba.gov.br/index.php?option=com_content&view=category&id=1500&Itemid=101)")

##################################################################################################

#Painel lateral

st.sidebar.markdown("## Painel Lateral")
st.sidebar.markdown("Use esse painel para explorar o app e criar interações.")

#df = pd.read_csv(DATA_URL, nrows = nrows)
 #   lowercase = lambda x:str(x).lower()
  #  df.rename(lowercase, axis='columns',inplace=True)
   # return df

st.header("Explore a Base de dados do PPA revisado")

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Baixando Base de dados do PPA do Programa de Gestão Governamental...')
    # Load 10,000 rows of data into the dataframe.
ges
df = ppa_ind

# Notify the reader that the data was successfully loaded.

data_load_state.text('Baixando base de dados do PPA do Programa de Gestão Governamental...Completo!')

images=Image.open(r'new.jpeg')

st.image(images,width=200)


##################################################
#interação painel lateral check box

if st.checkbox("Mostrar Todos Os Dados de todos os Programas íncluidos no DPE", False):
    st.subheader('Todos Os Dados')
    st.write(df)
st.title('Explorando...')
st.sidebar.subheader(' Exploração Breve')
st.markdown("Marque a caixinha no painel lateral para explorar os dados.")
if st.sidebar.checkbox('Informação Básica'):
    #if st.sidebar.checkbox('Breve exploração da base'):
        #st.subheader('Exploração Breve:')
       # st.write(df.head())
    if st.sidebar.checkbox("Mostrar Colunas"):
        st.subheader('Mostrar Lista de Colunas')
        all_columns = df.columns.to_list()
        st.write(all_columns)
   
    if st.sidebar.checkbox('Descrição Estatística (Apenas Para Vias de Demonstração)'):
        st.subheader('Dados da Descrição Estatística')
        st.write(df.describe())
    if st.sidebar.checkbox('Valores Faltantes?'):
        st.subheader('Valores Faltantes')
        st.write(df.isnull().sum())



if st.sidebar.checkbox('Exploração Breve Da Base'):
        st.subheader('Breve Exploração dos Dados:')
        st.write(df.head())

#############

#visualizacao de dados parte do painel lateral

st.title('Escolha Um Gráfico')
st.markdown("Marque uma das opções para disponibilizar a visualização.")
st.sidebar.subheader('Criando Gráficos')
if st.sidebar.checkbox('Gráficos'):
    if st.sidebar.checkbox('Gráfico de Barras - Contagem'):
        st.subheader('Gráfico de Barras')
        st.info("Caso Haja Erro por favor ajuste o nome no painel.")
        column_count_plot = st.sidebar.selectbox("Escolha uma coluna para visualizar. Tente Selecionar Programa",df.columns)
        hue_opt = st.sidebar.selectbox("Variáveis Categóricas Opcionais. Tente Selecionar Sugestão",df.columns.insert(0,None))
        
        fig = sns.countplot(x=column_count_plot,data=df,hue=hue_opt)
        st.pyplot()
            
            
    #if st.sidebar.checkbox('Histograma'):
      #  st.subheader('Histograma')
       # st.info("Caso Haja Erro Favor ajuste o nome da coluna no painel.")
        # if st.checkbox('Dist plot'):
       # column_dist_plot = st.sidebar.selectbox("Tente Selecionar o valor de referência",df.columns)
      #  fig = sns.distplot(df[column_dist_plot])
       # st.pyplot()
            
            
 
        
   # if st.sidebar.checkbox('Boxplot'):
       # st.subheader('Boxplot')
       # st.info("If error, please adjust column name on side panel.")
       # column_box_plot_X = st.sidebar.selectbox("X (Choose a column). Try Selecting island:",df.columns.insert(0,None))
       # column_box_plot_Y = st.sidebar.selectbox("Y (Choose a column - only numerical). Try Selecting Body Mass",df.columns)
       # hue_box_opt = st.sidebar.selectbox("Optional categorical variables (boxplot hue)",df.columns.insert(0,None))
        # if st.checkbox('Plot Boxplot'):
       # fig = sns.boxplot(x=column_box_plot_X, y=column_box_plot_Y,data=df,palette="Set3")
       # st.pyplot()



st.sidebar.markdown("[Fonte de Dados](https://seplan.ba.gov.br/)")
st.sidebar.info(" [Mais informações sobre o PPA](https://seplan.ba.gov.br/modules/conteudo/conteudo.php?conteudo=100)")
st.sidebar.info("Projeto feito por [Lucas Rabelo](https://github.com/marreapato) ")
st.sidebar.text("Feito com Streamlit - Python")







