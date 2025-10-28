# Importação da biblioteca para manipulação de dados em tabelas
import pandas as pd  

# Importação da biblioteca NumPy para operações matemáticas e arrays
import numpy as np  

# Importação da biblioteca Matplotlib para geração de gráficos
import matplotlib.pyplot as plt  

# Importação da biblioteca Seaborn para visualização estatística de dados
import seaborn as sns  

# Importação da biblioteca random para geração de números aleatórios
import random  

# Importação das classes datetime e timedelta para manipulação de datas e intervalos de tempo
from datetime import datetime, timedelta 
# Definição da função para gerar dados fictícios de vendas
def dsa_gera_dados_ficticios(num_registros = 600):
    
    """
    Gera um DataFrame do Pandas com dados de vendas fictícios.
    """

    # Mensagem inicial indicando a quantidade de registros a serem gerados
    print(f"\nIniciando a geração de {num_registros} registros de vendas...")

    # Dicionário com produtos, suas categorias e preços
    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
    }

    # Cria uma lista apenas com os nomes dos produtos
    lista_produtos = list(produtos.keys())

    # Dicionário com cidades e seus respectivos estados
    cidades_estados = {
        'São Paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo Horizonte': 'MG',
        'Porto Alegre': 'RS', 'Salvador': 'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'
    }

    # Cria uma lista apenas com os nomes das cidades
    lista_cidades = list(cidades_estados.keys())

    # Lista que armazenará os registros de vendas
    dados_vendas = []

    # Define a data inicial dos pedidos
    data_inicial = datetime(2026, 1, 1)

    # Loop para gerar os registros de vendas
    for i in range(num_registros):
        
        # Seleciona aleatoriamente um produto
        produto_nome = random.choice(lista_produtos)

        # Seleciona aleatoriamente uma cidade
        cidade = random.choice(lista_cidades)

        # Gera uma quantidade de produtos vendida entre 1 e 7
        quantidade = np.random.randint(1, 8)

        # Calcula a data do pedido a partir da data inicial
        data_pedido = data_inicial + timedelta(days = int(i/5), hours = random.randint(0, 23))

        # Se o produto for Mouse ou Teclado, aplica desconto aleatório de até 10%
        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome]['preco']

        # Adiciona um registro de venda à lista
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })
    
    # Mensagem final indicando que a geração terminou
    print("Geração de dados concluída.\n")

    # Retorna os dados no formato de DataFrame
    return pd.DataFrame(dados_vendas)

#Gera os dados chamando a função
df_vendas = dsa_gera_dados_ficticios(500)
print(type(df_vendas))
#print(df_vendas)
df_vendas.head() #ver as 5 primeiras linhas
df_vendas.tail() #ver as 5 últimas
df_vendas.info() #ver informações gerais
df_vendas.describe() #ver estatísticas descritivas
#Converter a Data Pedido em formato datetime
df_vendas["Data_Pedido"] = pd.to_datetime(df_vendas["Data_Pedido"])
#Criando a coluna Faturamento
df_vendas["Faturamento"] = df_vendas["Preco_Unitario"] * df_vendas["Quantidade"]
df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(lambda estado: "Rapida" if estado in ["SP","RJ","MG"] else "Normal")
print(df_vendas)
print(df_vendas.info())

#Análise 1 Top 10 Produtos
#print("Análise 1")
#Agrupa por nome de produto, soma a quantidade e ordena para encontrar os mais vendidos
#top_10_produtos = df_vendas.groupby('Nome_Produto')['Quantidade'].sum().sort_values(ascending=False).head(10)
#print(top_10_produtos)
#Criar o gráfico
#sns.set_style("whitegrid")
#plt.figure(figsize=(12,7))
#top_10_produtos.sort_values(ascending=True).plot(kind="barh",color="skyblue")

#Adiciona títulos e labels do gráfico
#plt.title ("Meu gráfico", fontsize = 18)
#plt.xlabel("Quantidade Vendida", fontsize = 12)
#plt.ylabel("Produto", fontsize = 12)

#Exibir o gráfico
#plt.tight_layout()
#plt.show()

#Análise 2
#print("Análise 2")
#Cria uma coluna para o mês para fazer agrupamento mensal
#df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')
#Agrupa por mês e soma o faturamento
#faturamento_mensal = df_vendas.groupby('Mes')['Faturamento'].sum()
#Converter para string para exibir no gráfico
#faturamento_mensal.index = faturamento_mensal.index.strftime("%Y-%m")
#faturamento_mensal.map("R$ {:,.2f}".format)
#plt.figure(figsize=[12,6])
#faturamento_mensal.plot(kind="line",marker = 'o',linestyle = '-',color='green')
#plt.title("Evolução do Faturamento Mensal", fontsize = 16)
#plt.xlabel("Mês", fontsize = 12)
#plt.ylabel("Faturamento (R$)", fontsize = 12)
#Rotação em 45º graus
#plt.xticks(rotation = 45)
#Colocar grade tracejada e linhas finas
#plt.grid(True,which='both',linestyle = '--',linewidth = 0.5)
#Ajusta os elementos para não sobreporem
#plt.tight_layout()
#Exibe
#plt.show()

#Análise 3
#print("Análise 3")
#Agrupa os dados por estado e soma o faturamento
#vendas_estado = df_vendas.groupby('Estado')['Faturamento'].sum().sort_values(ascending=False)

#Formata para duas casas decimais
#print(vendas_estado.map('R$ {:.2f}'.format))
#plt.figure(figsize=(12,7))
#vendas_estado.plot(kind='bar', color = sns.color_palette('Spectral',7))
#plt.title("Faturamento por Estado", fontsize = 16)
#plt.xlabel("Estado", fontsize = 12)
#plt.ylabel("Faturamento (R$)", fontsize = 12)
#plt.xticks(rotation = 0)
#plt.tight_layout()
#plt.show()

#Análise 4
#Faturamento por categoria
print("Análise 4")
#Agrupar por categoria e soma o faturamento
faturamento_categoria = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending=False)
print(faturamento_categoria.map('R$ {:,.2f}'.format))

#FuncFormatter para formatar os eixos
from matplotlib.ticker import FuncFormatter

# Ordena os dados para o gráfico ficar mais fácil de ler
faturamento_ordenado = faturamento_categoria.sort_values(ascending = False)

# Cria a Figura e os Eixos (ax) com plt.subplots()
# Isso nos dá mais controle sobre os elementos do gráfico.
fig, ax = plt.subplots(figsize = (12, 7))
#Cria uma função para formatar os números
#Recebe um valor x e transforma em string no formato R$ XX

def formatar_milhares(y,pos):
    #Formata o valor em milhares com o cifrão R$
    return f"R$ {y/1000:,.0f}K"

# Cria o objeto formatador
formatter = FuncFormatter(formatar_milhares)

# Aplica o formatador ao eixo Y (ax.yaxis)
ax.yaxis.set_major_formatter(formatter)

# Plota os dados usando o objeto 'ax'
faturamento_ordenado.plot(kind = 'bar', ax = ax, color = sns.color_palette("viridis", len(faturamento_ordenado)))

# Adiciona títulos e labels usando 'ax.set_...'
ax.set_title('Faturamento Por Categoria', fontsize = 16)
ax.set_xlabel('Categoria', fontsize = 12)
ax.set_ylabel('Faturamento', fontsize = 12)

# Ajusta a rotação dos rótulos do eixo X
plt.xticks(rotation = 45, ha = 'right')

# Garante que tudo fique bem ajustado na imagem final
plt.tight_layout()

# Exibe o gráfico
plt.show()
