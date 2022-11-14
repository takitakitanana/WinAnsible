###  llama.py v1.0.0 ![Alt text](images/llama.PNG?raw=true) --Splunk and Phantom Server Automation Framework-- 
#

## How To Install

1. From 'Software Center' install 'Visual Studio Code' and 'Python 3.7'
### Note: if 'Python 3.7' install fails, try any other Python version 3.7+ from 'Software Center'.


2. Open a Powershell prompt and install git and python dependency.
- git
```code
winget install --id Git.Git -e --source winget
```
- python
```code
python -m pip install paramiko
```


3. Open a CMD and clone this repository and check everything is installed.
```
git clone https://stash.merck.com/scm/splnk/llama.git && cd .\llama\ && python .\llama.py
```

4. (optional) All commands -> 1 liner -> PowerShell
```
winget install --id Git.Git -e --source winget && python -m pip install paramiko && git clone https://stash.merck.com/scm/splnk/llama.git && cd .\llama\ && python .\llama.py
```

#
## TODO
- add scp support
- add multi-threading
- add playbook support
- create Splunk dashboard

## Known Issues
#
 - "Secsh channel 0 open FAILED: Connection refused: Connect failed" debug info pops up without Debug flag enabled.