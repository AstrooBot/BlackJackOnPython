#Crear clases juego //con metodos para dar y contar cartas Clase init //para crear y revolver las cartas asi como mantener el conteo por debajo de 52 y volver a jugar
#Crear clase de jugador y de crupier 
#solo dejar simbolos y tipos 
#import os
#cardList = [Card(v,x) for v in ['A','K','Q','J']+[str(x) for x in range(2,11)]]
#os.system('start pic.png')
import random
class Card:
    def __init__(self,sym,type):
        self.sym = sym
        self.type = type

    def value(self):
        #for i in ['J','Q','K','A']:
        if 'A' == self.sym or 'K' == self.sym or 'Q' == self.sym or 'J' == self.sym:
                count = 10
        else:
                count = int(self.sym)
        return count 
    def takeCard(self, cardPlayed, count):
            print('Tarjeta salida: ',self.sym, ' ', self.type)
            count = self.value()
            cardPlayed += 1
            return count 

class Player:
    def __init__(self, name):
        self.name = name
    def takeCard(self,card, cardPlayed, count):
        print("Empieza turno ", self.name)
        if count < 21:
            count +=card.takeCard(cardPlayed,count)
            print("Termina turno ", self.name)    
        elif count > 21 and self.name == 'Jugador':
            print("Te has pasado de 21\nHas perdido")
        if count+1 <= 21 and card.sym == 'A':
            count +=1     
        return count

class IA(Player):
    def desicion(self,count):
     #El crupier siempre toma una carta si tiene menos o igual a 16
     if count <= 16:
       des = True
     #El crupier nunca toma una carta si tiene 17 o mas  
     elif count >= 17:
      print("Crupier no tomara mas tarjetas")  
      des = False    
     return des  

class game:
    def init(self):             
        count = 0
        countIA = 0
        cardPlayed = 1
        cardList = [Card(v,x) for v in [str(v) for v in range(2,11)]+['J','Q','K','A'] for x in ['♥','♠','♣','♦']]
        random.shuffle(cardList) 
        User = Player('Jugador')
        Crupier = IA(Player('Crupier')) #no muestra el nombre cupier 
        count = User.takeCard(cardList[cardPlayed],cardPlayed,count)
        cardPlayed +=1
        count = User.takeCard(cardList[cardPlayed],cardPlayed,count)
        cardPlayed +=1
        countIA = Crupier.takeCard(cardList[cardPlayed],cardPlayed,countIA)
        cardPlayed +=1
        while cardPlayed <= 52: 
            if Crupier.desicion(countIA) == True:
                countIA = Crupier.takeCard(cardList[cardPlayed],cardPlayed,countIA)
                cardPlayed +=1
            v = input("¿Continuar? Si (-s) No (-n)\n")
            if v == "s":
                count = User.takeCard(cardList[cardPlayed],cardPlayed,count)
                cardPlayed +=1
            elif v == "n":
                print("Has parado de jugar")
                while Crupier.desicion(countIA) == True:
                    countIA = Crupier.takeCard(cardList[cardPlayed],cardPlayed,countIA)
                    cardPlayed +=1 
                print("Tus puntos total son:", count)
                print("El total de puntos del Crupier son: ", countIA)
                if countIA < count <= 21 or countIA > 21:
                    print("Jugador ha ganado")  
                elif count < countIA <= 21 or count > 21:
                    print("Crupier ha ganado")
                    
                else:
                    print("Empate")  
                break
        round = input("¿Volver a jugar? Si (-s) No (-n)\n")
        if round == 's': 
            return True 
        else: 
            return False    

if __name__ == '__main__': 
    print("Bienvenido a BlackJacjPy\nEl unico casino en el que lo unico que pierdes es tu tiempo")
    round = input("¿Quieres empezar a jugar Blackjack Si (-s) No (-n)\n") 
    if round == 's':
        again = True
        while again == True:
            Game = game()
            again = Game.init()
    print("Gracias por jugar")     


