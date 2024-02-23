#Modulo especializado en las reglas del blackjack

import Classes

"""Este crupier ganara sin importar la trampa que sea necesaria.
Al inicio del juego le entrega dos cartas al jugador y espera a que deje de tomar cartas.
Una vez pasa esto, coje cartas del mazo, tomando unicamente las que les de una suma igual a 21. 
De esta forma toma arbitrariamente cartas que le den siempre 21"""
class IA(Classes.Player):
    def badchoice(self, cards, cardPlayed, count):
            self.count = 0
            while self.count <= 21:
                if value(cards[cardPlayed])+countIA <= 21:
                    self.count += value(cards[cardPlayed])
                else: 
                    cardPlayed += 1
            return self.count         
"""forma inicial en la que jugaba el crupier"""
    def goodchoice(self,count):
      #El crupier siempre toma una carta si tiene menos o igual a 16
         if count <= 16:
            des = True
     #El crupier nunca toma una carta si tiene 17 o mas  
        elif count >= 17:
            print("Crupier no tomara mas tarjetas")  
            des = False    
     return des     
     

def value(cards):
    if cards.sym in ['J','Q','K','A']:
        count = 10
    elif cards.sym == 'A' and count < 21:
        count = 11    
    else:
        count = int(cards.sym)
    return count

def takeCard(player,cards, count, cardPlayed):
      print("Empieza turno ", player)
      print('Tarjeta salida: ',cards.sym, ' ', cards.type)  
      if count < 21:
            print("Termina turno ", player)
      if count > 21:
              print("Te has pasado de 21\nHas perdido") 
      cardPlayed += 1        
      return cardPlayed

def winner(count, countIA):
    print("Tus puntos total son:", count)
    print("El total de puntos del Crupier son: ", countIA)
    if countIA < count <= 21 or countIA > count:
        print("Jugador ha ganado")  
    elif count < countIA <= 21 or count > countIA:
        print("Crupier ha ganado")
    else:
        print("Empate")     
    

""" Sample         
cards = Classes.ShuffleCards()
count = 0
cardPlayed = 0
for i in range (5):
    count += value(cards[i])
    cardPlayed = takeCard('Jugador', cards[i], count, cardPlayed)
print(count, cardPlayed)  """  
