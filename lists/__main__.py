names: list[str] = []

while (
    # This line uses the python walrus operator to simultanealy assign a value to a variable and use its value in an expression.
    name := input("Digite um nome para adicionar a lista (exit para sair): ").strip()
) != "exit":
    # if they didn't input anythingm just ignore and ask again
    if name == "":
        continue
    names.append(name)

# List destructuring to pass all itens in the list as arguments to the print function
print(*names, sep="\n")
