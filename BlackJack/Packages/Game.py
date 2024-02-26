import Classes
import Rules21 



while Rules21.replay() == True:

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
    print(Crupier.count)
    while cardPlayed <= 52:
        v = input("¿Continuar? Si (-s) No (-n)\n")
        if v == "s":
            User.count += Rules21.value(cards[cardPlayed],User.count)
            cardPlayed = Rules21.takeCard(User.name, cards[cardPlayed], User.count, cardPlayed)
            if User.count > 21:
                break    
        elif v == "n":
            print("Has parado de jugar")
            print(Crupier.count)
            Crupier.count = Crupier.badchoice(Crupier.count,User.count,cards,cardPlayed)
            Rules21.winner(User.count, Crupier.count)
            break
    print("Fin del juego\nLa casa siempre ganara, SIEMPRE")
    
