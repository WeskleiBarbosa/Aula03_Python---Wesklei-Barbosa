total = 0
produtos_acima_1000 = 0
produto_mais_barato = ""
preco_mais_barato = float('inf')

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    preco = float(input("Digite o preço do produto: "))

    total += preco

    if preco > 1000:
        produtos_acima_1000 += 1

    if preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome

print(f"Total gasto: R${total:.2f}")
print(f"Quantidade de produtos acima de R$1000: {produtos_acima_1000}")
print(f"Produto mais barato: {produto_mais_barato} com preço de R${preco_mais_barato:.2f}")
