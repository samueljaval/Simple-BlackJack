'''
Has to be run with python3, will not function properly
with python2.
'''

import random
import sys


#SIMPLE HELPER FUNCTIONS ###################################
def deal_cards(cards, nb):
    deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    i = 0
    while i < nb:
        cards.append(deck[random.randint(0,12)])
        i += 1
    return cards

def sum(cards):
    sum = 0
    for x in cards:
        sum += x
    return sum

def make_bet(money):
    print("\n")
    bet = input("How much do you wanna bet? : ")
    while bet.isdigit() == False:
        bet = input("How much do you wanna bet? : ")
    print("\n")
    while int(bet) > money :
        print("you do not have enough money for that")
        bet = input("How much do you wanna bet? : ")
    else :
        money -= int(bet)
        return bet, money

def intro():
    print("\n\n\n\n")
    print("WELCOME TO SIMPLE BLACKJACK, A SIMPLIFIED VERSION OF BLACKJACK")
    print("IF YOU TRIPLE YOUR MONEY YOU WIN, YOU START WITH 1000$")
    print("has to be run with python3")
    print("\n\n\n\n")
###########################################################


#### the if1 and if1_start functions ask the user if they
#### want to use their ace as a 1 or an 11
def if1(cards,nb):
    if cards[-nb] == 1:
        change = input("do you want your ace to be 1 or 11? :  ")
        while change.isdigit() == False:
            print("please enter 1 or 11")
            change = input("do you want your ace to be 1 or 11? :  ")
        if int(change) == 11:
            cards[-nb] = 11
        elif int(change) == 1:
            cards[-nb] = 1
        else :
            print("please enter 1 or 11")
            change = input("do you want your ace to be 1 or 11? :  ")
    return cards

def if1_start(cards):
    cards = if1(cards,1)
    cards = if1(cards,2)
    return cards
###################################


###### less_21 with what happens when the user's sum is
###### less than 21. If the user stops before 21, the dealer plays
def less_21(money, cards, dealer, bet):

    print("\n")
    response = input('do you wanna a card? if yes type 1, type 2 if you wanna stop :   ')

    while response.isdigit() == False:
        print("please enter 1 or 2")
        response = input('do you wanna a card? if yes type 1, type 2 if you wanna stop :   ')

    if int(response) == 1:                           #player wants another card
        cards = deal_cards(cards, 1)
        delt = cards[-1]
        print("your cards are now  ")
        print(cards)
        cards = if1(cards,1)
        print("and your total sum is")
        print(sum(cards))

    elif int(response) == 2:                        #player does not want another card, dealer plays

        print("let's see what the dealer gets")
        while sum(dealer) < 17 :
            dealer = deal_cards(dealer, 1)
            print("the dealer now has")
            print(dealer)
            print("their sum is " + str(sum(dealer)))

        if sum(dealer) > sum(cards) and sum(dealer) <= 21:
            print("Sorry, the dealer beat you, you lose your bet")
            print("\n\n\n\n\n\n")
            if money == 0:
                print("you are out of money")
                sys.exit(0)
            else :
                bj(money)

        elif sum(dealer) < sum(cards) or sum(dealer) > 21:
            print("congrats, you beat the dealer, you win your bet")
            money += 2*int(bet)
            print("\n\n\n\n\n\n")
            if money >= 3000:
                print("congrats you win")
                sys.exit(0)
            else :
                bj(money)

        else :
            print("It's a tie, you get your bet back")
            money += int(bet)
            bj(money)

    else :                                         #wrong user input, ask again
        print("please enter 1 or 2")
        response = input('do you wanna a card? if yes type 1, type 2 if you wanna stop :   ')

    return dealer
#########################################


###### This is the main function of the program. It is called recursively
###### when the player still has money and wants to play again
def bj(money):

    print("You have " + str(money) + " dollars")
    quit = input("do you wanna bet or quit, type 1 to bet, 2 to quit : ")

    while quit.isdigit() == False:
        print("please enter 1 or 2")
        quit = input("do you wanna bet or quit, type 1 to bet, 2 to quit : ")

    if int(quit) == 2:
        print("quitting...")
        sys.exit(0)

    elif int(quit) == 1:

        bet, money = make_bet(money)
        cards = []
        dealer = []
        dealer = deal_cards(dealer, 1)
        print("the dealer got : ")
        print(dealer)

        cards = deal_cards(cards,2)

        print("your cards are : ")
        print(cards)
        cards = if1_start(cards)
        print("and your total sum is")
        print(sum(cards))

        while sum(cards) <= 20:
            dealer = less_21(money,cards,dealer,bet)

        if sum(cards) == 21 and sum(dealer) != 21:
            print("BLACKJACK!!!!")
            money += 2*int(bet)

            if money >= 3000:
                print("congrats you win")
                sys.exit(0)

            print("\n\n\n\n\n\n")
            bj(money)

        if sum(cards) == 21 and sum(dealer) == 21:
            print("It's a tie, you get your bet back")
            money += int(bet)
            bj(money)

        if sum(cards) > 21:
            print("Sorry, you are over 21, you lost your bet")
            print("\n\n\n\n\n\n")
            if money == 0:
                print("you are out of money")
                sys.exit(0)
            else :
                bj(money)

    else :
        print("please enter 1 or 2")
        bj(money)


##### running the main function with 1000$ and showing a little text as intro
intro()
bj(1000)
