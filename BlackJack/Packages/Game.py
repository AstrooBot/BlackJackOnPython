import Classes
import Rules21 



while Rules21.replay() == True:
    count = 0
    countIA = 0
    cardPlayed = 0
    cards = Classes.ShuffleCards()
    User = Classes.Player('Jugador', 0)
    Crupier = Rules21.IA('Crupier', 0)
     
    User.count += Rules21.value(cards[cardPlayed],User.count)
    cardPlayed = Rules21.takeCard(User.name, cards[cardPlayed], User.count, cardPlayed)    
    User.count += Rules21.value(cards[cardPlayed],User.count)
    cardPlayed = Rules21.takeCard(User.name, cards[cardPlayed], User.count, cardPlayed)
    print('Empieza turno del Crupier')
    Crupier.count += Rules21.value(cards[cardPlayed],Crupier.count)
    cardPlayed += 1
    print('Termina turno del Crupier')
    print('Empieza turno del Crupier')
    Crupier.count += Rules21.value(cards[cardPlayed],Crupier.count)
    cardPlayed += 1
    print('Termina turno del Crupier')
 
    while cardPlayed <= 52:
        v = input("¿Continuar? Si (-s) No (-n)\n")
        if v == "s":
            User.count += Rules21.value(cards[cardPlayed],User.count)
            cardPlayed = Rules21.takeCard(User.name, cards[cardPlayed], User.count, cardPlayed)
            if User.count > 21:
                break    
        elif v == "n":
            print("Has parado de jugar")
            while Crupier.count != 21:
                if Crupier.count + Rules21.value(cards[cardPlayed],Crupier.count) == 21:
                    Crupier.count += Rules21.value(cards[cardPlayed],Crupier.count)
                else:
                    print('Empieza turno del Crupier')
                    cardPlayed += 1
                    print('Termina turno del Crupier')
            Rules21.winner(User.count, Crupier.count)
            break
    print("Fin del juego\nLa casa siempre ganara, SIEMPRE")
    
