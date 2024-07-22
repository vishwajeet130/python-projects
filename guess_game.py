import random

def instruction():
    print("Welcome,\nIn this game you will guess a 4 digit number.")
    print("If the number matches with the lucky number then good for you.")
    print("=================================================================")
    
def guess_game():
    player_name = input("Enter your name: ")
    lucky_number = random.randint(1000,9999)
    start_game = True
    while start_game:
        while True:
            try:
                player_number = int(input("Input 4 digit number: "))
                print("==========================================")
                break
            except:
                print("You need to enter something. Cannot leave it blank.")
                print("==========================================")
    
        if(len(str(player_number))==4):
            while True:
                if(player_number == lucky_number):
                    print(f"Wohoo!!\n{player_name},You Won!!!")
                    print("==========================================")
                    start_game = False
                    break
                elif(player_number<lucky_number):
                    print("You need to guess a bit higher!!")
                    print("==========================================")
                    break
                elif(player_number>lucky_number):
                    print("You need to guess a bit lower!!")
                    print("==========================================")
                    break

        else:
            while len(str(player_number))!=4:
                print("Number needs to be 4 digit. Try again!!")
                print(lucky_number)
                break
                # player_number = int(input("Input 4 digit number: "))
                
            
            
instruction()
guess_game()
