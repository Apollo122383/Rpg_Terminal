loja_carros = {
    'mercedes':{
        'valor': 200.000,
        'cor': 'verde',
        },
    'BMW':{
        'valor': 400.000,
        'cor': 'preto',
        },
}


for k,v in loja_carros.items():
      loja_carros.get(k)['valor']*=1.15
print(loja_carros)