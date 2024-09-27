import random, time, sys

GREEN = "\033[32m"
CYAN = "\033[36m"
RESET = "\033[0m"

classes = [
    "warrior",
    "healer",
    "thief",
]

player_one = input(f"{GREEN}PLAYER 1:{RESET} Type your name and press ENTER\n> ").title()

print(f"{CYAN}AVAILABLE CLASSES:{GREEN}\nWarrior:{RESET} You have a shield. Once per game, you can block 1d4 of damage from your opponent\n{GREEN}Healer:{RESET} You have magical healing abilities. Once per game, you can heal yourself for 1d4 HP\n{GREEN}Thief:{RESET} You are a master at pickpocketing. Once per game, you can steal 1d4 of your opponent's roll")

while True:
    player_one_class = input(f"{GREEN}{player_one.upper()}:{RESET} Pick a class\n> ").lower()

    if player_one_class not in classes:
        print("Please pick an available class.")
    
    else:
        break

while True:
    player_two = input(f"{GREEN}PLAYER 2:{RESET} Type your name and press ENTER\n> ").title()

    if player_two == player_one:
        print("Your name cannot be the same as Player 1.")
    
    else:
        break

print(f"{CYAN}AVAILABLE CLASSES:{GREEN}\nWarrior:{RESET} You have a shield. Once per game, you can block 1d4 of damage from your opponent\n{GREEN}Healer:{RESET} You have magical healing abilities. Once per game, you can heal yourself for 1d4 HP\n{GREEN}Thief:{RESET} You are a master at pickpocketing. Once per game, you can steal 1d4 of your opponent's roll")

while True:
    player_two_class = input(f"{GREEN}{player_two.upper()}:{RESET} Pick a class\n> ").lower()

    if player_two_class not in classes:
        print("Please pick an available class.")
    
    else:
        break
    
