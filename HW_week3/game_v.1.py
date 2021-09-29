import random
import sys
player = {
    "score": 0,
}



def printGraphic(name):
    if (name == "title"): 
        print("_ .-') _     ('-.     ('-.     _ (`-.        _ .-') _     ('-.     ('-.     _ (`-.                                  ('-.   ('-.         .-')")  
        print("( (  OO) )  _(  OO)  _(  OO)   ( (OO  )      ( (  OO) )  _(  OO)  _(  OO)   ( (OO  )                               _(  OO) ( OO ).-.    ( OO ) )") 
        print(" \     .'_ (,------.(,------. _.`     \       \     .'_ (,------.(,------. _.`     \       .-'),-----.    .-----. (,------./ . --. /,--./ ,--,'")  
        print(" ,`'--..._) |  .---' |  .---'(__...--''       ,`'--..._) |  .---' |  .---'(__...--''      ( OO'  .-.  '  '  .--./  |  .---'| \-.  \ |   \ |  |\ ") 
        print(" |  |  \  ' |  |     |  |     |  /  | |       |  |  \  ' |  |     |  |     |  /  | |      /   |  | |  |  |  |('-.  |  |  .-'-'  |  ||    \|  | )") 
        print(" |  |   ' |(|  '--. (|  '--.  |  |_.' |       |  |   ' |(|  '--. (|  '--.  |  |_.' |      \_) |  |\|  | /_) |OO  )(|  '--.\| |_.'  ||  .     |/ ")  
        print(" |  |   / : |  .--'  |  .--'  |  .___.'       |  |   / : |  .--'  |  .--'  |  .___.'        \ |  | |  | ||  |`-'|  |  .--' |  .-.  ||  |\    |  ")  
        print(" |  '--'  / |  `---. |  `---. |  |            |  '--'  / |  `---. |  `---. |  |              `'  '-'  '(_'  '--'\  |  `---.|  | |  ||  | \   |  ") 
        print(" `-------'  `------' `------' `--'            `-------'  `------' `------' `--'                `-----'    `-----'  `------'`--' `--'`--'  `--'  ")  
    
    if (name == "shark"):
        print("                                ,-                           ")
        print("                               ,'::|                         ")
        print("                              /::::|                         ")
        print("                            ,'::::o\                                      _.. ")
        print("         ____........-------,..::?88b                                  ,-' /  ")
        print(" _.---"""                          "_`-._                           ,-' .;'   ")
        print("<. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'     ")
        print(" `-._  ` ``:`:`:`::||||:::::::::::::::::.:. .  ----._ ,'|     ,-'.  .;'       ")
        print("     ""_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'          ")  
        print("         ""--.__     P(       \               ` ``:`:``:::: .   .;'           ")
        print("                \--.:-.     `.                             .:/                ")
        print("                  \. /    `-._   `.""-----.,-..::(--"".\"`.  `:\              ")
        print("                   `P         `-._ \          `-:\          `. `:\            ") 
        print("                                   ""            ""           `-._)           ")

    if (name == "skull"):
        print("                   ______                  ")
        print("                .-"      "-.               ")
        print("               /            \              ") 
        print("   _          |              |          _  ")
        print("  ( \         |,  .-.  .-.  ,|         / ) ")
        print("   > '=._     | )(__/  \__)( |     _."" <  ")
        print("  (_/'=._'=._ |/     /\     \| _.="   "\_) ")
        print("         '=._ (_     ^^     _);_'          ") 
        print("             '=\__|IIIIII|__/='            ")
        print("            _.='| \IIIIII/ |'=._           ")
        print("  _     _.='_.='\          /'=._'=._     _ ")
        print(" ( \_.='_.='     `--------`     '=._'=._/ )")
        print("  > _.="                            "=._ < ")
        print(" (_/                                    \_)")
    
    if (name == "hut"):
        print("                         _..-:-.._ ")
        print("                  _..--''    :    ``--.._ ")
        print("       _..--''           :           ``--.._ ")
        print(" _..-''                  :                .'``--.._")
        print("  _..--'' `.                     :              .'         |")
        print("|          `.              _.-''|``-._       .'           |")
        print("|            `.       _.-''     |     ``-._.'       _.-.  |")
        print(" |   |`-._      `._.-''          |  ;._     |    _.-'   |  |")
        print(" |   |    `-._    |     _.-|     |  |  `-.  |   |    _.-'  | ")
        print(" |_   `-._    |   |    |   |     |  `-._ |  |   |_.-'   _.-'   ..")
        print("   `-._   `-._|   |    |.  |  _.-'-._   `'  |       _.-'   ..::::::..")
        print("       `-._       |    |  _|-'  *    `-._   |   _.-'   ..::::::::''")
        print("           `-._   |   _|-'.::. \|/  *    `-.|.-'   ..::::::::''")
        print("               `-.|.-' *`:::::::.. \|/  *      ..::::::::''")
        print("                      \|/  *`:::::::.. \|/ ..::::::::''")

    if(name == "whale"):
        print("           __________...----..____..-'``-..___ ")
        print("    ,'.                                  ```--.._ ")
        print("   :                                             ``._ ")
        print("   |                           --                    ``. ")
        print("   |                   -.-      -.     -   -.        `. ")
        print("   :                     __           --            .     \ ")
        print("    `._____________     (  `.   -.-      --  -   .   `     \ ")
        print("       `-----------------\   \_.--------..__..--.._ `. `.   : ")
        print("                          `--'     SSt             `-._ .   | ")
        print("                                                       `.`  | ")
        print("                                                         \` | ")
        print("                                                          \ | ")
        print("                                                          / \`. ")
        print("                                                         /  _\-' ")
        print("                                                        /_,' ")

    if(name == "Nimo"):
        print("           __  ")
        print("          /  ;  ")
        print("      _.--'''-..   _. ")
        print("    /F         `-'  [ ")
        print("   ]  ,    ,    ,    ;")
        print("    '--L__J_.-"" ',_; ")
        print("         '-._J ")

        

