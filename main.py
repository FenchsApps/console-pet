import os
import pyfiglet
from rich import print
import time
import sys
import threading

# Global variables
title = pyfiglet.figlet_format('Console Pet', font="slant")
HAPPY = 60
HUNGER = 100
is_alive = True
NAME = "Nimbus"

# Function to decrease hunger over time
def decrease_hunger():
    global HUNGER, is_alive
    while is_alive:
        time.sleep(5)  # Wait for 5 seconds
        HUNGER = max(HUNGER - 4, 0)  # Decrease hunger by 4
        if HUNGER <= 0:
            print("[red]Your pet has starved to death...[/red]")
            is_alive = False
            sys.exit()

# Start the hunger thread
hunger_thread = threading.Thread(target=decrease_hunger)
hunger_thread.daemon = True  # Daemonize thread to exit when the main program exits
hunger_thread.start()

# Functions
def feed():
    global HUNGER, HAPPY
    HUNGER = min(HUNGER + 20, 100)  # Prevent hunger from exceeding 100
    HAPPY = min(HAPPY + 10, 100)    # Increase happiness
    print("Yummy!")
    time.sleep(1)
    main()

def woof():
    global HAPPY
    HAPPY = min(HAPPY + 5, 100)
    print("Woof! Woof!")
    time.sleep(1)
    main()

def exit_pet():
    print("Goodbye!")
    sys.exit()

def guide():
    print("Hi! I'm Nimbus. Thanks for getting me out from this freaki'n digital zoo. Take care of me like your dog from house.")
    print("Feed me, pet me, clean up after me, and walk me. that's obvious..")
    print("[red] But do it well, or I'll explode into bits and die q_q [/red]")
    input("Press Enter to continue...")
    main()

def github():
    print("Gawk! Gawk! oh.. there's my github!")
    print("https://github.com/FenchsApps/")
    input()
    time.sleep(1)
    main()

def play():
    global HAPPY, HUNGER
    HAPPY = min(HAPPY + 15, 100)
    HUNGER = max(HUNGER - 10, 0)
    print(f"{NAME} is having fun playing with you!")
    time.sleep(1)
    main()

def hurt():
    global HAPPY
    HAPPY = max(HAPPY - 20, 0)
    print(f"Why would you hurt {NAME}? :(")
    time.sleep(1)
    main()

def stats():
    print(f"{NAME}'s Stats:")
    print(f"Hunger: {HUNGER}")
    print(f"Happiness: {HAPPY}")
    input("Press Enter to continue...")
    main()

def settings():
    global NAME
    print(f"Current pet name: {NAME}")
    new_name = input("Enter a new name for your pet (or press Enter to keep the current name): ").strip()
    if new_name:
        NAME = new_name
        print(f"Pet name updated to {NAME}!")
    else:
        print("Pet name remains unchanged.")
    time.sleep(1)
    main()

def update_status():
    global HAPPY, is_alive
    if HAPPY <= 0:
        print("[red]Your pet has run away...[/red]")
        is_alive = False
        sys.exit()

def main():
    global is_alive
    if not is_alive:
        print("[red]Your pet is no longer with us...[/red]")
        sys.exit()

    os.system("clear")
    print(f"[red]{title}[/red]")
    print(f"Pet's hunger: {HUNGER}")
    print(f"Happiness: {HAPPY}")                                   
    print("                                       Command List: 1. pet --feed")
    print("                                                     2. pet --woof")
    print(f"[purple]  / \__[/purple]                                              3. pet --exit")
    print(f"[purple] (    @\___[/purple]                                          4. pet --guide")
    print(f"[purple] /         O[/purple]                                         5. pet --github")
    print(f"[purple]/   (_____/[/purple]                                          6. pet --play")
    print(f"[purple]/_____/   U[/purple]                                          7. pet --hurt (not recommended .. really)")
    print("                                                     8. pet --stats")
    print("                                                     9. pet --settings")

    request = input("Enter Command: ").strip()

    commands = {
        "pet --feed": feed,
        "pet --woof": woof,
        "pet --exit": exit_pet,
        "pet --guide": guide,
        "pet --github": github,
        "pet --play": play,
        "pet --hurt": hurt,
        "pet --stats": stats,
        "pet --settings": settings,
    }

    if request in commands:
        commands[request]()
    else:
        print("[red]Incorrect Command![/red]")
        time.sleep(1)
        main()

    update_status()

if __name__ == "__main__":
    main()