def main():
    player_one_hp = 20
    player_two_hp = 20
    playing = True
    round = 0
    stolen_roll_one = False
    stolen_roll_two = False
    healed_one = False
    healed_two = False
    blocked_one = False
    blocked_two = False

    while playing:
        round += 1
        player_one_roll = random.randint(1, 20)
        player_two_roll = random.randint(1, 20)

        print(f"{CYAN}ROUND {round}")

        print(f"{GREEN}{player_one.upper()}:{RESET} {player_one_roll}\n{GREEN}{player_two.upper()}:{RESET} {player_two_roll}")

        if player_one_class == "thief" and stolen_roll_one == False:

            while True:
                steal_answer = input(f"{GREEN}{player_one.upper()}:{RESET} You are a thief. Do you want to steal 1d4 from {player_two}'s roll?\nType yes or no: ").lower()

                if steal_answer == "yes":
                    stolen_roll = random.randint(1, 4)
                    player_one_roll += stolen_roll
                    player_two_roll -= stolen_roll
                    stolen_roll_one = True

                    print(f"{GREEN}{player_two.upper()}:{RESET} {player_one} stole {stolen_roll} from you. Your new roll is {player_two_roll}")
                    break
                
                elif steal_answer == "no":
                    print(f"{player_one} choses to not steal from {player_two} this round.")
                    break
                
                else:
                    print(f"{GREEN}{player_one.upper()}:{RESET} Please answer yes or no")
        
        if player_two_class == "thief" and stolen_roll_two == False:

            while True:
                steal_answer = input(f"{GREEN}{player_two.upper()}:{RESET} You are a thief. Do you want to steal 1d4 from {player_two}'s roll?\nType yes or no: ").lower()

                if steal_answer == "yes":
                    stolen_roll = random.randint(1, 4)
                    player_two_roll += stolen_roll
                    player_one_roll -= stolen_roll
                    stolen_roll_two = True

                    print(f"{GREEN}{player_one.upper()}: {player_two} stole {stolen_roll} from you. Your new roll is {player_one_roll}")
                    break
                
                elif steal_answer == "no":
                    print(f"{player_two} choses to not steal from {player_one} this round.")
                    break
                
                else:
                    print(f"{GREEN}{player_two.upper()}:{RESET} Please answer yes or no")
        
        if player_one_class == "warrior" and player_one_roll < player_two_roll and blocked_one == False:

            while True:
                block_question = input(f"{GREEN}{player_one.upper()}:{RESET} You are a warrior. Do you want to block 1d4 of damage from {player_two}?\nType yes or no: ").lower()

                if block_question == "yes":
                    player_two_roll -= random.randint(1, 4)
                    blocked_one = True
                    
                    print(f"{GREEN}{player_two.upper()}:{RESET} Your new roll is {player_two_roll}")
                    break
                
                elif block_question == "no":
                    print(f"{player_one} chooses to not block {player_two}'s damage.")
                    break
                
                else:
                    print(f"{GREEN}{player_one.upper()}:{RESET} Please answer yes or no")
        
        if player_two_class == "warrior" and player_one_roll > player_two_roll and blocked_two == False:

            while True:
                block_question = input(f"{GREEN}{player_two.upper()}:{RESET} You are a warrior. Do you want to block 1d4 of damage from {player_one}?\nType yes or no: ").lower()

                if block_question == "yes":
                    player_one_roll -= random.randint(1, 4)
                    blocked_two = True
                    
                    print(f"{GREEN}{player_one.upper()}:{RESET} Your new roll is {player_one_roll}")
                    break
                
                elif block_question == "no":
                    print(f"{player_two} chooses to not block {player_one}'s damage.")
                    break
                
                else:
                    print(f"{GREEN}{player_two.upper()}:{RESET} Please answer yes or no")
        
        if player_one_roll > player_two_roll:
            player_two_hp -= player_one_roll - player_two_roll

            print(f"{GREEN}{player_one.upper()}'s HEALTH:{RESET} {player_one_hp}\n{GREEN}{player_two.upper()}'s HEALTH:{RESET} {player_two_hp}")

        elif player_one_roll < player_two_roll:
            player_one_hp -= player_two_roll - player_one_roll

            print(f"{GREEN}{player_one.upper()}'s HEALTH:{RESET} {player_one_hp}\n{GREEN}{player_two.upper()}'s HEALTH:{RESET} {player_two_hp}")

        elif player_one_roll == player_two_roll:
            print("Your rolls were equal! No one loses HP...")
        
        if player_one_class == "healer" and healed_one == False:

            while True:
                heal_answer = input(f"{GREEN}{player_one.upper()}:{RESET} You are a healer, do you want to heal 1d4 of damage?\nType yes or no: {RESET} ")

                if heal_answer == "yes":
                    player_one_hp += random.randint(1, 4)
                    healed_one = True

                    print(f"{GREEN}{player_one.upper()}'s HEALTH:{RESET} {player_one_hp}\n{GREEN}{player_two.upper()}'s HEALTH:{RESET} {player_two_hp}")
                    break
                
                elif heal_answer == "no":
                    print(f"{player_one} chooses to not heal this round")
                    break
                
                else:
                    print(f"{GREEN}{player_one.upper()}:{RESET} Please answer yes or no.")
        
        if player_two_class == "healer" and healed_two == False:

            while True:
                heal_answer = input(f"{GREEN}{player_two.upper()}:{RESET} You are a healer, do you want to heal 1d4 of damage?\nType yes or no: ")

                if heal_answer == "yes":
                    player_two_hp += random.randint(1, 4)
                    healed_two = True

                    print(f"{GREEN}{player_one.upper()}'s HEALTH:{RESET} {player_one_hp}\n{GREEN}{player_two.upper()}'s HEALTH:{RESET} {player_two_hp}")
                    break
                
                elif heal_answer == "no":
                    print(f"{player_two} chooses to not heal this round")
                    break
                
                else:
                    print(f"{GREEN}{player_two.upper()}:{RESET} Please answer yes or no.")
        
        input(f"{CYAN}Press ENTER to continue")

        if player_one_hp <= 0:
            print(f"{CYAN}{player_two.upper()} WON!")
            playing = False
        
        elif player_two_hp <= 0:
            print(f"{CYAN}{player_one.upper()} WON!")
            playing = False
    
    end_of_game()

def end_of_game():
    play_again = input(f"{CYAN}Do you want to play again?\nType yes or no:{RESET} ").lower()

    if play_again == "yes":
        print(f"{CYAN}Restarting...")
        
        time.sleep(3)
        main()
    
    elif play_again == "no":
        print(f"{CYAN}Quitting...")

        time.sleep(3)
        sys.exit()

main()