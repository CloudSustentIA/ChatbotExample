import os, platform, string
import delivery, db
from datetime import datetime

os_name = platform.system()
if os_name == "Windows":
    clear = "cls"
elif os_name == "Linux":
    clear = "clear"
else:
    print("[-]Sistema operacional nao detectado, limpar tela nao sera possivel!")


def chatbot():
    calabresa = 28
    portuguesa = 29
    frangoCatupiry = 30
    baiana = 28
    carijo = 29
    moda = 32
    quatroQueijos = 27
    matriz = [calabresa, portuguesa, frangoCatupiry, baiana, carijo, moda, quatroQueijos]

    print("Qual tamanho da pizza que voce deseja?")
    print("1 - Pizza M - 4 pedacos")
    print("2 - Pizza G - 8 pedacos")
    print("3 - Pizza X - 12 pedacos")
    tamanho = int(input("Selecione o tamanho: "))
    if tamanho >= 4:
        print("\nNumero invalido\nFinalizando o atendimento...")
        exit()
    #os.system(f"{clear}")

    if tamanho == 1:
        print("\n[+] Escolha o sabor da pizza: ")
        print("1 - Calabresa - R$:28.00")
        print("2 - Portuguesa - R$:29.00")
        print("3 - Frango com catupiry - R$:30.00")
        print("4 - Baiana - R$:28.00")
        print("5 - Carijo - R$:29.00")
        print("6 - A moda - R$:32.00")
        print("7 - Quatro queijos - R$:27.00")
        sabor = int(input("Escolha o sabor: "))
        if sabor >= 8:
            print("\nNumero invalido\nFinalizando o atendimento...")
            exit()
        print("\n")
        valor = matriz[sabor - 1]
        print(f"Valor R$: ${valor:.2f}")
    elif tamanho == 2:
        print("\n[+] Escolha o sabor da pizza: ")
        print("1 - Calabresa - R$:48.00")
        print("2 - Portuguesa - R$:49.00")
        print("3 - Frango com catupiry - R$:50.00")
        print("4 - Baiana - R$:48.00")
        print("5 - Carijo - R$:49.00")
        print("6 - A moda - R$:52.00")
        print("7 - Quatro queijos - R$:47.00")
        sabor = int(input("Escolha o sabor: "))
        if sabor >= 8:
            print("\nNumero invalido\nFinalizando o atendimento...")
            exit()
        print("\n")
        valor = matriz[sabor - 1] + 20
        print(f"Valor R$: ${valor:.2f}")
    elif tamanho == 3:
        print("\n[+] Escolha o sabor da pizza: ")
        print("1 - Calabresa - R$:58.00")
        print("2 - Portuguesa - R$:59.00")
        print("3 - Frango com catupiry - R$:60.00")
        print("4 - Baiana - R$:58.00")
        print("5 - Carijo - R$:59.00")
        print("6 - A moda - R$:62.00")
        print("7 - Quatro queijos - R$:57.00")
        sabor = int(input("Escolha o sabor: "))
        if sabor >= 8:
            print("\nNumero invalido\nFinalizando o atendimento...")
            exit()
        print("\n")
        valor = matriz[sabor - 1] + 30
        print(f"Valor R$: ${valor:.2f}")

    while True:
        try:
            name = input("Digite seu nome e sobrenome: ")
            if not name.replace(" ", "").isalpha():
                raise ValueError("O nome deve conter apenas letras e espacos.")
            break
        except ValueError as e:
            print(f"{e} Tente novamente.\n")

    while True:
        tel1 = input("Digite seu numero de telefone para contato: ")
        tel = tel1.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        if tel1.isdigit() and len(tel) == 11:
            break
        print("Numero invalido. Ex: 27990001111\n")

    while True:
        cep_str = input("Digite seu CEP: ")
        cep_clean = cep_str.replace("-", "")
        if cep_str.isdigit() and len(cep_str) == 8 or len(cep_str) == 9:
            cep = int(cep_clean)
            break
        print("CEP Invalido! Ele deve conter 8 caracteres. Ex: 29100-000\n")
    
    local = delivery.location(cep)
    if local == 0:
        print(f"\nObrigado pela preferencia, {name}!")
        print(f"Seu numero de telefone: {tel1}")
        print(f"Seu CEP: {cep_str}")
        print("Tempo estimado: 50 a 60 minutos")
        price = valor + 2
        print(f"Valor final: R${price:.2f}\n")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return name, tel, price, date, cep
    else:
        print("\nDesculpe, entregamos apenas em Vila Velha - ES")
        print("Terminando o atendimento...")
        exit()

def new():
    while True:
        print("Deseja fazer outro pedido?\n")
        y = input("> ")
        y = y.strip().lower().rstrip(string.punctuation)
        if y == "sim":
            os.system(f"{clear}")
            return 0
        elif y == "nao":
            print("\nFinalizando o atendimento...")
            print("Obrigado pela preferencia :D")
            return 1
        else:
            print("Tente 'sim' ou 'nao'.")
            continue

def main():
    print("====================================")
    print("Bem vindo a nossa pizzaria!")
    print("====================================")

    database = "database.db"
    connect = db.conectar(database)
    db.create_table(connect)

    while True:
        name, tel, price, date, cep = chatbot()
        db.insert_client(connect, name, tel, price, date, cep)
        connect.close()
        r = new()
        if r == 0:
            continue
        elif r == 1:
            break
        else:
            print("Erro inesperado")

if __name__ == "__main__":
    main()