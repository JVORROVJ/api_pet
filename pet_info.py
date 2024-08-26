def coletar_informacoes_pet():
    nome = input("Nome do pet: ")
    
    # Adicionando espécie do pet
    especie = input("Digite qual é a espécie do pet: ")

    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Espécie: {especie}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")

# Chama a função para coletar e exibir as informações
coletar_informacoes_pet()
