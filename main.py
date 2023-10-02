import os
import json


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
    if os.path.exists(os.path.expanduser('~\\AppData\\Roaming\\obsidian\\obsidian.json')):
        with open(os.path.expanduser('~\\AppData\\Roaming\\obsidian\\obsidian.json'), "r") as file:
            return file.read()
            # Returns a string
    else:
        print("Error: the 'obsidian.json' file couldn't be found in the appdata\\roaming folder.\nProgram will exit now.")
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
            elif user_choice.isdigit() and int(user_choice) == 0:
                create_vault(os.path.dirname(path))
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
            json.dump(data, file)
    return


def open_vault(vaultpath):
    print(vaultpath, " detected, open_vault online. Uncomment to test!")
    # receives a vaultpath. Simply launch obsidian.exe (...\appdata\local\obsidian)
    # interact with GUI to open the desired folder as vault
    # remember to exit() the program, or we'll stay stuck in the while True loop from offer_choice


def create_vault(vaults_folder):
    while True:
        desired_name = input("Enter name for the new vault. It must be <= 260 characters, and can't include \\/:*?\"<>|"
                             "\n>>> NOTE: the vault will be opened immediately and this program will exit. This step is necessary"
                             ">>> for the vault to be initialized and obsidian.json to be updated by Obsidian."
                             "\nAlternatively, enter an empty string to go back to the previous menu:")
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
                print(f"Unable to create vault: must be <= 260 characters. Current count: {len(desired_name)} characters")
        else:
            print("Unable to create vault: name may not include \\/:*?\"<>|")


def main():
    offer_choice(extract_json_data())


if __name__ == '__main__':
    main()
