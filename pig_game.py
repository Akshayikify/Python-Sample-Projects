import random
print("Hey! Welcome to pig game!")
def roll():
    min_val=1
    max_val=6
    rolled_val=random.randint(min_val,max_val)
    return rolled_val

while True:
    players=input('Enter the number of players (2-4): ')
    if players.isdigit():
        players=int(players)
        if players>=2 and players<=4:
            break
        else:
            print("There must be 2-4 players")
    else:
        print("Invalid. Try again.")

max_score=50
players_score=[0 for i in range(players)] #eg.,[0,0,0,0]

while max(players_score) < max_score:
    for player_idx in range(players):
        print(f'Player number {player_idx+1} is playing the game.')
        print(f'Your score is {players_score[player_idx]}')
        current_score=0
        while True:
            should_play=input('Would you like to roll dice:').lower()
            if should_play !='y':
                break
            value=roll()
            if value==1:
                print("You rolled 1! You are done.")
                break
            else:
                current_score+=value
                print("You rolled a value ",value)
            print("Your score is ",current_score)
        players_score[player_idx]=current_score
        print("Your total score is ",players_score[player_idx])

max_score=max(players_score)
winning_idx=players_score.index(max_score)
print(f"Player number {winning_idx+1} won with the score {max_score}")
