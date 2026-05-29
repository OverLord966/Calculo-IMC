# Sprint 2 - Cálculo do IMC com funções e classificação OMS

def converter_altura(altura_cm: float) -> float:
    """Converte altura de centímetros para metros."""
    return altura_cm / 100


def calcular_imc(peso: float, altura_m: float) -> float:
    """Calcula o IMC e devolve o valor arredondado a 2 casas decimais."""
    imc = peso / (altura_m * altura_m)
    return round(imc, 2)


def classificar_imc(imc: float) -> str:
    """Classifica o IMC segundo a OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    else:
        return "Obesidade"


def main():
    print("=== Cálculo do IMC ===")

    peso = float(input("Introduza o seu peso (kg): "))
    altura_cm = float(input("Introduza a sua altura (cm): "))

    altura_m = converter_altura(altura_cm)
    imc = calcular_imc(peso, altura_m)
    classificacao = classificar_imc(imc)

    print(f"\nO seu IMC é: {imc}")
    print(f"Classificação: {classificacao}")


if __name__ == "__main__":
    main()
