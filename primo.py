print("esse programa foi desenvolvido com o intuito",
      "de demonstrar um posicionamento de um batalhão", sep='\n')
x = int(input("digite um numero de soldados: "))
filas = 0
n = 0
while x > 0:
    n += 1
    n += n
    filas += 1
    print("o número de fileiras formadas foi", filas)
if x < 0:
    print("e restaram", x + n, "soldados na ultima fileira.")

