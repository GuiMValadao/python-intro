# -------------------------------------
# Tabela de desconto
# -------------------------------------

# Tabela de preços e valor do desconto
precos = [4.95, 9.95, 14.95, 19.95, 24.95]
desconto = 0.6
print("Preço original   | " "Valor do desconto\t | Preço com desconto")
print("-" * 60)
for item in range(0, len(precos)):
    print(
        f"\t{precos[item]:.2f}\t",
        f"|\t{precos[item]*desconto:.2f}\t\t",
        f"|\t{(precos[item]*(1-desconto)):.2f}",
    )
