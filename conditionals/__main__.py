# Uses a ternary to get the input from the user, check if its less than 18, and choose what to print in a single line.
# Format is <true> if <cond> else <false>.
print("Rejeitado" if int(input("Digite a idade da pessoa: ")) < 18 else "Aprovado")
