import os
import json

"""
This program opens an Obsidian vault for you.
It finds the obsidian.json file in the Obsidian appdata folder and extracts the existing vaults and their paths.
Then it offers a list of vaults for the user to choose which to open.
This .json file keeps a tag to indicate which vault should be opened automatically on startup. In order for the
program to work, this behavior must be avoided. Obsidian offers no settings to facilitate this, but it can be achieved
by deleting the tag from the .json before opening Obsidian.
Once that is done, the program opes Obsidian and interacts with the launcher GUI to open the desired vault,
entering the corresponding directory (which was already found and saved in the first step).
Finally, the program exits.
"""


def extract_json_data():
    if os.path.exists(os.path.expanduser('~\\AppData\\Roaming\\obsidian\\obsidian.json')):
        with open(os.path.expanduser('~\\AppData\\Roaming\\obsidian\\obsidian.json'), "r") as file:
            return file.read()
            # Returns a string
    else:
        print("Error: the 'obsidian.json' file couldn't be found in the appdata\\roaming folder.\nProgram will exit now.")
        exit()



def remove_open_tag(data):
    if ",\"open\":true" in data:
        data = data.replace(",\"open\":true", "")
        with open(os.path.expanduser('~\\AppData\\Roaming\\obsidian\\obsidian.json'), 'w') as file:
            json.dump(data, file)
    return


def offer_choice(json_string):
    json_dictionary = json.loads(json_string)  # Loads the string as a dictionary to easily extract vault paths
    vault_paths = [entry['path'] for entry in json_dictionary['vaults'].values()]  #  Creates a list with the vault paths
    print("The following vaults have been found:")
    counter = 1
    for path in vault_paths:
        print(f"{counter} - {os.path.basename(path)}")
        counter += 1
    while True:
        user_choice = input("Press the corresponding number to open a vault, or enter \"q\" to quit this program "
                            "without making any changes\n")
        if user_choice.isdigit() and 0 < int(user_choice) < counter:
            remove_open_tag(json_string)
            open_vault(user_choice)
        elif user_choice in {"q", "Q"}:
            print("Quitting program")
            exit()
        else:
            print("Input must be a valid integer or \"q\"")


def open_vault(vault):
    print(vault, " detected, open_vault online")
# notice that it's receiving an integer. This number -1 should equal the required index for whichever vault
# the user wants to open
# remember to exit() the program, or we'll stay stuck in the while True loop from offer_choice


def main():
    offer_choice(extract_json_data())


if __name__ == '__main__':
    main()
