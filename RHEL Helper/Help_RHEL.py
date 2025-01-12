from pathlib import Path
import os
# Clearing the Screen
os.system('cls')

# Menu Header 
print("############### Shell Helper Menu #####################")

# Determine the path to 'menu.txt' in the current directory
p = Path(__file__).with_name('menu.txt')

# Open and read the file
with p.open('r') as f:
    # Read all lines from the file and strip leading/trailing whitespace
    lines = [line.strip() for line in f.readlines()]

# Sort the lines alphabetically
lines.sort()

# Display each line with an incrementing integer
for index, line in enumerate(lines, start=1):
    print(f"{index}. {line}")

# Menu Header 
print("#######################################################")

# Prompt the user to choose an integer from the menu
try:
    selection = int(input("\nChoose an integer from the menu above: "))
    if 1 <= selection <= len(lines):
        selected_line = lines[selection - 1]   
    else:
        print("\nInvalid selection. Please choose a number from the menu.")
except ValueError:
    print("\nInvalid input. Please enter a valid integer.")

os.system('cls')

# Prints the Data to Screen from Txt file
p = Path(__file__).with_name(f"{selected_line}.txt")
with p.open('r') as f:
    print(f.read())
print("\n")
input("Press Enter to continue...")