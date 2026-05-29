# Sprint 3 - IMC com Loop, resumo final e tratamento de erros.

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


def ler_float(mensagem: str) -> float:
    """Lê um número float com tratamento de erros."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Erro: o valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Erro: introduza um número válido.")


def mostrar_resumo(imcs: list, classificacoes: list):
    """Mostra o resumo final das consultas."""
    total = len(imcs)
    media = round(sum(imcs) / total, 2)

    # Classificação mais frequente
    mais_frequente = max(set(classificacoes), key=classificacoes.count)

    print("\n=== RESUMO FINAL ===")
    print(f"Total de consultas: {total}")
    print(f"Média dos IMC: {media}")
    print(f"Classificação mais frequente: {mais_frequente}")


def main():
    imcs = []
    classificacoes = []

    print("=== Sistema de Cálculo de IMC ===")

    while True:
        peso = ler_float("Introduza o seu peso (kg): ")
        altura_cm = ler_float("Introduza a sua altura (cm): ")

        altura_m = converter_altura(altura_cm)
        imc = calcular_imc(peso, altura_m)
        classificacao = classificar_imc(imc)

        print(f"\nO seu IMC é: {imc}")
        print(f"Classificação: {classificacao}\n")

        imcs.append(imc)
        classificacoes.append(classificacao)

        continuar = input("Deseja realizar outra consulta? (s/n): ").strip().lower()
        if continuar != "s":
            break

    mostrar_resumo(imcs, classificacoes)


if __name__ == "__main__":
    main()
