import random

GREEN = "\033[32m"
CYAN = "\033[36m"
RESET = "\033[0m"

classes = [
    "warrior",
    "healer",
    "thief",
]

player_one = input(f"{GREEN}PLAYER 1: Type your name and press ENTER\n>{RESET} ").title()

print(f"{CYAN}AVAILABLE CLASSES:{GREEN}\nWarrior:{RESET} You have a shiled. Once per game, you can block your opponent's attack\n{GREEN}Healer:{RESET} You have magical healing abilities. Once per game, you can heal yourself for 1d4 HP\n{GREEN}Thief:{RESET} You are a master at pickpocketing. Once per game, you can steal 1d4 of your opponent's roll")

while True:
    player_one_class = input(f"{GREEN}PLAYER 1: Pick a class\n>{RESET} ").lower()

    if player_one_class not in classes:
        print("Please pick an available class.")
    
    else:
        break

player_two = input(f"{GREEN}PLAYER 2: Type your name and press ENTER\n>{RESET} ").title()

print(f"{CYAN}AVAILABLE CLASSES:{GREEN}\nWarrior:{RESET} You have a shiled. Once per game, you can block your opponent's attack\n{GREEN}Healer:{RESET} You have magical healing abilities. Once per game, you can heal yourself for 1d4 HP\n{GREEN}Thief:{RESET} You are a master at pickpocketing. Once per game, you can steal 1d4 of your opponent's roll")

while True:
    player_two_class = input(f"{GREEN}PLAYER 2: Pick a class\n>{RESET} ").lower()

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

    while playing:
        round += 1

        print(f"{CYAN}ROUND {round}")

        if player_one_class == "warrior":
            player_one_roll = random.randint(1, 20) + random.randint(1, 4)
        
        else:
            player_one_roll = random.randint(1, 20)
        
        if player_two_class == "warrior":
            player_two_roll = random.randint(1, 20) + random.randint(1, 4)
        
        else:
            player_two_roll = random.randint(1, 20)

        print(f"{GREEN}PLAYER 1:{RESET} {player_one_roll}\n{GREEN}PLAYER 2:{RESET} {player_two_roll}")

        if player_one_class == "thief" and stolen_roll_one == False:
            steal_answer = input(f"{GREEN}PLAYER 1:{RESET} You are a thief. Do you want to steal 1d4 from {player_two}'s roll?\nType yes or no: ").lower()

            while True:
                if steal_answer == "yes":
                    player_two_roll -= random.randint(1, 4)
                    stolen_roll_one = True

                    print(f"{GREEN}PLAYER 2: Your new roll is {player_two_roll}")
                    break
                
                elif steal_answer == "no":
                    print(f"{player_one} choses to not steal from {player_two} this round.")
                    break
                
                else:
                    print(f"{GREEN}PLAYER 1:{RESET} Please answer yes or no")
        
        if player_two_class == "thief" and stolen_roll_two == False:
            steal_answer = input(f"{GREEN}PLAYER 2:{RESET} You are a thief. Do you want to steal 1d4 from {player_two}'s roll?\nType yes or no: ").lower()

            while True:
                if steal_answer == "yes":
                    player_one_roll -= random.randint(1, 4)
                    stolen_roll_two = True

                    print(f"{GREEN}PLAYER 1: Your new roll is {player_one_roll}")
                    break
                
                elif steal_answer == "no":
                    print(f"{player_two} choses to not steal from {player_one} this round.")
                    break
                
                else:
                    print(f"{GREEN}PLAYER 2:{RESET} Please answer yes or no")
        
        if player_one_roll > player_two_roll:
            player_two_hp -= player_one_roll - player_two_roll

            print(f"{GREEN}PLAYER 1 HEALTH:{RESET} {player_one_hp}\n{GREEN}PLAYER 2 HEALTH:{RESET} {player_two_hp}")

        elif player_one_roll < player_two_roll:
            player_one_hp -= player_two_roll - player_one_roll

            print(f"{GREEN}PLAYER 1 HEALTH:{RESET} {player_one_hp}\n{GREEN}PLAYER 2 HEALTH:{RESET} {player_two_hp}")

        elif player_one_roll == player_two_roll:
            print("Your rolls were equal! No one loses HP...")
        
        if player_one_class == "healer" and healed_one == False:
            heal_answer = input(f"{GREEN}PLAYER 1: You are a healer, do you want to heal 1d4 of damage? (capped at 10 HP)\n>{RESET} ")

            while True:
                if heal_answer == "yes":
                    player_one_hp += random.randint(1, 4)
                    healed_one = True

                    print(f"{GREEN}PLAYER 1 HEALTH:{RESET} {player_one_hp}\n{GREEN}PLAYER 2 HEALTH:{RESET} {player_two_hp}")
                    break
                
                elif heal_answer == "no":
                    print(f"{player_one} chooses to not heal this round")
                
                else:
                    print(f"{GREEN}PLAYER 1: Please answer yes or no.")
        
        if player_two_class == "healer" and healed_two == False:
            heal_answer = input(f"{GREEN}PLAYER 2: You are a healer, do you want to heal 1d4 of damage? (capped at 10 HP)\n>{RESET} ")

            while True:
                if heal_answer == "yes":
                    player_two_hp += random.randint(1, 4)
                    healed_two = True

                    print(f"{GREEN}PLAYER 1 HEALTH:{RESET} {player_one_hp}\n{GREEN}PLAYER 2 HEALTH:{RESET} {player_two_hp}")
                    break
                
                elif heal_answer == "no":
                    print(f"{player_two} chooses to not heal this round")
                    break
                
                else:
                    print(f"{GREEN}PLAYER 2: Please answer yes or no.")

        if player_one_hp <= 0:
            print(f"{CYAN}{player_two.upper()} WON!")
            playing = False
        
        elif player_two_hp <= 0:
            print(f"{CYAN}{player_one.upper()} WON!")
            playing = False

main()