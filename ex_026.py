frase = str(input('digite uma frase: ')).lower().strip()
print(f'a letra A aparece {frase.count("a")} vezes na frase ')
print(f'a primeira letra A aparece na posição {frase.index("a")+1}')
print(f'a ultima letra A aparece na posição {frase.rfind("a")+1} ')
