import random

def play():
    user = input("What's your hoice? 'r' for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r', 'p', 'p'])

    if user == computer:
        return 'Its a tie' #empate
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):

    # reutnr true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())