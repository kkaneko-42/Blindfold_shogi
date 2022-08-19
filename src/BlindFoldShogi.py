import sys
import subprocess

def game_start():


def main():

    #print_usage()
    game_start()
    turn = get_turn()
    while True:
        movement = input()
        if (validate_input(movement)):
            pass
            #print_usage()
        else:
            move(movement)
        print_
        

if __name__ == "__main__":
    main()
