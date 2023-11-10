import random
import os

# Lista de dicionários com palavras em português como chave e em inglês como valor
dicionarios = [
    {'cachorro': 'dog'},
    {'gato': 'cat'},
    {'banana': 'banana'},
    {'computador': 'computer'},
    # Adicione mais palavras conforme necessário
]

def limpar_tela():
    # Função para limpar a tela do console
    os.system('cls' if os.name == 'nt' else 'clear')

def jogo():
    dicionario_atual = None  # Inicializa a variável fora do loop

    while True:
        # Limpa a tela a cada iteração
        limpar_tela()

        # Escolhe aleatoriamente um dicionário da lista, garantindo que não seja o mesmo da iteração anterior
        dicionario_atual = random.choice([d for d in dicionarios if d != dicionario_atual]) if dicionario_atual is not None else random.choice(dicionarios)
        palavra_portugues = list(dicionario_atual.keys())[0]
        palavra_ingles = list(dicionario_atual.values())[0]

        # Solicita ao usuário a tradução da palavra em português
        resposta_usuario = input(f"Traduza a palavra '{palavra_portugues}' para inglês: ").lower()

        # Verifica se a resposta do usuário está correta
        if resposta_usuario == palavra_ingles.lower():
            print("Parabéns! Você acertou!\n")
        else:
            print(f"Ops, resposta incorreta. Tente novamente.\n")

if __name__ == "__main__":
    jogo()
