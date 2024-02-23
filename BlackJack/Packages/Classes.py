#Modulo especializado en la creacion de las cartas y jugador
import random

class Card:
    def __init__(self,sym,type):
        self.sym = sym
        self.type = type


def ShuffleCards():
       list = [Card(v,x) for v in [str(v) for v in range(2,11)]+['J','Q','K','A'] for x in ['♥','♠','♣','♦']]
       random.shuffle(list) 
       return list


class Player:
    def __init__(self, name, count):
        self.name = name
        self.count = count
        
"""Sample to use Card class
cards = ShuffleCards()
count = 0
for i in cards:
    count += 1
    print(i.sym,i.type, '\n' )
    
print(count)"""  
