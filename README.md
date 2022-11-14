###  llama.py v1.0.0 ![Alt text](images/llama.PNG?raw=true) --Splunk and Phantom Server Automation Framework-- 
#
## How To Use
- From the same directory
```code
python llama.py <TARGET> <CMD>
```
Example
```code
python llama.py all pwd
```
Target is selected from inventory row number
```code
<TARGET>
```

#
## How To Install

1. From 'Software Center' install 'Python 3.7' and (optionally 'Visual Studio Code' -> as code editor).

#### Note: if 'Python 3.7' install fails, try any other Python version 3.7+ from 'Software Center'.


2. Open a Powershell prompt and install git and python dependency.
- git
```code
winget install --id Git.Git -e --source winget
```
![Alt text](images/screenshot2.PNG?raw=true)
- python
```code
python -m pip install paramiko
```

3. Open a CMD and clone this repository, then check everything is installed.
```
git clone https://stash.merck.com/scm/splnk/llama.git
```
```code
python llama/llama.py
```
![Alt text](images/screenshot3.PNG?raw=true)
#
## TODO
- add scp support
- add playbook support
- add multi-threading
- add logs
- create Splunk dashboard from logs

## Known Issues
#
- If target is given an ip or hostname from inventory the command will run twice. Run only groups as the target.
 - Sometimes "Secsh channel 0 open FAILED: Connection refused: Connect failed" debug info pops up without debug flag set to True..