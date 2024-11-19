import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')


sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, marker='o', color='b', label='Preço da Gasolina')

plt.title('Preço da Gasolina ao Longo do Tempo', fontsize=16)
plt.xlabel('Dia', fontsize=12)
plt.ylabel('Preço (R$)', fontsize=12)

plt.xticks(rotation=45)

plt.legend(title='Legenda', fontsize=12, loc='upper right')

plt.tight_layout()
plt.savefig('gasolina.png')

plt.show()
