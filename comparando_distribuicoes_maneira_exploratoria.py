from importando_e_traduzindo_dados import (gorjetas)
from matplotlib import pyplot as plt
import seaborn as sns

gorjetas = gorjetas
print('gorjetas.columns : \n', gorjetas.columns)

valor_gorjeta = sns.scatterplot(x='valor_conta', y='gorjeta', data=gorjetas)
plt.show()

print('gorjetas.shape[0] : \n', gorjetas.shape[0])
print('gorjetas.count() : \n', gorjetas.count())

gorjetas['porcentagem'] = gorjetas['gorjeta'] / gorjetas['valor_conta']
print('gorjetas.head() : \n', gorjetas.head())

gorjetas.porcentagem = gorjetas.porcentagem.round(2)
print('gorjetas.head() : \n', gorjetas.head())

porcentagem_conta = sns.scatterplot(x='valor_conta', y='porcentagem', data=gorjetas)
plt.show()

porcentagem_conta_linha = sns.relplot(x='valor_conta', y='porcentagem',kind='line', data=gorjetas)
plt.show()

sns.lmplot(x='valor_conta', y='porcentagem', data=gorjetas)
plt.show()

porcentagem_conta.set_title('Análise do valor da gorjeta em função do valor da conta')
porcentagem_conta.set(xlabel='Valor da conta', ylabel='Valor da gorjeta')
imagem = porcentagem_conta.get_figure()
imagem.savefig('data/imagem.png')
