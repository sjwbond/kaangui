# Python (PyQt5) Frontend

## Configuration
- Make a copy of *settings.default.json* and rename it to *settings.json*
- Open *settings.json* with a text editor
- If you are running the backend on a remote server, do the following:
    - In the line that says `"api_path": "http://localhost:3000",` change `http://localhost:3000` to the URL pointing to the backend
- You can change all of the options, choices, object types, and properties available in the program through this file
- Save the file when done

## Installation
- [Download and install Anaconda](https://www.anaconda.com/download)
- Open Powershell
    - Press Windows+R, type `pwsh`, and hit enter
- Change into the directory where the backend is installed (replace *path\to\backend* with the path to the backend folder)
    - Type `cd path\to\backend` and hit enter
- Create a new Conda environment
    - Type `conda create -n gui python=3.9` and hit enter
- Activate the Conda environment
    - Type `conda activate gui` and hit enter
- Install the Python dependencies
    - Type `pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt` and hit enter

## Running
- Open Powershell
    - Press Windows+R, type `pwsh`, and hit enter
- Change into the directory where the PyQt5 frontend is installed (replace *path\to\frontend-pyqt5* with the path to the PyQt5 frontend folder)
    - Type `cd path\to\frontend-pyqt5` and hit enter
- Activate the Conda environment
    - Type `conda activate gui` and hit enter
- Start the backend
    - Type `python main.py` and hit enter

## Development

### Editing UIs
The files with the extension *.ui* define the layout of some of the GUI screens. You can edit these files using Qt Designer. You can run Qt Designer by following the steps below:

- Open Powershell
    - Press Windows+R, type `pwsh`, and hit enter
- Activate the Conda environment
    - Type `conda activate gui` and hit enter
- Run Qt Designer
    - Type `qt5-tools designer` and hit enter

Once you have Qt Designer open, you can edit *.ui* files but for your changes to take effect, you have to update the corresponding Python file. To do so, in Qt Designer open the *Form* menu and select *View Python Code...*. Then copy only definitions for the two functions *setupUi* and *retranslateUi* from the window (starting with the line that says `def setupUi(self, Dialog):` until the end of the text), open the Python file matching the *.ui* file, select the definitions of these two functions in that file, and paste the new contents, replacing only these 2 functions in the process. Finally save your changes.