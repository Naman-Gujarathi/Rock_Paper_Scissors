import random
def play():
    print("Lets play a game with computer rock paper scissor")
    print("Rules: \n 1. Rock Win over Scissor \n 2. Scissor Win over Paper \n 3. Paper win over Rock \n 4. If both comes same its draw and will be repeated")

    opponent = random.choice(["Rock", "Paper", "Scissor"])
    # print(f"opponent {opponent}")
    player = input("user enter input ")
    who_win(player, opponent)



def who_win(player, opponent):
    while(player == opponent):
        print("its a draw try again")
        player = input("user enter input ")
        opponent = random.choice(["Rock", "Paper", "Scissor"])

    if((player == "Scissor" and opponent == "Paper") or (player == "Stone" and opponent == "Scissor") or 
        (player == "Paper" and opponent == "Stone") ):
        print(f"player win !! player: {player} , opponent: {opponent}")
    else:
        print(f"opponent win !! player: {player} , opponent: {opponent}")


play()

