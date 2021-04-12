import random
import art
from replit import clear

def deal_cards():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)

def sum_score(cards):
  if sum(cards)==21:
    return 0
  if sum(cards)>21:
    if 11 in cards:
      cards.remove(11)
      cards.append(1)  
  return sum(cards)  

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose "
  if user_score == computer_score:
    return "Draw "
  elif computer_score == 0:
    return "Lose, opponent has Blackjack "
  elif user_score == 0:
    return "Win with a Blackjack "
  elif user_score > 21:
    return "You went over. You lose "
  elif computer_score > 21:
    return "Opponent went over. You win "
  elif user_score > computer_score:
    return "You win "
  else:
    return "You lose "

def blackjack():
  print(art.logo)
  user_cards=[]
  comp_cards=[]
  is_game_over=False
  for _ in range(2):
    user_cards.append(deal_cards())
    comp_cards.append(deal_cards())


  while not is_game_over:
    user_score=sum_score(user_cards)
    comp_score=sum_score(comp_cards)

    print(f"Your cards are : {user_cards} and your current score is {user_score}")
    print(f"The computers first card is {comp_cards[0]}")
      

    if user_score==0 or user_score>21 or comp_score==0 or comp_score>21:
      is_game_over=True
    else:
      y=input('Do you want to pick another card? : \n')
      if y=='y':
        user_cards.append(deal_cards())
      else:
        is_game_over=True  

  if user_score>21 and comp_score<21 and (len(comp_cards)+1)==len(user_cards) or (comp_score>21 and user_score<21):
    is_game_over=True
  else:  
    while comp_score!=0 and comp_score<19:
      comp_cards.append(deal_cards())
      comp_score=sum_score(comp_cards)

  print(f"Your final hand is {user_cards} and your final score is {user_score}")
  print(f"Computer's final hand is {comp_cards} and computers final score is {comp_score}")

  print(compare(user_score,comp_score))

while input('Do you want to play ? : ')=='y':
  clear()
  blackjack()


'''import random
from replit import clear

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def blackjack():
  user_cards=[]
  comp_cards=[]
  for _ in range(2):
    user_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))
  should_continue=True

  while should_continue:
    user_score=sum(user_cards)
    comp_score=sum(comp_cards)


    print(f" Your cards are {user_cards} and your score is {user_score}")
    print(f" Computer's cards are {comp_cards} and score is {comp_score}")

    if user_score==21 or comp_score==21:
      should_continue=False  

    if comp_score>21:
      if len(comp_cards)==2:
        for i in comp_cards:
          if i == 11:
            comp_cards.remove(11)
            comp_cards.append(1)
            comp_score=sum(comp_cards)  
      should_continue=False        
    else:
      if input('Do you want to select another card: ')=='y':
        comp_cards.append(random.choice(cards))
      else:
        should_continue=False    
    
    if user_score>21:
      if len(user_cards)==2:
        for i in user_cards:
          if i == 11:
            user_cards.remove(11)
            user_cards.append(1)
            user_score=sum(user_cards)
      should_continue=False 
    

    else:
      if input('Do you want to select another card: ')=='y':
        user_cards.append(random.choice(cards))
      else:
        should_continue=False  

  while comp_score<17 and comp_score!=21:
    comp_cards.append(random.choice(cards))
    comp_score=sum(comp_cards)

  print(f"Your final hand is {user_cards} and your final score is {user_score}")
  print(f" Computer's final hand is {comp_cards} and your final score is {comp_score}")


  if user_score>21 and comp_score>21:
    print('You went over , You lose')

  if user_score==21 and comp_score!=21:
    print('You win with a Blackjack')
  elif comp_score==21 and user_score!=21:
    print('Opponent hits a Blackjack.You lose')   
  elif comp_score>21 and user_score<21:
    print('Opponent went over, YOU WIN')
  elif user_score>21 and comp_score<21:
    print('You went over.You lose')      

  elif user_score<21 and comp_score<21:
    if user_score==comp_score:
      print('Draw')
    elif user_score>comp_score:
      print('You win')
    else:
      print('You lose')        

while input('Do you want to play?\n')=='y':
  clear()
  blackjack()'''





    











