import random
#from replit import clear
#import art
do_want_play_game = True
black_jack =[11,2,3,4,5,6,7,8,9,10,10,10,10]
while do_want_play_game:
  game = input("Do you want to play a game of Blackjack ? Type 'y' or 'n': ").lower()
  if game == 'y':
    user_cards = []
    computer_cards = []
    u_sum = 0 
    c_sum = 0
    #print(art.logo)
    u_first_card = random.choice(black_jack)
    u_second_card = random.choice(black_jack)
    c_first_card = random.choice(black_jack)
    c_second_card = random.choice(black_jack)
    user_cards.append(u_first_card)
    user_cards.append(u_second_card)
    computer_cards.append(c_first_card)
    computer_cards.append(c_second_card)
    for i in user_cards:
      u_sum += i
    for j in computer_cards:
      c_sum += j
    print(f"your cards:{user_cards},current score :{u_sum}")
    print("computer's first card: ",computer_cards[0])
    if (u_sum == 21 and c_sum == 21 ):
      print(f"your final hand:{user_cards},current score :{u_sum}")
      print(f"computer final hand:{computer_cards},current score :{c_sum}")
      print("Match draw")
    elif 11 in user_cards and 10 in user_cards and len(user_cards) == 2:
      print(" user blackjack = 0")
    elif 11 in computer_cards and 10 in computer_cards and len(computer_cards)==2:
      print("computer blackjack = 0")
    elif 11 in user_cards and u_sum >21:
      user_cards.remove(11)
      user_cards.append(1)
    elif 11 in computer_cards and c_sum >21:
      computer_cards.remove(11)
      computer_cards.append(1)
    add_cards = input("Type 'y' to get another card , type 'n' to pass: ").lower()
    if add_cards == 'y':
      new_card = random.choice(black_jack)
      cnew_card = random.choice(black_jack)
      user_cards.append(new_card)
      computer_cards.append(cnew_card)
      u_sum = u_sum + new_card
      c_sum = c_sum + cnew_card
    elif add_cards == 'n':
      print(f"your final hand:{user_cards},current score :{u_sum}")
      print(f"computer final hand:{computer_cards},current score :{c_sum}")
    if(u_sum > 21 and c_sum > 21):
      print(f"your final hand:{user_cards},current score :{u_sum}")
      print(f"computer final hand:{computer_cards},current score :{c_sum}")
      print("you went over and computer went over . both lose")
    elif(u_sum > 21):
      print(f"your final hand:{user_cards},current score :{u_sum}")
      print(f"computer final hand:{computer_cards},current score :{c_sum}")
      print("you went over . You lose")
    elif (u_sum <= 21 and c_sum < u_sum):
      print(f"your final hand:{user_cards},current score :{u_sum}")
      print(f"computer final hand:{computer_cards},current score :{c_sum}")
      print("you won")
    elif (c_sum > 21 and u_sum < c_sum):
      print(f"your final hand:{user_cards},current score :{u_sum}")
      print(f"computer final hand:{computer_cards},current score :{c_sum}")
      print("computer went over. you won")
    elif (u_sum<21 and c_sum <21 and c_sum>u_sum ):
      print(f"your final hand:{user_cards},current score :{u_sum}")
      print(f"computer final hand:{computer_cards},current score :{c_sum}")
      print("you lose")
    else:
      print(f"your final hand:{user_cards},current score :{u_sum}")
      print(f"computer final hand:{computer_cards},current score :{c_sum}")
      print("you lose")
      
  else:
    break
