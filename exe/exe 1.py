loja_fruta = {
    'melancia': 3.00,
    'pitaya': 14.00,
    'mandioca': 4.00,
}


#função get
preco_mandioca = loja_fruta.get('mandioca',{})
print('Mandioca:', preco_mandioca)


#função update: metodo usado para atualizar os valores
loja_fruta.update({'Mandioca': 4.0,'Siriguela': 5})
print(loja_fruta,'#Siriguela adicionado')


#remover um dado do dicionario
loja_fruta.pop('Siriguela')
print(loja_fruta,'#Siriguela removida')

#função itens: metodo de leitura de um dicionario
for chave, valor in loja_fruta.items():
  print(f'key:{chave}: value:{valor}')