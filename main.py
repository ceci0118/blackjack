'''
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

1. two players
mycards = []
computercards = []

2. first two cards each player
addcard(player)

3. computer card deck only show one card

4. first round
  while player continue
  a. player
    ask player if they want one more card
    if yes: addcard()
    if no: continue = false
  
  while computer continue
  b. computer
    if computer has 11: addcard()
      if sum > 21: 11 = 1
    
    check computer deck sum
    if sum < 20 : addcard()
    if sum >= 20: continue = false

5. when two continue are both false,compare final result
  if sum(player) == sum(computer):
    result = draw
  elif sum(player) > sum(computer) and sum(player) <= 21:
    result = win
  else:
    result = lose

'''
import random
import art
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def addcard(player):
  player.append(random.choice(cards))

def check_sum(player):
  if 11 in player and sum(player) > 21:
    player.remove(11)
    player.append(1)
  return sum(player)

#start the game
root = True
start = False
while root:
  start_game = input("Do you want to play a blackjack game? Type 'y' to play or type 'n' to exit: ").lower()
  if start_game == 'y':
    start = True
    clear()
  elif start_game != 'n':
    print("Please enter 'y' or 'n' to choose.")
  else:
    print("Goodbye")
    quit()


  #first round
  if start:
    player = []
    computer = []

    addcard(player)
    addcard(player)
    addcard(computer)
    addcard(computer)

    print(art.logo)

    player_continue = True
    while player_continue:

      print(f"Your cards: {player}, current score: {sum(player)}")
      print(f"Computer's first card: {computer[0]}")

      one_more_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

      if one_more_card == 'y':
        addcard(player)
        if check_sum(player) > 21:
          player_continue = False
      elif one_more_card == 'n':
        player_continue = False
      else:
        print("Please enter 'y' or 'n' to choose.")

    computer_continue = True
    while computer_continue:
      if check_sum(computer) >= 18:
        computer_continue = False
      else:
        addcard(computer)

  if not player_continue and not computer_continue:
    if check_sum(player) == check_sum(computer):
      result = "Draw"
    elif check_sum(player) > check_sum(computer) and check_sum(player) <= 21:
      result = "You win"
    elif check_sum(player) < check_sum(computer) and check_sum(computer) > 21:
      result = "You win"
    else:
      result = "You lose"

    print(f"Your final hand {player}, final score {check_sum(player)}")
    print(f"Computer's final hand {computer}, final score {check_sum(computer)}")
    print(result)
