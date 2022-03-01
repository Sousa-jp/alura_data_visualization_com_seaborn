import pandas as pd


dados = pd.read_csv('data/tips.csv')
print('dados.head() : \n', dados.head() )

print('dados.columns : \n', dados.columns)

renomeacao = {
    'total_bill': 'valor_conta',
    'tip': 'gorjeta',
    'dessert': 'sobremesa',
    'day': 'dia_semana',
    'time': 'hora_dia',
    'size': 'total_pessoas'
}

gorjetas = dados.rename(columns=renomeacao)
print('gorjetas.head() : \n', gorjetas.head())

print('gorjetas.sobremesa.unique() : \n', gorjetas.sobremesa.unique())
sim_nao = {
    'No': 'Não',
    'Yes': 'Sim'
}
gorjetas.sobremesa = gorjetas.sobremesa.map(sim_nao)
print('gorjetas.head() : \n', gorjetas.head())

print('gorjetas.dia_semana.unique() : \n', gorjetas.dia_semana.unique())
dias = {
    'Sun': 'Domingo',
    'Sat': 'Sábado',
    'Thur': 'Quinta',
    'Fri': 'Sexta'
}

gorjetas.dia_semana = gorjetas.dia_semana.map(dias)
print('gorjetas.head() : \n', gorjetas.head())

hora = {
    'Dinner': 'Jantar',
    'Lunch': 'Almoço'
}
gorjetas.hora_dia = gorjetas.hora_dia.map(hora)
print('gorjetas.head() : \n', gorjetas.head())
