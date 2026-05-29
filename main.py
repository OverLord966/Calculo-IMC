# Sprint 1 - Cálculo do IMC

# Solicitar dados ao utilizador
peso = float(input("Introduza o seu peso (kg): "))
altura_cm = float(input("Introduza a sua altura (cm): "))

# Converter altura para metros
altura_m = altura_cm / 100

# Calcular IMC
imc = peso / (altura_m * altura_m)

# Arredondar a 2 casas decimais
imc_arredondado = round(imc, 2)

# Apresentar o valor do IMC
print(f"\nO seu IMC é: {imc_arredondado}")

# Classificação
if imc < 18.5:
    print("Classificação: Fora do peso normal")
elif imc < 25:
    print("Classificação: Peso normal")
else:
    print("Classificação: Fora do peso normal")
print("\nFim do programa.")