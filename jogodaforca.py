import os
import time
import random

def Wait():
    k = input("Pressione enter para continuar")

def Draw(x):
    if x == 6:
        print(" ---|  ")
        print(" |  o  ")
        print(" | /|\ ")
        print(" | / \ ")
        print(" |     ")
        print("_|_    ")
    elif x == 5:
        print(" ---|  ")
        print(" |  o  ")
        print(" | /|\ ")
        print(" |   \ ")
        print(" |     ")
        print("_|_    ")
    elif x == 4:
        print(" ---|  ")
        print(" |  o  ")
        print(" | /|\ ")
        print(" |     ")
        print(" |     ")
        print("_|_    ")
    elif x == 3:
        print(" ---|  ")
        print(" |  o  ")
        print(" | /|  ")
        print(" |     ")
        print(" |     ")
        print("_|_    ")
    elif x == 2:
        print(" ---|  ")
        print(" |  o  ")
        print(" |  |  ")
        print(" |     ")
        print(" |     ")
        print("_|_    ")
    elif x == 1:
        print(" ---|  ")
        print(" |  o  ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print("_|_    ")
    elif x == 0:
        print(" ---|  ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print("_|_    ")

def StringToArray(word):
    wordArray = []
    for x in word:
        wordArray.append(x)
    return wordArray

def HiddenWord(word):
    hiddenWord = []
    for x in word:
        hiddenWord.append("-")
    return hiddenWord
    
def Game():
    storage = ['abacaxi', 'morango', 'kiwi', 'manga', 'melancia']
    word = storage[random.randrange(len(storage))]
    wordArray = StringToArray(word)
    hiddenWord = HiddenWord(word)
    error = 0
    tries = []
    wordLenght = len(word)

    while error < 7 and wordLenght > 0 :
        acerto = False
        os.system('cls')
        Draw(error)

        for x in hiddenWord:
            print(x, end = '')
        print()

        for i in tries:
            print(i, end = ', ')
        print()
        
        guess = input("Digite uma letra: ").lower().strip()

##Checkletrarepetida
        if guess not in tries:
            
            for x in range(len(word)):
                if wordArray[x] == guess:
                    hiddenWord [x] = wordArray[x]
                    acerto = True
                    wordLenght -= 1 
                    
        if acerto == False:
            error += 1

##Tentativas
        tries.append(guess) 
        Wait()
        
##CheckWin
    if error < 7 :
        print ("Você Ganhou!")
        Wait()
    else:
        print("Você perdeu!")
        Wait()

    Wait()
Game()
