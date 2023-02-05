# griefficient-filter

Runs [<img src="https://camo.githubusercontent.com/b079fe922f00c4b86f1b724fbc2e8141c468794ce8adbc9b7456e5e1ad09c622/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f6769746875622e737667" alt="gh" width="18"/>](https://github.com/Odyssey346/Griefficient) **[Odyssey346/Griefficient](https://github.com/Odyssey346/Griefficient)** and filters it's output using Python 3.

### ⚠️ Warning, only tested on Windows 10! ⚠️

**⚠For educational purposes only!⚠**

## Installation

- Install [<img src="https://camo.githubusercontent.com/b079fe922f00c4b86f1b724fbc2e8141c468794ce8adbc9b7456e5e1ad09c622/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f6769746875622e737667" alt="gh" width="18"/>](https://github.com/Odyssey346/Griefficient) **[Odyssey346/Griefficient](https://github.com/Odyssey346/Griefficient)**
- Clone this project and `cd` into it
- Run `python3 -m pip install -r requirements.txt`

## Usage

- Run `python3 main.py -h` to get help
  
## Examples

- `python3 main.py -m w -f 1.16,1.17`
  - **Only shows** servers on version **1.16.\*** and **1.17.\***

- `python3 main.py -m b -f 1.19,1.18.2`
  - **Shows all servers except** servers on version **1.19.\*** and **1.18.2**

- `python3 main.py -m b -f 1.19.1 -g`
  - **Shows all servers except** servers on version **1.19.1** and shows the servers gradually (on `ENTER` key press)
  
- `python3 main.py -g`
  - **Shows 100 servers** and shows them gradually (on `ENTER` key press)

- `python3 main.py -g -pr`
  - **Shows 100 servers** and shows them gradually (on `ENTER` key press) and starts a proxy
  - You can now connect to the currently shown server with this adress: `127.0.0.1`
  - Pressing enter makes `127.0.0.1:25565` point to the new server and you don't have to copy-paste anything

- `python3 main.py -g -pr -p 25566`
  - Same as the above example, but you connect to the currently shown server using `127.0.0.1:25566`
