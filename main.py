import sys

arqv_sped = sys.argv[1]
arqv_itens = sys.argv[2]

sped = open(arqv_sped)
linhas_sped = sped.readlines()

itens = open(arqv_itens)
linhas_itens = itens.readlines()

if len(linhas_sped) >= len(linhas_itens):
    for linha_sped in linhas_sped:
        for linha_item in linhas_itens:
            if linha_item == linha_sped:
                print(f'{linha_sped} é igual a {linha_item}')
            else:
                print(f'{linha_sped} não é igual a {linha_item}')