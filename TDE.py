from itertools import product

arquivo = open("arqtxt2.txt", "r")
qtd_operacoes = int(arquivo.readline())

while qtd_operacoes > 0:
    operacao = arquivo.readline().strip()
    conjunto_1 = set(espaco.strip() for espaco in arquivo.readline().strip().split(','))
    conjunto_2 = set(espaco.strip() for espaco in arquivo.readline().strip().split(','))
    
    if operacao == "U":
        uniao = conjunto_1.union(conjunto_2)
        print(f"União: conjunto 1 {conjunto_1}, conjunto 2 {conjunto_2}. Resultado: {uniao}")
    
    elif operacao == "I":
        interseccao = conjunto_1.intersection(conjunto_2)
        print(f"Interseção: conjunto 1 {conjunto_1}, conjunto 2 {conjunto_2}. Resultado: {interseccao}")
        
    elif operacao == "D":
        diferenca = conjunto_1.difference(conjunto_2)
        print(f"Diferença: conjunto 1 {conjunto_1}, conjunto 2 {conjunto_2}. Resultado: {diferenca}")
    
    elif operacao == "C":
        produto = set(product(conjunto_1, conjunto_2))
        print(f"Produto do cartesiano: conjunto 1 {conjunto_1}, conjunto 2 {conjunto_2}. Resultado: {produto}")
    
    qtd_operacoes -= 1

arquivo.close()
