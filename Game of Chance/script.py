#! /usr/bin/env python3
# coding: utf-8

import random

cards = {
    0: 'Joker',
    1: '2',
    2: '3',
    3: '4',
    4: '5',
    5: '6',
    6: '7',
    7: '8',
    8: '9',
    9: '10',
    10: 'Jack',
    11: 'Queen',
    12: 'King',
    13: 'Ace'
}


def head_or_tails(money):
    bet = get_bet(money)
    guess = guess = get_guess("Heads", "Tails")
    money += flip_coin(bet, guess) - bet
    print(f"You have now {money} dollars.")
    get_results(money)


def flip_coin(bet, guess):
    flip_result = random.choice("HEADS", "TAILS")
    print(f"The result is {flip_result}!")
    win = flip_result == guess
    print("You won!" if win else "You lost!")
    return bet * 2 if win else 0


def cho_han(money):
    bet = get_bet(money)
    guess = get_guess("Odd", "Even")
    money += roll_dices(bet, guess) - bet
    get_results(money)


def roll_dices(bet, guess):
    first_dice, second_dice = random.randint(0, 6), random.randint(0, 6)
    total = first_dice + second_dice
    print(f"The dices rolled {first_dice} and {second_dice}, for a total of {total}!")
    result = "EVEN" if not total % 2 else "ODD"
    win = result == guess
    print("You won!" if win else "You lost!")
    return bet * 2 if win else 0


def highest_card(money):
    bet = get_bet(money)
    player_pick = random.randint(0, 13)
    print(f"You picked the card {cards.get(player_pick)}")
    computer_pick = random.randint(0, 13)
    print(f"Your opponent picked the card {cards.get(computer_pick)}")
    win = player_pick > computer_pick
    tie = player_pick == computer_pick
    print("You won!" if win else "It's a tie" if tie else "You lost!")
    money = money + bet if win else money if tie else money - bet
    get_results(money)


def roulette(money):
    bet = get_bet(money)
    guess = get_guess("Even", "Odd", True)
    money += spin_roulette(bet, guess) - bet
    get_results(money)


def spin_roulette(bet, guess):
    result = random.randint(0, 36)
    print(f"The roulette stopped on {result}!")
    if guess in ["EVEN", "ODD"]:
        even_or_odd = "EVEN" if not result % 2 else "ODD"
        win = even_or_odd == guess and spin_roulette != 0
        print("You won!" if win else "You lost!")
        return bet * 2 if win else 0
    win = result == bet
    print("You won!" if win else "You lost!")
    return bet * 36 if win else 0


def get_bet(money):
    print(f"How much do you want to bet? You have {money} dollars left.")
    bet = False
    while not bet:
        try:
            bet = int(input("Enter the selected amount: "))
            if money - bet < 0 or bet > money:
                raise Exception
        except:
            print("The amount is invalid.")
            bet = False
    return bet


def get_guess(choice_one, choice_two, game_is_roulette=False):
    print(f"{choice_one} or {choice_two}?")
    if game_is_roulette:
        print("You can also choose any number between 0 and 36!")
    guess = False
    while guess not in [choice_one[0], choice_two[0]]:
        if game_is_roulette:
            print("Choose your number or...")
        guess = input(f"Type {choice_one[0]} for {choice_one}, {choice_two[0]} for {choice_two}: ").upper()
        if game_is_roulette and guess not in [choice_one[0], choice_two[0]]:
            try:
                guess = int(guess)
                if 36 >= guess >= 0:
                    return guess
                else:
                    raise Exception
            except:
                guess = False
    return choice_one.upper() if guess == choice_one[0] else choice_two.upper()


def get_results(money):
    print(f"You have now {money} dollars.")
    if money == 0:
        exit()
    play_game(money)


def play_game(money=1000):
    selection = False
    print("Choose a game: ")
    print("1 - Heads or Tails")
    print("2 - Cho-Han")
    print("3 - Highest Card")
    print("4 - Roulette")
    while not selection:
        try:
            selection = int(input("Enter the corresponding number: "))
            if selection not in [1, 2, 3, 4]:
                raise Exception
        except:
            print("You didn't choose a valid option.")
            selection = False
    if selection == 1:
        head_or_tails(money)
    if selection == 2:
        cho_han(money)
    if selection == 3:
        highest_card(money)
    if selection == 4:
        roulette(money)


def main():
    play_game()


if __name__ == "__main__":
    main()
