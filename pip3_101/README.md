# Python3 pip3 101
This guide shows how to use pip3 to manage Python packages on Debian based systems.
pip is used to extend the commands contained in Python by installing 3rd party packages.
There some packes included in Python3 which can be imported , others have to be installed first using pip3.

For example :
- 'requests' must be installed first.
- 'math' is included and can be imported

Sometimes users need to use root rights for pip3 install.
This depends of the installation of the system.

## An example of missing packages (requests)
    #python3
    >>>import requests
       this will result in error: ImportError: No module named requests
## pip3 help
    #pip3 --h

## Install pip3
    #sudo apt-get update
    #sudo apt-get upgrade
    #sudo apt-get install python-pip3

## Upgrade pip3
    #pip3 install --upgrade setuptools pip

## Show all installed packages
    #pip3 list
        example output:  bottle (0.12.13)

## Install package (example package: requests)
    #pip3 install requests
    #pip3 list
        example output: requests (2.22.0)

## show outdated packages
    #pip3 list --outdated

## Upgrade a package (example package: requests)
    #pip3 install --upgrade requests

## uninstall package
    #pip3 uninstall requests

## create requirements file
this files will include all installed packages and their versions
    #pip3 freeze >> requirements.txt
    
## show package informations
    #pip3 show requests
    
## search for a 3rd party package
    #pip3 search mqtt



Have fun !


created by tsterber

