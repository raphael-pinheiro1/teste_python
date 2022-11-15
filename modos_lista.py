meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_completa = vendas_1sem + vendas_2sem
maior_valor = max(vendas_completa)
menor_valor = min(vendas_completa)

i_maior = vendas_completa.index(maior_valor)
i_menor = vendas_completa.index(menor_valor)



print(f'Maior venda: {maior_valor} \n Menor venda: {menor_valor} \n O melhor mês do ano foi: {meses[i_maior]} \n O pior mês do ano foi: {meses[i_menor]}  \n lista completa: {vendas_completa}')
