import random

com_point = 0
player_point = 0

players_optionts = ['snake', 'water', 'gun']
print(players_optionts)

computer_choose = random.choice(players_optionts)

i = 1
while i < 6:
    player_choose = input("Enter any one : ")
    print("player_choose", player_choose)

    if (computer_choose == "snake" and player_choose == "water"):
        com_point += 1
        print("com_point : ",com_point, "\nplayer_point : ", player_point)
    elif (computer_choose == "water" and player_choose == "snake"):
        player_point += 1
        print("com_point : ",com_point, "\nplayer_point : ", player_point)
    elif (computer_choose == "water" and player_choose == "gun"):
        com_point += 1
        print("com_point : ",com_point, "\nplayer_point : ", player_point)
    elif (computer_choose == "gun" and player_choose == "water"):
        player_point += 1
        print("com_point : ",com_point, "\nplayer_point : ", player_point)
    elif (computer_choose == "snake" and player_choose == "gun"):
        player_point += 1
        print("com_point : ",com_point, "\nplayer_point : ", player_point)
    elif (computer_choose == "gun" and player_choose == "snake"):
        com_point += 1
        print("com_point : ",com_point, "\nplayer_point : ", player_point)
    else:
        print("com_point : ",com_point, "\nplayer_point : ", player_point)
        print("**Both player are same choose so point = 0")
    i += 1

