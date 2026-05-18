from cls_funcs import *
"""
Use Object-Oriented Programming to create a BlackJack game

Players: Computer dealer and Human player

Starting from a deck of cards 52 shuffled cards: the human player has an initial sum of money and from that a bet is 
placed based on the value of the cards.
The player starts with 2 cards, so does the dealer (one of the cards is covered), the player goes first in the gameplay.

Player goal: get closer to a value of 21 than the dealer does, value = sum of the player's cards'value 

2 actions the player can do: hit = receive another card from the deck, stay = stop receiving cards

Then it's computer turn: if player < 21 the computer hits until they either beat the player or the dealer busts
if the player busts before the computer plays the bet is lost

if the dealer lose the player gets bet*2

Jack King Queen value is 10
Ace 11 or 1 (choice of the player)

"""

play_again = True

print('#---------- WELCOME TO BLACKJACK! ----------#\n')

player = Player('Player')
dealer = Player('Dealer')

while play_again:

      # Start: player
      mydeck = set_game(player,dealer)
      build_player_hand(mydeck, player)
      change_ace_value(player)
      player_score = player.sum_cards()

      print(f'Your initial score is: {player_score}')
      if player_score == 21:
          print("Player wins!")
          _, play_again = playAgain()
          continue

      # Start: dealer
      build_player_hand(mydeck, dealer)
      dealer_score = dealer.sum_cards()
      bet = check_enough_money(player.money)
      if bet == 0:
          play_again = False
          break
      player.bet(bet)
      print(f'Remaining money: {player.money}')
      print("#-------------------------------------------#\n")

      win = False
      # Player turn
      while True:

          deal = input('Deal? (y/n)')

          if deal == 'n':
              if player_score == 21:
                  print('You won!')
                  player.money += bet*2
                  win, play_again = playAgain(win,play_again)
                  break
              print(f'Final score: {player_score}')
              break

          else:
              new_card = mydeck.deal_one()
              player.add(new_card)
              change_ace_value(player)
              player_score = player.sum_cards()
              print(f'Score: {player_score}')
              if player_score == 21:
                  print('You won!')
                  player.money += bet*2
                  win, play_again = playAgain(win,play_again)
                  break
              elif player_score > 21:
                  print(f'BUST! Final sum: {player_score}')
                  win, play_again = playAgain(win,play_again)
                  break


      print("\n")
      print("#-------------------------------------------#\n")
      # Dealer's turn
      dealer_bust = False
      if not win:
          print("It's dealer's turn")
          print(f"Score: {dealer_score}")
          while dealer_score <= player_score:
              new_card = mydeck.deal_one()
              dealer.add(new_card)
              dealer_sum = dealer.sum_cards()
              if dealer_sum > 21:
                  print(f'BUST! Final sum: {dealer_sum}')
                  print('You won!')
                  player.money += bet*2
                  win, play_again = playAgain(win,play_again)
                  dealer_bust = True
                  break

          if dealer_score > player_score and dealer_bust == False:
              print('The dealer won!')
              win, play_again = playAgain(win,play_again)





