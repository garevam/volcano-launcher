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
    # HERE: the variable data contains the json_string. Add code to remove the open tag from there.
    with open('address', 'w') as file:
        json.dump(data, file)
    return



def offer_choice(json_string):


    # next step: extract vault name + address from the variable holding the json data string
    # lists options and asks the user what to open, or offers to quit
    # if the user chooses to quit, exit. No changes are made at all
    # if the user chooses a vault, summon remove_open_tag(json_data_dictionary)
    #   and then the function to manipulate the Obsidian GUI. Alternatively, do that directly here but then
    #   rename this "handle_choice(json_data_dictionary)"

# def open_vault(AS TOLD FROM offer_choice):


"""
NOTE FOR THE FUNCTION FISHING UP ADDRESSES FROM .JSON: COPY .JSON TO A VARIABLE, THEN EDIT .JSON TO REMOVE TAG, AND
SAVE+CLOSE .JSON. THEN FIND THE ADDRESSES IN THE VARIABLE DIRECTLY! Why? Because for small text it's more efficient to
work from memory than to read from a file, and since this .json only contains vault addresses and a couple tags, it's
reasonable to expect that it won't ever be too large.
And we're doing this to launch a program that's much heavier than the weight of that .json in the ram, so obviously
we expect to have that much ram free right now.
"""

def main():
    offer_choice(extract_json_data())


if __name__ == '__main__':
    main()
