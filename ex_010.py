quantidade_reais = float(input('Quanto dinheiro você tem? R$'))
cotacao = 5.53
dolar = quantidade_reais // cotacao
print(f'Os seus R${quantidade_reais:.2f} equivalem a US${dolar:.2f}')
