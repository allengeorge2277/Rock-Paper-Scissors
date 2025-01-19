
# ******************* Childhood Favorite Game ********************************************
# ******************** Rock-Paper-Scissors ***********************************************

#   r - Rock, p - Paper, s - Scissors
#   Taking input from the user, which also checks invalid choice that are not 'r','p','s'
#   Generate a random number (0, 1, 2) for the computer's choice.
#   A function to generate choice for computer in term of 'r','p','s'
#   where 0 --> r, 1 --> p and 2 --> s.
#   A function to determine the result.
#   Continue the game unless the user enters 'n' to stop or 'y' to continue.
#   Display the scores for both the user and the computer.

# **************************************************************************************** 
# ******************* Time to refresh your mind!! ****************************************


import random

def computerChoice(value):
    if value == 0:
        return 'r'
    elif value == 1:
        return 'p'
    else:
        return 's'

def finalResult(new_choice):
    human_win = [['p','r'],['s','p'],['r','s']]
    if new_choice in human_win: return 'H'
    else: return 'C'

human_count = 0
computer_count = 0

while True:
    
    human = input("\nRock, Paper, Scissors (r,p,s):").lower()
    if human not in ['r','p','s']:
        print('Invalid choice')
        continue
    
    computer = computerChoice(random.randrange(0,3))
    new_choice = [human,computer]
    forOutput = {
        'r' : '🪨',
        'p' : '📜',
        's' : '✂️'
    }

    print("You: ",forOutput[human])
    print("Computer: ",forOutput[computer])
    
    if human == computer:
        print('\nIts a tie 😊')
    else:
        result = finalResult(new_choice)
        if result == 'H':
            human_count += 1
            print('\nYou win!!')
        else:
            computer_count += 1
            print('\nComputer won!!')
    
    while True:
        end = input('\nWant to continue? (y -> yes|n -> no): ').lower()
        if end in ['y','n']:
            break
        print('Give valid input, either "y" or "n"')

    if end == 'n': 
        print('\nFINAL SCORE')
        print(f'Human: {human_count}')
        print(f'Computer: {computer_count}')
        break
