import random as rd
#deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#userexit
def exit():
    print("Thanks for playing!")
    userExit = input("Play again?(Y/N) ")
    if userExit == "Y":
        #player_hand = []
        main()
    elif userExit == "N":
        quit(0)
    else:
        print("'eerm... NO!' - scout tf2")
        quit(0)
#deck of cards (in points)
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 1, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

print("Welcome to blackjack!")
print("Shuffuling deck...")
rd.shuffle(deck) 
print("dealing cards...")
#house
print("The house's hand: ")
dealerCard = rd.choice(deck)
dealerCardOne = rd.choice(deck)
dealer_hand = [dealerCard, dealerCardOne]
print(f"[{dealerCard}, #]")
#player
print("Your hand: ")
playerCard = rd.choice(deck)
playerCardOne = rd.choice(deck)
player_hand = [playerCard, playerCardOne]
print(player_hand)

#house moves
def house():
    #house logic
    if sum(dealer_hand) > 15:
        print("Dealer stands!")
        print(f"{dealerCard}, #")
        main()
    elif sum(dealer_hand) < 15:
        print("Dealer Hits!")
        dealerCardThree = rd.choice(deck)
        print(f"{dealerCard}, {dealerCardThree}, #")
        main()

#main loop
def main():
    while True:
        userChoice = input("Hit, or Stand? ")
        if userChoice == "Hit" or userChoice == "hit":
            playerCardThree = rd.choice(deck)
            player_hand.append(playerCardThree)
            print(player_hand)
            print("dealers turn...")
        #elif userChoice == "Stand" or userChoice == "stand":
            #bust
            if sum(player_hand) > 21:
                print("Your bust!")
                print("The house wins!")
                print("calculating opposition score...")
                break
            elif sum(dealer_hand) > 21:
                print("House is bust!")
                print("You win!")
                print("calculating opposition score...")
                break
            #bust - tie
            if sum(player_hand) > 21 and sum(dealer_hand) > 21:
                print("All parties are bust!")
                print("Its a tie!")
                break
            else:
                print("Score calculated.")
            #blackjack
            if sum(player_hand) == 21:
                print("Blackjack!")
                print("You win!")
                print("calculating opposition score...")
                break
            elif sum(dealer_hand) == 21:
                print("Blackjack!")
                print("The house wins!")
                print("calculating opposition score...")
                break
            #blackjack - tie
            if sum(player_hand) == 21 and sum(dealer_hand) == 21:
                print("Blackjak!")
                print("All parties are blackjack!")
                print("Its a tie!")
                break
            else:
                print("Score calculated.")
        house()
        
main()
exit()




