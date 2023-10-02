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
Volcano is compatible with Obsidian 1.4.13 and should work on any modern Windows release.

Built with Python.
Tested on Windows 10.

> How does it work?

The file obsidian.json can be found in ...\appdata\roaming\obsidian. It lists the existing vaults and the folder where
they're located. Volcano retrieves this data and presents it to the user as a list, each with a corresponding number
in the range 1...n. The user can enter one of these numbers, and Volcano will open the Obsidian launcher (assumed to be
in its default location, in ...\appdata\local\obsidian) and interact with the launcher's GUI to open the desired vault.
Alternatively, the user can create a new vault by entering 0. Sadly there is no (official) way to interact with Obsidian
directly from the command line.

There is an issue: by default, Obsidian opens the last closed vault, and there are no options to disable this. However,
Obsidian identifies which vault was closed last by adding the tag *,"open":true* to that vault's entry in obsidian.json,
and Obsidian's behavior defaults to opening the launcher when this tag cannot be found. When instructed to open a vault,
Volcano removes first the tag from obsidian.json before running Obsidian, to ensure that the launcher opens directly.

> What did I use to make it?

> Challenges?

- 

> Limitations

Volcano assumes that all vaults are in the same folder. It doesn't support multiple locations.
A standard installation is also assumed. The default location of Obsidian is in ...\appdata\local\obsidian, while the
obsidian.json file is found in ...\appdata\roaming\obsidian. Since obsidian.json 

> Future development possibilities

- Creation of new vaults
- Support for different filepaths than default
- Linux support

> What did I learn?

Sadly the pun doesn't work. Obsidian is usually created by rapidly cooling, high-silica lava that's already been thrown out by the volcano,
so volcanoes don't actually launch obsidian. A major flaw in an otherwise functional program.
