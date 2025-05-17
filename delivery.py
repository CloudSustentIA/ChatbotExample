import requests

def location(cep):
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if response.status_code == 200:
        dados = response.json()
        try:
            if dados['localidade'] == "Vila Velha":
                return 0
            else:
                return 1
        except KeyError:
            print("CEP Invalido ou nao encontrado! Entregamos apenas em Vila Velha - ES")
    else:
        print("Server Error: [404]")
        return 2