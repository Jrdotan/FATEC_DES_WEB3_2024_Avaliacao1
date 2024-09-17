import requests
from collections import Counter

# rank de pontuações de poker
# straights e flushes não foram implementados pela complexidade de implementação
# high card significa impate
# eu falhei, eu falhei orlando...

RANKINGS = {
    'high_card': 1, 
    'one_pair': 2,
    'two_pair': 3,
    'three_of_a_kind': 4,
    'straight': 5,
    'flush': 6,
    'full_house': 7,
    'four_of_a_kind': 8,
    'straight_flush': 9,
    'royal_flush': 10
}

def conseguir_baralho():
    URL = 'https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
    deck = requests.get(URL)
    return deck.json()

def pegar_carta(deck_id, count):
    URL = f'https://www.deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}'
    draw = requests.get(URL)
    return draw.json()



def avaliar_mao(cartas):
    valores = [card['value'] for card in cartas]


  

    # Conta frequência de pares
    valor_count = Counter(valores)
    counts = sorted(valor_count.values(), reverse=True)
    
    if counts[0] == 4:
        return 'four_of_a_kind'
    if counts[0] == 3 and counts[1] == 2:
        return 'full_house'
    if counts[0] == 3:
        return 'three_of_a_kind'
    # distingue dois pares e conta a frequência
    if counts.count(2) == 2:
        return 'two_pair'
    if counts[0] == 2:
        return 'one_pair'
    
    return 'high_card'

def main():
    # prepara o deck
    meu_baralho = conseguir_baralho()
    deck_id = meu_baralho.get('deck_id')

    # puxa cartas para player e para o CPU
    jogador = pegar_carta(deck_id, 5).get('cards')
    cpu = pegar_carta(deck_id, 5).get('cards')
    
    # Mostra as mãos
    print(f"Sua mão: {[card['code'] for card in jogador]}")
    print(f"Mão da CPU: {[card['code'] for card in cpu]}")

    # Determine rankings das cartas de cada jogador
    jogador_rank = avaliar_mao(jogador)
    cpu_rank = avaliar_mao(cpu)

      
    # Compara mãos do player com o CPU
    if RANKINGS[jogador_rank] > RANKINGS[cpu_rank]:
        print(f"Você ganhou com {jogador_rank.replace(' ', ' ')}, se sinta foda!")
    elif RANKINGS[jogador_rank] < RANKINGS[cpu_rank]:
        print(f"A CPU ganhou com {cpu_rank.replace(' ', ' ')}! ruim demaisKKKK")
    else:

        print("Empate!")

        

if __name__ == "__main__":
    main()

