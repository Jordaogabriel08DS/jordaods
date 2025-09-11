def mostrar_menu():
    print("\n=== Gestão de Viagens ===")
    print("1. Adicionar viagem")
    print("2. Listar viagens")
    print("3. Sair")

def adicionar_viagem(viagens):
    destino = input("Destino: ")
    data = input("Data (DD/MM/AAAA): ")
    custo = float(input("Custo da viagem: R$ "))
    viagem = {
        "destino": destino,
        "data": data,
        "custo": custo
    }
    viagens.append(viagem)
    print("Viagem adicionada com sucesso!")

def listar_viagens(viagens):
    if not viagens:
        print("Nenhuma viagem cadastrada.")
        return
    print("\nViagens cadastradas:")
    for i, v in enumerate(viagens):
        print(f"{i+1}. Destino: {v['destino']}, Data: {v['data']}, Custo: R$ {v['custo']:.2f}")

def main():
    viagens = []
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            adicionar_viagem(viagens)
        elif escolha == "2":
            listar_viagens(viagens)
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
