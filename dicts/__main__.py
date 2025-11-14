products: dict[str, float] = {}

while (
    product := input(
        'Digite um produto para adicionar ao dicionario (formato: "{nome} R${preço}") (exit para sair): '
    ).strip()
) != "exit":
    name, price = map(lambda x: x.strip(), product.split("R$", 1))
    price = float(price.replace(",", "."))
    products[name] = price

for name, price in products.items():
    print(f"""
Produto
Nome: {name}
Preço: R${price:.2f}""")
