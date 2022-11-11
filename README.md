###  llama.py v1.0.0 ![Alt text](images/llama.PNG?raw=true) --Splunk and Phantom Server Automation Framework-- 
#

## How To Install

1. From 'Software Center' install 'Visual Studio Code'.

![Alt text](images/screenshot1.PNG?raw=true)
#
2. From 'Software Center' install 'Python 3.8.10'.

![Alt text](images/screenshot2.PNG?raw=true)

### Note: if 'Python 3.8.10' install fails, try any other Python version 3.+ from 'Software Center'.
#
3. Open a CMD and paste the below one-liner command to download this repo, the dependencies and install them, then finally verify install as self check.
```
git clone https://stash.merck.com/scm/splnk/splunk-tools.git && git clone https://stash.merck.com/scm/splnk/paramiko-jump.git && cd .\paramiko-jump\ && python .\setup.py install && cd ../spluk-tools/inhouse-ansible/ && python ./inhouse-ansible.py --version
```
#
## TODO
- error handling
- add multi-threading
- add playbook support
- add logging on host + on target via " > llama.log"
- create Splunk dashboard