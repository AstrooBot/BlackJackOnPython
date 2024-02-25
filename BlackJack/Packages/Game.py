import Classes
import Rules21 

count = 0
countIA = 0
cardPlayed = 0
cards = Classes.ShuffleCards()
User = Classes.Player('Jugador', count)
Crupier = Rules21.IA('Crupier', countIA) 

while Rules21.replay() == True:

    count += Rules21.value(cards[cardPlayed])
    cardPlayed = Rules21.takeCard('Jugador', cards[cardPlayed], count, cardPlayed)
    count += Rules21.value(cards[cardPlayed])
    cardPlayed = Rules21.takeCard('Jugador', cards[cardPlayed], count, cardPlayed)
    print('Empieza turno del Crupier')
    countIA += Rules21.value(cards[cardPlayed])
    cardPlayed += 1
    print('Termina turno del Crupier')
    print('Empieza turno del Crupier')
    countIA += Rules21.value(cards[cardPlayed])
    cardPlayed += 1
    print('Termina turno del Crupier')

    while cardPlayed <= 52:
        v = input("¿Continuar? Si (-s) No (-n)\n")
        if v == "s":
            count += Rules21.value(cards[cardPlayed])
            cardPlayed = Rules21.takeCard('Jugador', cards[cardPlayed], count, cardPlayed)       
        elif v == "n":
            print("Has parado de jugar")
            while countIA != 21:
                if countIA + Rules21.value(cards[cardPlayed]) == 21:
                    countIA += Rules21.value(cards[cardPlayed])
                else:
                    print('Empieza turno del Crupier')
                    cardPlayed += 1
                    print('Termina turno del Crupier')
            Rules21.winner(count, countIA)
            break
    print("Fin del juego\nLa casa siempre ganara, SIEMPRE")
    
