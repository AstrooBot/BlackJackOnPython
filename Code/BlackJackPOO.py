"""The next code is a simulation of the blacjack game which a user plays with the machine (as a Crupier)""""

import random

#incializamos las variables
cardList = []  
cardPlayed = 1
Simbolos = ["A", "J", "Q", "K","10","9","8", "7", "6", "5", "4", "3", "2"]
Valores = [11,10,10,10,10,9,8,7,6,5,4,3,2]

#Creamos la clase que contiene los atributos que cada tarjeta debe tener
class Card:
    Value = 0
    Type = 'Default'
    Symbol = '0'
    
#Creamos las funciones para el jugador y la maquina    
def takeCard(cardList, cardPlayed, count):
# si el jugador supera los 21, pierde automaticamente    
    if(count < 21):
     print('Tarjeta salida: ' + cardList[cardPlayed].Symbol +' de '+cardList[cardPlayed].Type)
    else:
     print("Te has pasado de 21\nHas perdido")
     return False

def crupier(countIA, cardPlayed):
     print("Empieza turno del crupier")
     #El crupier siempre toma una carta si tiene menos o igual a 16
     if countIA <= 16:
       des = True
       print("Crupier ha tomado una tarjeta")
       print("Finaliza turno del Crupier")
     #El crupier nunca toma una carta si tiene 17 o mas  
     elif countIA >= 17:
      des = False    
      print("Crupier no tomara mas tarjetas")
      print("Finaliza turno del Crupier")
     return des     
#Creamos cada mazo de tipo de tarjeta y las almacenamos todas en una lista
i = 0
for var in range(13):
    var = Card()
    var.Type = 'Corazón'
    var.Value = Valores[i]
    var.Symbol = Simbolos[i]
    cardList.append(var)
    i += 1
i = 0    
for var in range(13):
    var = Card()
    var.Type = 'Picas'
    var.Value = Valores[i]
    var.Symbol = Simbolos[i]
    cardList.append(var)    
    i += 1
i = 0    
for var in range(13):
    var = Card()
    var.Type = 'Trebol'
    var.Value = Valores[i]
    var.Symbol = Simbolos[i]
    cardList.append(var)    
    i += 1
i = 0    
for var in range(13):
    var = Card()
    var.Type = 'Diamantes'
    var.Value = Valores[i]
    var.Symbol = Simbolos[i]
    cardList.append(var)    
    i += 1    
 #Preparativos del juego  
again = True
while again == True:
 random.shuffle(cardList)
 count = 0
 countIA = 0
 #Empieza el juego
 takeCard(cardList, cardPlayed, count)
 count += cardList[cardPlayed].Value
 cardPlayed += 1
 if crupier(countIA, cardPlayed) == True:
   countIA += cardList[cardPlayed].Value

 while cardPlayed <= 52:
    print("Empieza turno del jugador")
    v = input("¿Continuar? Si -s No -n\n")
    if v == "s":
        if(takeCard(cardList, cardPlayed,count) == False):
            break
        count += cardList[cardPlayed].Value
        if(count > 21 and cardList[cardPlayed].Symbol == 'A'):
            count -= 10
        cardPlayed += 1
        print("Termina turno del jugador")
        if crupier(countIA, cardPlayed) == True:
         countIA += cardList[cardPlayed].Value
         if(countIA > 21 and cardList[cardPlayed].Symbol == 'A'):
            count -= 10
         cardPlayed += 1
    elif v == "n":
         print("Has parado de jugar")
         while crupier(countIA, cardPlayed) == True:
             countIA += cardList[cardPlayed].Value
             if(countIA > 21 and cardList[cardPlayed].Symbol == 'A'):
               count -= 10
             cardPlayed += 1
         print("Tus puntos total son:", count)
         print("El total de puntos del Crupier son: ", countIA)
         if countIA < count <= 21 or countIA > 21:
             print("Jugador ha ganado")
         elif count < countIA <= 21 or count > 21:
             print("Crupier ha ganado")
         else:
             print("Empate")
         break
 print("El juego ha terminado")
 game = input("¿Volver a jugar? Si -s No -n\n")
 if (game == 's'):
    again = True
 elif(game == 'n'):
    again == False
    break
print("Gracias por jugar")  