# Introduce our story to users
def introStory():
    printGraphic("title")
    print("Welcome to Deep Deep Ocean, what should I call you? ")  
    userName = input("Please enter your name >")

    print("Nice to meet you, " + userName)
    input ("Press enter > ")

    print("You enter the Deep Deep Ocean gate.")
    print("There’s a sea animal in front of you. What is it?")
    
def oceanGate():
    print("option: [ shark, Nimo ]")
    pcmd = input(">")

    if (pcmd == "shark"):
        print("Shark ate you up. The game is over.")
        gameOver()

    else:
        printGraphic("Nimo")
        print("Hello, I’m Nimo. Please follow me!")
        print("You got point 50.")
        player["score"] += 50 
        print ("Your total score is " + str(player["score"]))
    
        input ("Press enter > ")

def foodStorage():
    printGraphic("hut")
    print ("Here is the food storage in our ocean. You must be very hungry. Which one do you want to eat?")
    print ("option: [ squid, shrimp, clam ]")
    pcmd = input(">")
    if (pcmd == "shrimp"):
        print ("Great choice! We have lots of fresh shrimps. Help yourself!" )
        print("You got point 100.")
        player["score"] += 100 
        print ("Your total score is " + str(player["score"]))

        input ("Press enter > ")
    
    elif (pcmd == "clam"):
        print ("Great choice! We have lots of fresh clams. Help yourself!" )
        print("You got point 200.")
        player["score"] += 200 
        print ("Your total score is " + str(player["score"]))
        input ("Press enter > ")

    
    else :    
        print("Squid shot ink to you. The game is over.")
        gameOver()

def meetWhale():
    printGraphic("whale")
    print("You must be full now. Oh, you've just met a Whale. ")
    print ("Hi, I'm a whale. Good to see you! I'm so bored now. How about playing dice? If you get 4 or higher, you win!")
    input ("Press enter > ")
    dice = random.randint(1,6)
    print ("You roll a: " + str(dice) + " out of 6 ")
    
    if (dice >= 4):
        print ("Shoot, you win... You got point 300.")
        player["score"] += 300 
        print ("Your total score is " + str(player["score"]))

    else :
        print ("Hahaha, I win! You lost! ")
        gameOver()

def gameOver():
    printGraphic("skull")
    print ("GAME OVER")
    print ("Your score is " + str(player["score"]) )
 

# Start here 
introStory()
oceanGate()
foodStorage()
meetWhale()