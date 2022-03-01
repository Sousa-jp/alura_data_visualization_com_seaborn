from analisando_forma_visual_e_descritiva import gorjetas
from matplotlib import pyplot as plt
from scipy.stats import ranksums

import seaborn as sns

print('gorjetas.head() : \n', gorjetas.head())

sns.catplot(x='hora_dia', y='valor_conta',kind='swarm', data=gorjetas)
plt.show()

sns.violinplot(x='hora_dia', y='valor_conta', data=gorjetas)
plt.show()

sns.boxplot(x='hora_dia', y='valor_conta', data=gorjetas)
plt.show()

almoco = gorjetas.query("hora_dia == 'Almoço'").valor_conta
sns.displot(almoco)
plt.show()

jantar = gorjetas.query("hora_dia == 'Jantar'").valor_conta
sns.displot(jantar)
plt.show()

print(gorjetas.groupby(['hora_dia']).mean()[['valor_conta', 'gorjeta', 'porcentagem']])

r3 = ranksums(jantar, almoco)
print('O valor do p-value é', r3.pvalue)
print('A distribuição do valor da conta não é igual no almoço e no jantar')

porcentagem_almoco = gorjetas.query("hora_dia == 'Almoço'").porcentagem
porcentagem_jantar = gorjetas.query("hora_dia == 'Jantar'").porcentagem

print('O valor do p-value é', ranksums(porcentagem_jantar, porcentagem_almoco).pvalue)
print('A distribuição da taxa de gorjeta é igual no almoço e no jantar')
