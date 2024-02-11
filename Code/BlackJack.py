import random
Pintas = ["picas", "trebol", "diamantes", "corazones"]
Simbolos = ["A", "J", "Q", "K","10","9","8", "7", "6", "5", "4", "3", "2"]
Valores = [10,10,10,10,10,9,8,7,6,5,4,3,2]
# Lista por compresion
Mazo2 = list(zip(Valores,Simbolos))
Mazo = [(u,p) for u in Mazo2 for p in Pintas] 
random.shuffle(Mazo)
i = 0
while i <= 52:
    v = input("¿Continuar? Si -s No -n")
    if v == "s":
        print(Mazo[i])
        i += 1
    elif v == "n":
         print("El juego ha terminado")
         break
# Es imposible continuar con este codigo porque no se puede leer el valor entero de cada carta
