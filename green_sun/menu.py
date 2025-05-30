# main menu

# import sys stuff for reading cmd lines
import subprocess
import sys

running = 1

print("Welcome to Green Sun!")
print("If you want to play, enter \'level\'.")
print("If you need help, enter \'help\'.")
print("If you want to quit, enter \'quit\'.")

while running != 0:
    try:
        user_input = input("What do you want to do? ").strip()
        if user_input == "level":
            level = input("What level do you want to play? Enter a number between 1 and 5.\n ")
            level_file_name = "level" + level + ".py"
            subprocess.Popen(["python3", level_file_name])
        elif user_input == "help":
            print("If you want to play, enter \'level\'.")
            print("If you need help, enter \'help\'.")
            print("If you want to quit, enter \'quit\'.")
            print("For example, if you want to run level 1, enter \'level\' and then \'1\'.")
            print("Please consult the GitHub documentation for a detailed description of all game pieces.\n")
        elif user_input == "quit":
            running = 0
        else:
            print("Invalid.")
    except KeyboardInterrupt:
        print("\nQuitting Green Sun...")
        running = 0

