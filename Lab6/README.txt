# Title: Lab 6: Optimization, User Interfaces, README

## Date: 2023-12-08
## Software's Name and Version: Data Fitter 1.0
## Contact Infromation: StefanMartincevic@cmail.carleton.ca

## Description: 

A command line application that enables the user to either load data, sort data, generate a curve fit, generate a histogram, or exit the program. The input data is taken from a file to load the data. Afterwards, this data may be fit/analyzed by sorting the data in part of a specific parameter, fit the data as a curve on a graph, or as a histogram.  

## Dependencies: 

Python 3.11.5
Matplotlib
NumPy

## Installation: 

### Installation of Python 3.11.5 (https://www.python.org/downloads/)

Follow instructions listed on the offered link to download Python 3.11.5 or the latest version of Python.

### Installation of Matplotlib and NumPy on Windows

#### Step 1 - Check Python and pip

Open a Command Prompt window. After the prompt (C:>), type the command "python --version" to verify that the recent release of python is installed:

C:> python --version
Python 3.11.5

If the Python version is older than Python 3.10, it is strongly recommended that the most recent release of python is installed and downloaded (https://www.python.org/downloads/).If a message is printing stating that "python" isnt recognized, it is probable that it was not added to the Windows PATH variable during installation. In this case, run the installer, select "Modify", check the "Add Python to PATH" checkbox and click "Install". Ensure that the "pip - Installs pip..." checkbox is also checked. 

"pip" (the package installer for Python) is automatically installed if Python was download from (https://www.python.org/downloads/). The command "python -m pip --version" should be typed to varify that pip is installed:

C:> python -m pip --version
pip x.y.z from path/pip (python 3.11.5)

Type the command "python -m pip install --upgrade pip" to upgarde to the newest available version of pip, if it is available:

C:> python -m pip install --upgrade pip

A .whl file will be downloaded containing the latets version of pip. This should be installed, replacing the older version. When the installation isfinished, the message "Successfully installed pip-x.y.x" is displayed. In the case that pip is not installed, run "ensurepip" in the command below ot install it:

C:> python -m ensurepip

#### Step 2 - Install Matplotlib

Run "pip" as shown in the command below to install the Matplotlib library:

C:> python -m pip install matplotlib

pip will download and install several .whl files containg packages that are required for the installation of Matplotlib. When the installation is completed, the message "Successfully installed a
list of package names, including matplotlib-x.y.z and numpy-x.y.z" is displayed. 

#### Step 3 - Install NumPy

NumPy should have been installed with the installation of Matplotlib, but "pip" will be utilised to ensure this with the following command:

C:> python -m pip install numpy

NumPy is installed if the message "Requirement already satisfied: numpy in path (x.y.z)" is displayed. If NumPy is not installed, pip will download and install it. 
  
### Installation of Matplotlib and NumPy on macOS

#### Step 1 - Check Python and pip

Open the terminal and after the prompt "$" type the command "python3 --version" to verify that the latets relase of python has been installed as shown bellow:
 
$ python3 --version
Python 3.11.2

If the Python version is older than Python 3.10, it is strongly recommended that the most recent release of python is installed and downloaded (https://www.python.org/downloads/).

"pip" (the package installer for Python) is automatically installed if Python was download from (https://www.python.org/downloads/). The command "python3 -m pip --version" should be typed to varify that pip is installed:

$ python3 -m pip --version
pip x.y.z from path/pip (python 3.11

Type the command "python3 -m pip install --upgrade pip" to upgarde to the newest available version of pip, if it is available:

A .whl file will be downloaded containing the latets version of pip. This should be installed, replacing the older version. When the installation isfinished, the message "Successfully installed pip-x.y.x" is displayed. In the case that pip is not installed, run "ensurepip" in the command below ot install it:

$ python3 -m ensurepip

#### Step 2 - Install Matplotlib

Run "pip" as shown in the command below to install the Matplotlib library:

$ python3 -m pip install matplotlib

pip will download and install several .whl files containg packages that are required for the installation of Matplotlib. When the installation is completed, the message "Successfully installed a
list of package names, including matplotlib-x.y.z and numpy-x.y.z" is displayed. 

#### Step 3 - Install NumPy

NumPy should have been installed with the installation of Matplotlib, but "pip" will be utilised to ensure this with the following command:

$ python3 -m pip install numpy

NumPy is installed if the message "Requirement already satisfied: numpy in path (x.y.z)" is displayed. If NumPy is not installed, pip will download and install it.

### Running the application

Application is downloaded as *.zip file in Download folder from Brightspace. The *.zip file has to be exctracted into desired folder by right mouse click->Extract all... and follow the prompt. After extraction   
go to the target folder and run Python.

## Usage:

## Credits: 
	
load_data.py - Esosa Ohangbon, Lance Downton, Ivan Wang, Stefan Martincevic
sort.py - Esosa Ohangbon, Lance Downton, Ivan Wang, Stefan Martincevic 	
curve_fit.py - Esosa Ohangbon
hisotgram.py - Stefan Martincevic
Text_UI.py - Lance Downton
Batch_User - Ivan Wang 

## License: 

MIT License 

Copyright (c) [2023] [Stefan Martincevic]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.		

