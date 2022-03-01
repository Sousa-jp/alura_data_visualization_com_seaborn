from analisando_forma_visual_e_descritiva import gorjetas
from matplotlib import pyplot as plt
from scipy.stats import ranksums

import seaborn as sns

gorjetas = gorjetas
print('gorjetas.dia_semana.unique() : \n', gorjetas.dia_semana.unique())

sns.catplot(x='dia_semana', y='valor_conta', data=gorjetas)
plt.show()

sns.relplot(x='valor_conta', y='gorjeta', hue='dia_semana', data=gorjetas)
plt.show()

sns.relplot(x='valor_conta', y='porcentagem', hue='dia_semana', data=gorjetas)
plt.show()

sns.relplot(x='valor_conta', y='gorjeta', hue='dia_semana', col='dia_semana', data=gorjetas)
plt.show()

sns.relplot(x='valor_conta', y='porcentagem', hue='dia_semana', col='dia_semana', data=gorjetas)
plt.show()

sns.lmplot(x='valor_conta', y='porcentagem', hue='dia_semana', col='dia_semana', data=gorjetas)
plt.show()

media_geral_gorgetas = gorjetas.gorjeta.mean()
print(f'Medía geral gorgetas {media_geral_gorgetas}')

print("gorjetas.groupby(['dia_semana']).mean() : \n",
      gorjetas.groupby(['dia_semana']).mean()[['valor_conta', 'gorjeta', 'porcentagem']])

print('gorjetas.dia_semana.value_counts() :  \n', gorjetas.dia_semana.value_counts())

valor_conta_domingo = gorjetas.query("dia_semana == 'Domingo'" ).valor_conta
valor_conta_sabado = gorjetas.query("dia_semana == 'Sábado'" ).valor_conta
r2 = ranksums(valor_conta_domingo, valor_conta_sabado)
print('O valor do p-value é :', r2.pvalue)
print('A distribuição do valor da conta é igual no sábado e no domingo')
