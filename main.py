import os
import json
import subprocess
from pywinauto import Application
import time
import pyautogui

"""
This program opens an Obsidian vault for you.
It finds the obsidian.json file in the Obsidian appdata folder and extracts the existing vaults and their paths.
Then it offers a list of vaults for the user to choose which to open.
The obsidian.json file keeps a tag to indicate which vault should be opened automatically on startup. In order for this
program to work, this behavior must be avoided. Obsidian offers no settings to facilitate this, but it can be achieved
by deleting the tag from the .json before opening Obsidian.
Once that is done, the program opens Obsidian and interacts with the launcher GUI to open the desired vault,
entering the corresponding directory (which was already found and saved in the first step).
Finally, the program exits.
"""


def extract_json_data():
    try:
        with open(os.path.expanduser('~\\AppData\\Roaming\\obsidian\\obsidian.json'), "r") as file:
            return file.read()
            # Returns a string
    except FileNotFoundError:
        print("Error: the 'obsidian.json' file couldn't be found in the appdata\\roaming\\obsidian folder.\nProgram will exit now.")
        exit()


def offer_choice(json_string):
    json_dictionary = json.loads(json_string)  # Loads the string as a dictionary to easily extract vault paths
    vault_paths = [entry['path'] for entry in json_dictionary['vaults'].values()]  # Creates a list with the vault paths
    print("The following vaults have been found:")
    counter = 1
    for path in vault_paths:
        print(f"{counter} - {os.path.basename(path)}")
        counter += 1  # counter variable to print the list with numbers 1...n
    while True:
        user_choice = input("Press the corresponding number to open a vault, or enter \"q\" to quit this program "
                            "without making any changes:\n")
        if user_choice.isdigit():
            if 0 < int(user_choice) < counter:
                remove_open_tag(json_string)
                open_vault((vault_paths[int(user_choice) - 1]))
                return
            elif user_choice.isdigit() and int(user_choice) == 0:
                create_vault(os.path.dirname(path))  # This "path" is taken from the for loop right before. It references
                # the last path that was checked, and takes the directory name. This will cause trouble if a user attempts
                # to keep vaults in different folders.
            else:
                print("Invalid number. Input must be a valid vault number or 0")
        elif user_choice in {"q", "Q"}:
            print("Quitting program")
            exit()
        else:
            print("Input must be a valid integer or \"q\"")


def remove_open_tag(data):
    if ",\"open\":true" in data:
        data = data.replace(",\"open\":true", "")
        with open(os.path.expanduser('~\\AppData\\Roaming\\obsidian\\obsidian.json'), 'w') as file:
            file.write(data)
    return


def open_vault(vault_path):
    try:
        subprocess.Popen(os.path.expanduser('~\\AppData\\Local\\obsidian\\obsidian.exe'))
    except FileNotFoundError:
        print("Error: the 'obsidian.exe' file couldn't be found in the appdata\\local\\obsidian folder."
              "\nSorry, this program does not currently support alternative installation folders.\nProgram will exit now.")
        exit()
    time.sleep(1)
    click_obsidian_button(vault_path)
    return


def click_obsidian_button(vault_path):
    obsidian_window = find_obsidian_window()
    try:
        open_button = obsidian_window.child_window(title="Open", control_type='Button')
        open_button.click_input()
    except Exception as e:
        print(f"Error clicking the \"Open\" button: {e}")
    try:
        pyautogui.write(vault_path)
        pyautogui.press("tab")  # This tab ensures that the cursor moves to the Select Folder button before pressing Enter.
        pyautogui.press("enter")
    except Exception as e:
        print(f"Error entering the chosen vault into the Select Folder dialog: {e}")
    return


def find_obsidian_window():
    try:
        app = Application(backend="uia").connect(title="Obsidian")
        main_window = app.top_window()
        return main_window
    except Exception as e:
        print(f"Error finding Obsidian window: {e}")
        exit()


def create_vault(vaults_folder):
    while True:
        desired_name = input("Enter name for the new vault. It must be <= 260 characters, and can't include \\/:*?\"<>|"
                             "\n>>> NOTE: the new vault will be opened immediately and this program will exit. This step <<<\n"
                             ">>> is necessary for the vault to be initialized and obsidian.json to be updated by Obsidian <<<"
                             "\nAlternatively, enter an empty string to go back to the previous menu:\n")
        if desired_name == "":
            return
        elif not any(char in '\\/:*?\"<>|' for char in desired_name):
            if len(desired_name) <= 260:
                try:
                    new_vault = os.path.join(vaults_folder, desired_name)
                    os.makedirs(new_vault)
                    print("The requested folder has been created and may be opened as a vault. It will now be opened.")
                    open_vault(new_vault)
                except FileExistsError:
                    print("This vault already exists")
            else:
                print(f"Unable to create vault: must be <= 260 characters. Current count: {len(desired_name)} characters\n")
        else:
            print("Unable to create vault: name may not include \\/:*?\"<>|")


def main():
    offer_choice(extract_json_data())


if __name__ == '__main__':
    main()
