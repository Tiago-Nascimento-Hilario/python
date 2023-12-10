# String são imutáveis, alterar necessário armazenar em uma nova variável

cidade = 'Porto alegre'

print(cidade.split())
print(cidade.join(" - "))
print(cidade[1])
print(cidade.index('r'))
print(cidade[-5:])

biblioteca = 'Biblioteca'
frase1 = 'Desenvolvimento De Aplições'
frase2 = 'Desenvolvimento de palicações com Python'

print(biblioteca.index('o'))
print(frase1[-11:])

palavras1 = frase1.split()
print(palavras1)
palavras2 = frase2.split()
print(palavras2)

print(','.join(palavras1))
print(' & '.join(palavras2))



