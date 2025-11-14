names: list[str] = []

while (
    name := input("Digite um nome para adicionar a lista (exit para sair): ").strip()
) != "exit":
    if name == "":
        continue
    names.append(name)

print(*names, sep="\n")
