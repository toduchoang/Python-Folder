import random

print('This is a rock paper scissor game.')
move_list = ['Rock','Paper','Scissor']
player_score = 0
computer_score = 0 
loop_times = 0

while True:
    print('Please type in your move (please type Rock/Paper/Scissor):')
    # Ask for user's input
    player_move = input()
    if player_move not in move_list:
        print(' ')
        print('Oops did you have a typo? Please type in your move again.')
    else:
        # Generate computer's move randomly
        computer_number = random.randint(1,3)
        if computer_number == 1:
            computer_move = 'Rock'
        elif computer_number == 2:
            computer_move = 'Paper'
        elif computer_number == 3:
            computer_move = 'Scissor'

        # Mapping all possible scenarios of the game
        if computer_move == player_move:
            print(' ')
            print('It is a tie')
            print(f'New score (Player - Comp): {player_score} - {computer_score}')
        elif computer_move == 'Scissor' and player_move == 'Paper':
            print(' ')            
            print(f'Computer move is {computer_move}')
            print('Computer wins.')
            computer_score += 1    
            print(f'New score (Player - Comp): {player_score} - {computer_score}')
        elif computer_move == 'Paper' and player_move == 'Rock':
            print(' ')  
            print(f'Computer move is {computer_move}')
            print('Computer wins.')
            computer_score += 1 
            print(f'New score (Player - Comp): {player_score} - {computer_score}')
        elif computer_move == 'Rock' and player_move == 'Scissor':
            print(' ')  
            print(f'Computer move is {computer_move}')
            print('Computer wins.')
            computer_score += 1 
            print(f'New score (Player - Comp): {player_score} - {computer_score}')
        else:
            print(' ')  
            print(f'Computer move is {computer_move}')
            print('Player wins')
            player_score += 1    
            print(f'New score (Player - Comp): {player_score} - {computer_score}')
        
        # Keep track of number of times the loop is run and the user's win percentage.
        loop_times += 1
        win_percentage = round(player_score/loop_times*100,2)
        
        # Check if the user wants to play again
        while True:
            print(' ')
            print('Do you want to play again (Please type y or n):')
            user_decision = input()
            if user_decision not in ['y','n']:
                print('Oops did you have a typo? Please confirm your decision again.')
            else:
                break
        if user_decision == 'y':
            continue
        if user_decision == 'n':
            # Provide a summarization if the player decides to end the game
            print(' ')              
            print('* * * * * * * * * * * * *')
            print(f'You play {loop_times} times with the computer')
            print(f'Your win percentage is {win_percentage}%')
            print('* * * * * * * * * * * * *')
            break
            
        

