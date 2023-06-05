def intro():
    print('''
888    888       .d88b.   88888b.d88b.  8888b.  88888888  .d88b.  
888    888      d8P  Y8b  888 "888 "88b    "88b    d88P  d8P  Y8b 
888888 88888888 88888888  888  888  888 d888888   d88P   88888888 
888    888  888 Y8b.      888  888  888 88  888  d88P    Y8b.     
888888 888  888  "Y8888   888  888  888 Y888888 88888888  "Y8888  
    ''')

    print('''
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88888888888888888888888888888888888888888888888888888888888888888888888
    ''')

    print("Welcome to The maze.")
    print("Your mission is to find the exit.\n")
    print("You're at the cross road.")


def event1():
    print("\nYou turn left and keep walking until you end up in a bloody room. You see a door but there is a monster near it. It seems like the monster is blind but you're not sure about it. You can either 'sneak' past it or try your luck by 'run' to the door\n")


def event2():
    print("\nYou sneakily walk past the monster. The monster twitch every time you make a noise. But eventually, you reach the door. You gently open the door and get into the next room.\n")
    print(
        "You arrive at a room with three doors. One of them is 'green', the other one is 'blue', and the last one is 'red'.\n")


def final_event():
    print(
        "\nYou open the red door and enter the room. You found yourself in a room with a giant tv. The tv start and show a guy singing and dancing.\n")

    print(
        "Never gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\n")

    print("You stand there while the guy keeps dancing and singing. You finally realize that there is no exit. It's not possible to escape from this place. There is only you and that guy.\n")

    print(
        "Never gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n")


def gameover_event1():
    print("\nYou turn right and keep walking, then suddenly you feel the floor beneath you disappear. You have fallen into a hole filled with deadly spikes.\n")
    print("GAME OVER\n")


def gameover_event2():
    print(
        "\nFool! Even if the monster is blind it definitely can hear you from miles away. The monster tore open your chest and took its time eating you alive.\n")
    print("GAME OVER\n")


def gameover_event3():
    print(
        "\nYou open the green door and get into the room. You found yourself in a room filled with holes. And suddenly fire came out of them. You tried to open the door to go back, but the door won't budge. You're being burned alive. Your body is charred to the point not even your ex or imaginary girlfriend would recognize you.\n")
    print("GAME OVER\n")


def gameover_event4():
    print("\nYou open the blue door and enter the room. You are in a hallway. You keep walking and walking and suddenly remember that you are ugly, unemployed and useless. You are just a disappointment, and nobody wants you. Not even your imaginary girlfriend. So you just die.\n")
    print("GAME OVER\n")


def event_else_check_1():
    print(
        "\nYou slam youself to a wall. What the hell is wrong with you? there is no such option.\n")


def event_else_check_2():
    print(
        "\nYou slam youself to the wall even harder. Are you blind or maybe illiterate? Maybe you should go to doctor and get your eyes checked. oh... wait...\n")


def event_else_check_3():
    print("\nSigh... you can just die. I dont care anymore.\n")


def retry():
    return input("Retry? 'Y' or 'N'\n").upper()


def final_retry():
    return input("You finally reach the end. So? Want to try again? 'Y' or 'N'\n").upper()
