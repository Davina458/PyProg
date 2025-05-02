'''The function takes two integer parameters and returns a string that says who won which should be either “player1” or “player2”. The winner depends on the rolls being odd or even as follows: 
If player 1 rolls an even, player 2 must roll an odd, and vice versa.  
Hence, both numbers being odd or both numbers being even means player 1 wins, 
one odd and one even means player 2 wins.  
Test your program with a reasonable set of combinations of dice roll. 
'''
def checker(p1roll, p2roll):
    if p1roll % 2 == 0 and p2roll % 2 == 0 or p1roll % 2 != 0 and p2roll % 2 != 0:
        return "player 1"
    else:
        return "player 2"
    
print(checker(1,2)) # player 2 wins
print(checker(2,2)) # player 1 wins
    
print(checker(1,6)) # player 2 wins
print(checker(3,5)) # player 1 wins