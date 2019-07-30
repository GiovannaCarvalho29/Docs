import time
import os

def Wait():
    k = input("pressione enter para continuar")

def Floors(maxFloor,actualFloor, minFloor):
    for i in range(maxFloor, minFloor-1, -1):
        if i == actualFloor:
            print("(|)", actualFloor)
        else:
            print(" | ", i)

def FromToUp(actualFloor, floorNumber, minFloor):
    for actualFloor in range(actualFloor, floorNumber+1):
        os.system('cls')
        Floors(maxFloor, actualFloor, minFloor)
        time.sleep(1)
    return actualFloor

def FromToDown(actualFloor, floorNumber, minFloor):
    for actualFloor in range(actualFloor, floorNumber-1, -1):
        os.system('cls')
        Floors(maxFloor, actualFloor, minFloor)
        time.sleep(1)
    return actualFloor


##loop
while True:
    os.system('cls')
    maxFloor = int(input("quantos andares tem o predio? "))
    actualFloor=0
    minFloor=-5
    end = False

##CheckSubsolo
    while True:
        x = input("O prédio tem subsolo? <sim/nao>").lower.strip
        if x =="sim":
         minFloor = - int(input("Quantos andares abaixo existem?"))
                break
        elif x == "nao":
        minFloor = 0
                break
   
    while end == False:
        Floors(maxFloor, actualFloor, minFloor)
        #floornumber = minfloor-1
        #while(floornumber<minfloor or floornumber > maxfloor):
        floorNumber = int(input("digite qual andar quer visitar: "))

        #checkposition
        if (floorNumber > actualFloor):
            actualFloor = FromToUp(actualFloor, floorNumber, minFloor)

        elif (floorNumber < actualFloor):
            actualFloor = FromToDown(actualFloor, floorNumber, minFloor)

        print ("você chegou ao seu destino!")
        Wait()

        #check
        x = input("Deseja ir para outro andar? <sim/nao>").lower().strip()
        if x == "sim":
            continue
        elif x == "nao":
            end = True

        
