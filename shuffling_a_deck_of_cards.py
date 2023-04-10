import random
card_deck = []

card_values = [2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K", "A"]
card_suits = ["s", "h", "d", "c"]

def create_deck():
    for value in card_values:
        for suit in card_suits:
            card_deck.append("".join([str(value), suit]))
    if len(card_deck) < 51:
        pass
    else:
        print(card_deck)

def shuffle():
    create_deck()
    random.shuffle(card_deck)
    print(card_deck)

def main() -> None:
    shuffle()

if __name__ == "__main__":
    main()