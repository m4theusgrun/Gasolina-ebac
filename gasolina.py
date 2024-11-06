import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('gasolina.csv')

# Verificar as primeiras linhas do DataFrame (opcional)
print(df.head())

# Definindo o estilo do gráfico
sns.set(style="whitegrid")

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', marker='o')

# Adicionando título e rótulos
plt.title('Preço da Gasolina ao Longo dos Dias')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Salvar o gráfico em um arquivo
plt.savefig('gasolina.png')

# Exibir o gráfico
plt.show()
