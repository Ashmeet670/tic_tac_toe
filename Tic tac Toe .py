#---------------------global variables----------------------------------------------------------------------------
r1=[' ',' ',' ']
r2=[' ',' ',' ']
r3=[' ',' ',' ']
#-----------------game board--------------------------------------------------------------------------------------
def board():



    
    print("Position Board")
    print("----------")
    print("| " + "1" + " | " + "2" + " | "+"3"+ " | ")
    print("----------")
    print("| " +"4" + " | " + "5" + " | "+ "6" + " | ")
    print("----------")
    print("| " + "7" + " | " + "8" + " | "+ "9" + " | ")
    print("----------")
    print("")
    print("")
    print("")
    print("")
    print("Game Board")
    print("----------")
    print("| " + r1[0] + " | " + r1[1] + " | "+r1[2] + " | ")
    print("----------")
    print("| " + r2[0] + " | " + r2[1] + " | "+r2[2] + " | ")
    print("----------")
    print("| " + r3[0] + " | " + r3[1] + " | "+r3[2] + " | ")
    print("----------")
#-----------------------------intake for player 1------------------------------------------------------------------
def takea():
    if a==1:
        r1[0]='X'
    elif a==2:
        r1[1]='X'
    elif a==3:
        r1[2]='X'
    elif a==4:
        r2[0]='X'
    elif a==5:
        r2[1]='X'
    elif a==6:
        r2[2]='X'
    elif a==7:
        r3[0]='X'
    elif a==8:
        r3[1]='X'
    elif a==9:
        r3[2]='X'
    else:
        exit()
#---------------------------------intake for player 2----------------------------------------------------------------
def takeb():
    if b==1:
        r1[0]='O'
    elif b==2:
        r1[1]='O'
    elif b==3:
        r1[2]='O'
    elif b==4:
        r2[0]='O'
    elif b==5:
        r2[1]='O'
    elif b==6:
        r2[2]='O'
    elif b==7:
        r3[0]='O'
    elif b==8:
        r3[1]='O'
    elif b==9:
        r3[2]='O'
    else:
        exit()
#-----------------------------pass condition for player 1--------------------------------------------------------------
def passa():
    if r1[0]=='X' and r1[1]=='X' and r1[2]=='X':
        print('layer 1 wins')
        exit()
    elif r2[0]=='X' and r2[1]=='X' and r2[2]=='X':
        print('Player 1 wins')
        exit()
    elif r3[0]=='X' and r3[1]=='X' and r3[2]=='X':
        print('Player 1 wins')
        exit()
    elif r1[0]=='X' and r2[0]=='X' and r3[0]=='X':
        print('Player 1 wins')
        exit()
    elif r1[1]=='X' and r2[1]=='X' and r3[1]=='X':
        print('Player 1 wins')
        exit()
    elif r1[2]=='X' and r2[2]=='X' and r3[2]=='X':
        print('Player 1 wins')
        exit()
    elif r1[0]=='X' and r2[1]=='X' and r3[2]=='X':
        print('Player 1 wins')
        exit()
    elif r3[2]=='X' and r2[1]=='X' and r1[0]=='X':
        print('Player 1 wins')
        exit()
#----------------------------------pass condition for player 2-----------------------------------------------------------
def passb():
    if r1[0]=='O' and r1[1]=='O' and r1[2]=='O':
        print('Player 2 wins')
        exit()
    elif r2[0]=='O' and r2[1]=='O' and r2[2]=='O':
        print('Player 2 wins')
        exit()
    elif r3[0]=='O' and r3[1]=='O' and r3[2]=='O':
        print('Player 2 wins')
        exit()
    elif r1[0]=='O' and r2[0]=='O' and r3[0]=='O':
        print('Player 2 wins')
        exit()
    elif r1[1]=='O' and r2[1]=='O' and r3[1]=='O':
        print('Player 2 wins')
        exit()
    elif r1[2]=='O' and r2[2]=='O' and r3[2]=='O':
        print('Player 2 wins')
        exit()
    elif r1[0]=='O' and r2[1]=='O' and r3[2]=='O':
        print('Player 2 wins')
        exit()
    elif r1[2]=='O' and r2[1]=='O' and r1[0]=='O':
        print('Player 2 wins')
        exit()
#-------------------------------actual game!!!!!----------------------------------------------------------------------------
print('>>>>>>>CAUTION<<<<<<<<<')
print('THE GAME WILL END IF ANY INVALID OPTION IS SELECTED')
print('PLAYER 1 IS X')
print('PLAYER 2 IN O')
board()
counta=0
countb=0
l=[]
while counta<6 and countb<5:
    a=int(input('Player 1 enter your desired position'))
    if a in l:
        print('repeated value entered')
        exit()
    else:
        l.append(a)
    takea()
    passa()
    board()
    counta+=1
    b=int(input('Player 2 enter your desired position'))
    if b in l:
        print('repeated value entered')
        exit()
    else:
        l.append(b)
    takeb()
    passb()
    board()
    countb+=1
print('IT IS A TIE')
