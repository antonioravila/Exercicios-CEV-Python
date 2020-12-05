nome = input('digite seu nome completo: ')
print('analizando seu nome...')
print(f'seu nome em maiúsculas é {nome.upper()}')
print(f'seu nome em minúsculas é {nome.lower()}')
print(f'seu nome tem ao todo {len(nome)} letras')
nome_separado = nome.split()
primeiro_nome = nome_separado[0]
print(f'seu primeiro nome é {primeiro_nome}, e ele tem {len(primeiro_nome)} letras')
