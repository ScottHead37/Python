from pathlib import Path
import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()

    # Menu Header 
    print("############### Shell Helper Menu #####################")

    # Determine the path to 'menu.txt' in the current directory
    p = Path(__file__).with_name('menu.txt')

    # Open and read the file
    with p.open('r') as f:
        lines = [line.strip() for line in f.readlines()]

    # Sort the lines alphabetically
    lines.sort()

    # Display menu options
    for index, line in enumerate(lines, start=1):
        print(f"{index}. {line}")

    # Exit option
    print(f"{len(lines) + 1}. Exit")

    print("#######################################################")

    # Prompt the user to choose an option
    try:
        selection = int(input("\nChoose an option (enter a number): "))

        # Exit condition
        if selection == len(lines) + 1:
            print("\nExiting...")
            break  # Breaks the while loop and ends the program

        # Valid selection check
        if 1 <= selection <= len(lines):
            selected_line = lines[selection - 1]
        else:
            print("\nInvalid selection. Please choose a valid number.")
            input("\nPress Enter to continue...")
            continue  # Go back to the menu

    except ValueError:
        print("\nInvalid input. Please enter a valid integer.")
        input("\nPress Enter to continue...")
        continue  # Restart the menu loop

    # Clear the screen before displaying the selected data
    clear_screen()

    # Display the content of the selected file
    p = Path(__file__).with_name(f"{selected_line}.txt")
    
    if p.exists():
        with p.open('r') as f:
            print(f.read())
    else:
        print(f"\nError: File '{selected_line}.txt' not found.")

    print("\n")
    input("Press Enter to return to the menu...")
