dias = int(input('digite a quantidade de dias: '))
km = float(input('digite a quantidade de km: '))
total_pago = (dias * 60) + (km * 0.15)
print(f'o preço foi de: R${total_pago:.2f}')
