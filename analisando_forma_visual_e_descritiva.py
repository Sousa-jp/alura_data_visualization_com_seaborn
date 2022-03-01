from comparando_distribuicoes_maneira_exploratoria import (gorjetas)
from matplotlib import pyplot as plt
from scipy.stats import ranksums

import seaborn as sns

gorjetas = gorjetas

print("gorjetas[gorjetas.sobremesa == 'Sim'].describe() : \n", gorjetas[gorjetas.sobremesa == 'Sim'].describe())
print("gorjetas[gorjetas.sobremesa == 'Não'].describe() : \n", gorjetas[gorjetas.sobremesa == 'Não'].describe())

gorjeta_x_sobremesa = sns.catplot(x='sobremesa', y='gorjeta', data=gorjetas)
plt.show()

sns.relplot(x='valor_conta', y='gorjeta', hue='sobremesa', col='sobremesa', data=gorjetas)
plt.show()

sns.lmplot(x='valor_conta', y='gorjeta', col='sobremesa', hue='sobremesa', data=gorjetas)
plt.show()

sns.lmplot(x='valor_conta', y='porcentagem', col='sobremesa', hue='sobremesa', data=gorjetas)
plt.show()

sobremesa = gorjetas.query("sobremesa == 'Sim'").porcentagem
sem_sobremesa = gorjetas.query("sobremesa == 'Não'").porcentagem

r = ranksums(sobremesa, sem_sobremesa)
print('o valor do p-value é {}'.format(r.pvalue))
print('a distribuição nos dois grupos é a mesma')