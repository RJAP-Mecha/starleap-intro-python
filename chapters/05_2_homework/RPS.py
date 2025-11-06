def get_move(Player):
   valid = False
   while not valid: 
      s = input(Player)
      if s in ["rock", "paper", "scissors"]:
         valid = True 
         return s
      


      

def play_rps():
    P1 = get_move("Player1")
    # P1 = input('Player1')
    # print("Player1")
    # if P1 in ["rock", "paper", "scissors"]:
    # # if P1 == ('rock' or 'paper' or 'scissors'):
    #  print("Player1 ready")
    # else: print("invalid")

    P2 = get_move("Player2")
    # P2 = input('Player2')
    # print("Player2")
    # if P2 in ["rock", "paper", "scissors"]:
    # # if P2 == ('rock' or 'paper' or 'scissors'):
    #  print("Player1 ready")
    # else: print("invalid")

    if P1 == 'scissors' and P2 == 'scissors':
        print('Tie!')
    if P1 == 'paper' and P2 == 'paper':
        print('Tie!')
    if P1 == 'rock' and P2 == 'rock':
        print('Tie!')
    elif (P1 == 'rock') and (P2 == 'paper'):
        print ("Player2 Wins!")
    elif (P2 == 'rock' and P1 == 'paper'): 
        print ("Player1 Wins!")
    elif (P1 == 'scissors' and P2 == 'paper'): 
        print("Player1 Wins!")
    elif (P2 == 'scissors' and P1 == 'paper'): 
        print  ("Player2 Wins!")
    elif (P1 == 'scissors' and P2 == 'rock'): 
        print ("Player2 Wins!")
    elif (P2 == 'scissors' and P1 == 'rock'): 
        print ("Player1 Wins!")

    else:
     print("invalid")
while True:
    play_rps() 