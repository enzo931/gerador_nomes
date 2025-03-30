import random

# Listas simples de nomes e sobrenomes
nomes_masculinos = [
    "Lucas", "Mateus", "Gabriel", "Pedro", "João", "Arthur", "Enzo", "Miguel",
    "Rafael", "Bruno", "Gustavo", "Thiago", "Leonardo", "Henrique", "Daniel",
    "Vinícius", "André", "Eduardo", "Caio", "Felipe", "Samuel", "Diego", "Vitor",
    "Luiz", "Fernando", "Igor", "Nathan", "Ricardo", "Alexandre", "Jorge", "Otávio",
    "Raul", "Heitor", "Yuri", "Fabrício", "Cauã", "Breno", "Elias", "Matheus",
    "Jonas", "Alan", "Iago", "Luan", "Estêvão", "Jefferson", "Marcos", "Davi",
    "Cássio", "Murilo", "Renan", "Wallace", "Leandro"
]

nomes_femininos = [
    "Maria", "Ana", "Julia", "Beatriz", "Larissa", "Carolina", "Amanda", "Laura",
    "Isabela", "Rafaela", "Camila", "Letícia", "Luana", "Bruna", "Patrícia",
    "Fernanda", "Bianca", "Juliana", "Yasmin", "Sabrina", "Nicole", "Valentina",
    "Cecília", "Gabriela", "Lorena", "Tatiane", "Vitória", "Clara", "Helena",
    "Alícia", "Natália", "Roberta", "Elaine", "Sandra", "Paula", "Renata",
    "Tainá", "Priscila", "Vanessa", "Cristina", "Aline", "Tatiana", "Débora",
    "Joana", "Rebeca", "Manuela", "Melissa", "Marina", "Carla", "Alice", "Estela"
]

sobrenomes = [
    "Silva", "Souza", "Oliveira", "Santos", "Ferreira", "Lima", "Costa", "Almeida",
    "Carvalho", "Ribeiro", "Martins", "Rocha", "Barbosa", "Pereira", "Araújo",
    "Melo", "Castro", "Teixeira", "Fernandes", "Gomes", "Cardoso", "Moreira",
    "Nogueira", "Cavalcante", "Monteiro", "Cunha", "Borges", "Machado", "Pinto",
    "Vieira", "Dias", "Batista", "Campos", "Morais", "Rezende", "Farias", "Tavares",
    "Freitas", "Amaral", "Andrade", "Aguiar", "Assis", "Ramos", "Duarte", "Peixoto",
    "Queiroz", "Bittencourt", "Henriques", "Xavier", "Guimarães", "Torres"
]


def gerar_nome(tipo="misto", incluir_sobrenome=True):
    if tipo == "masculino":
        primeiro_nome = random.choice(nomes_masculinos)
    elif tipo == "feminino":
        primeiro_nome = random.choice(nomes_femininos)
    else:  # misto
        primeiro_nome = random.choice(nomes_masculinos + nomes_femininos)

    if incluir_sobrenome:
        sobrenome = random.choice(sobrenomes)
        return f"{primeiro_nome} {sobrenome}"
    else:
        return primeiro_nome

# Interface no terminal
print("🎲 Gerador de Nomes Aleatórios 🎲")
tipo = input("Tipo (masculino / feminino / misto): ").lower()
quantidade = int(input("Quantos nomes deseja gerar? "))
incluir_sobrenome = input("Incluir sobrenome? (s/n): ").lower() == "s"

print("\n🔹 Nomes Gerados:")
for _ in range(quantidade):
    nome = gerar_nome(tipo=tipo, incluir_sobrenome=incluir_sobrenome)
    print(f" - {nome}")
