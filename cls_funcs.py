import random

suits = ('Hearts','Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
          'Jack':10,'Queen':10,'King':10,'Ace':11}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:

    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                a = Card(suit, rank)
                self.cards.append(a)

    def deal_one(self):
        return self.cards.pop()

    def deal_two(self):
        deal_one = self.cards.pop()
        deal_two = self.cards.pop()
        return [deal_one, deal_two]

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

class Player:
    def __init__(self,name):
        self.name = name
        self.money = 1000
        self.all_cards = []

    def sum_cards(self):
        cont = 0
        for card in self.all_cards:
            cont += card.value
        return cont


    def add(self,cards):
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def remove_card(self):
        return self.all_cards.pop(0)

    def bet(self,value):
        self.money -= value
        return self.money

    def gain_money(self,value):
        self.money += value

def set_game(player,dealer):
    mydeck = Deck()
    mydeck.shuffle()
    player.all_cards = []
    dealer.all_cards = []
    return mydeck

def build_player_hand(deck,player):
    player_cards = deck.deal_two()
    player.add(player_cards)
    if player.name == 'Dealer':
        print(f"Dealer's uncovered card is: {player.all_cards[0]}\n")
        print("#-------------------------------------------#\n")
    else:
        print(f'These are your cards: {player.all_cards[0]} and {player.all_cards[1]}')

def change_ace_value(player):

    num_cards = len(player.all_cards)
    if num_cards == 2:
        if player.all_cards[0].rank == 'Ace' or player.all_cards[1].rank == 'Ace':
            rank_list = [player.all_cards[0].rank, player.all_cards[1].rank]
            ace_index = rank_list.index('Ace')
            ace_value = input('Do you want your ace to value 1? (yes/no): ')
            if ace_value == 'y':
                player.all_cards[ace_index].value = 1
            elif ace_value == 'n':
                player.all_cards[ace_index].value = 11

        elif player.all_cards[0].rank == 'Ace' and player.all_cards[1].rank == 'Ace':
            player.all_cards[0].value = 1

    elif num_cards > 2:
        if player.all_cards[-1].rank == 'Ace':
            ace_value = input('Do you want your ace to value 1? (yes/no): ')
            if ace_value == 'yes':
                player.all_cards[-1].value = 1
            elif ace_value == 'no':
                player.all_cards[-1].value = 11

def check_enough_money(money):

    print(f"Starting money: {money}")
    if money == 0:
        print("You don't have enough money! The game is over.")
        return 0

    while True:

        try:
            bet = int(input("What's your bet?: "))
            if bet > money:
                print("Sorry, you don't have enough money!")
            else:
                break
        except ValueError:
            print("Sorry, wrong input!")

    return bet

def playAgain(win=True, play_again=True):

    answer = input('Play again? (y/n)')
    if answer == 'n':
        play_again = False

    return win, play_again
