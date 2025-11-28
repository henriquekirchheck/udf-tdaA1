## Dictionary that has the product name as the key and the price as the value.
products: dict[str, float] = {}

while (
    # This line uses the python walrus operator to simultanealy assign a value to a variable and use its value in an expression.
    product := input(
        'Digite um produto para adicionar ao dicionario (formato: "{nome} R${preço}") (exit para sair): '
    ).strip()
) != "exit":
    # This line separates the input into its parts, uses a map to easily strip out any extra spaces from the input
    name, price = map(lambda x: x.strip(), product.split("R$", 1))
    # Replacing the "," with "." so float parsing doesn't fail in the case of it being written with the brazilian decimal separator.
    price = float(price.replace(",", "."))
    products[name] = price

# This just formats the result in a prettier way.
for name, price in products.items():
    print(f"""
Produto
Nome: {name}
Preço: R${price:.2f}""")
