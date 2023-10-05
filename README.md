# volcano-launcher
Volcano is a launcher for the personal wiki software Obsidian. The purpose of Volcano is to make it easier to open
Obsidian with a  specific vault (wiki), and to do so as fast as possible. The only extra feature is creating a new empty
vault, which is  as simple as creating a new folder in the right directory.


The default Obsidian launcher is tailored to users with a single vault (through the function to automatically open the
last used vault), or users who regularly switch between 4-5 vaults (through the recently opened menu). Any vault not
"recently" accessed is forgotten and must be reselected manually. There is no support for users who prefer to keep
separate vaults for different purposes and only rarely access some of them. Volcano should help bridge that gap, allowing
quick access to all vaults.

Obsidian is currently under active development, which might break compatibility with this program.

Built with Python.
Tested on Windows 10, with Obsidian 1.4.13. It works on my machine as of 05.10.2023; your mileage may vary.

This software or I are not in any way associated with or part of Obsidian.

### To do

- Pack as a comfortable executable file.

### How does it work?

The file obsidian.json can be found in ...\appdata\roaming\obsidian. It lists the existing vaults and the folder where
they're located. Volcano retrieves this data and presents it to the user as a list, each with a corresponding number
in the range 1...n. The user can enter one of these numbers, and Volcano will open the Obsidian launcher (assumed to be
in its default location, in ...\appdata\local\obsidian) and interact with the launcher's GUI to open the desired vault.
Alternatively, the user can create a new vault by entering 0. Sadly there is no (official) way to interact with Obsidian
directly from the command line, and the Obsidian API is only reachable through Obsidian files.

There is an issue: by default, Obsidian opens the last closed vault, and there are no options to disable this. However,
Obsidian identifies which vault was closed last by adding the tag *,"open":true* to that vault's entry in obsidian.json,
and Obsidian's behavior defaults to opening the launcher when this tag cannot be found. When instructed to open a vault,
Volcano removes first the tag from obsidian.json before running Obsidian, to ensure that the launcher opens directly.

This program's functions are very atomic, maybe a bit too much, but Obsidian is currently under rapid development. The
atomization is intended to make it easier to fix if an Obsidian update breaks compatibility.

### What did I use to make it?

It's a simple Python script with some standard libraries, pywinauto and pyautogui.

### Challenges?

I had never written a program before to interact with another programs' GUI and I had quite a lot of trouble getting
it to click the Open button: I kept getting an error about there being 4 different "Open" buttons. In the end, and after
carefully studying the GUI with the inspect.exe tool from the Windows SDK to find some unique identifier, I noticed that
I had placed the 'time.sleep(1)' in the wrong location, so the program was not waiting for the GUI to open before
executing the click. Correcting this fixed the entire issue. Very fortunately, because I couldn't find more than one
"Open" button.

### Limitations

- A standard installation is assumed: the default location of Obsidian is in ...\appdata\local\obsidian, while the  file obsidian.json file is found in ...\appdata\roaming\obsidian. Any changes here will break the program.
- Due to the (at this point) lack of an official API (that can also be reached from outside of an Obsidian document), it is necessary to manually press the buttons of the launcher. This slows down the execution time considerably.
- While Obsidian doesn't technically force the user to keep all vaults in a single folder, it's intended behavior. This program allows multiple locations as long as they're known to Obsidian. The Create Vault function might create the new vault in the wrong folder, though, since it'll always choose the location of the vault listed last in obsidian.json

### Future development possibilities

- Increase execution speed by replacing the 'time.wait(1)' command in line 73 with a function to continuously check whether the window is ready for the click
- Support for different filepaths than default, with an automated search function, an option for manual input, and a config file to save the address for future reference
- Linux support, with automatic system identification + (Support for different filepaths...)
- Some extra tools to rename vaults, duplicate them, archive them...
- GUI

### What did I learn?

I got to mess with some libraries and get a taste of manipulating external GUIs. The main lesson was to pay attention to timing
when interacting with a different program.

### Disappointment

Sadly the pun in the name doesn't work. Obsidian is usually created by rapidly cooling, high-silica lava that's already
been thrown out by a volcano, so volcanoes don't actually launch obsidian. A major flaw in an otherwise functional
program.
