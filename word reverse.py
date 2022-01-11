#reverse-string program
#This programm will prompt the user to enter a word which will then be reversed and outputted

Endgame=False

def player_input():
    global Endgame
    word = input('Enter a word/sentence you would like to be reversed: ').capitalize()
    if word == 'Stop':
        Endgame=True
        return 
    return word

def reverser(n):
    try:
        print (n[::-1])
    except:
        return 

print('Hello! Welcome to my word reverser game\nType in a word/sentence and the reverse of it will be given back to you\nEnter "Stop" to end the game')    
while not Endgame:
    reverser(player_input())
else:
    print ('Thanks for playing')
