#Modulo especializado en las reglas del blackjack

import Classes

class IA(Classes.Player):
    
    def badchoice(countIA,count, cards,cardPlayed):
        while count < countIA <= 21:
                if countIA + value(cards[cardPlayed]) >= count and countIA + value(cards[cardPlayed]) <= 21 :
                    countIA += value(cards[cardPlayed])
                else:
                    print('Empieza turno del Crupier')
                    cardPlayed += 1
                    print('Termina turno del Crupier')
        return countIA                  

    """forma inicial en la que jugaba el crupier"""

    def goodchoice(count):
    #El crupier siempre toma una carta si tiene menos o igual a 16
        if count <= 16:
            des = True
    #El crupier nunca toma una carta si tiene 17 o mas  
        elif count >= 17:
            print("Crupier no tomara mas tarjetas")  
            des = False    
        return des     
     
def ass(cards):     
    if cards.sym == 'A':
        return True
    return False    


def value(cards,count):
    if cards.sym in ['J','Q','K']:
        count = 10
    elif ass(cards) == True and count+11 <= 21:
        count = 11 
    elif ass(cards) == True and count+11 > 21:
        count = 1        
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
    if countIA < count <=21 or countIA > 21 and count <= 21 :
        print("Jugador ha ganado")  
    elif count < countIA <= 21 or 21 > count:
        print("Crupier ha ganado")
    else:
        print("Empate") 

def replay():
    print("Bienvenido a BlackJacjPy\nEl unico casino en el que lo unico que pierdes es tu tiempo")
    round = input("¿Quieres empezar a jugar Blackjack Si (-s) No (-n)\n") 
    if round == 's':
        again = True
    elif round == 'n':
        again = False
        print("Gracias por jugar")
    return again

"""def init(count, cards, cardPlayed,countIA):
al intentar poner esta funcion en reemplazo del codigo de 13 a 24, resulta en un sobrepaso del indice
de la lista"""


