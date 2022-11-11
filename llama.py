### llama modules ###
import inventory

### python modules ###
import sys, os

### dependencies ###
import paramiko
from paramiko_jump import SSHJumpClient

### config menu ###
debug = False
max_argv = 3

### static ###
# colors
pref = "\033["
reset = f"{pref}0m"

class colors:
    red = "31m"
    green = "32m"
    white = "37m"

### functions ###
# colors

# logic
def run_logic(rules, whattorun):

    if debug == True:
        print('[debug]' + ' 3 test argv')

    # iterate through inventory list
    for server, value in rules.items():
        # validate target
        if sys.argv[1] in inventory.servers[server]['group']:
            # check for jump server flag
            if inventory.servers[server]['jump'] == False:
                # send ssh cmd
                ssh(
                    server,
                    inventory.servers[server]['user'],
                    inventory.servers[server]['pass'],
                    inventory.servers[server]['port'],
                    inventory.servers[server]['host'],
                    whattorun,
                )

                # new line
                print('-'*80)

            # check for jump server flag
            elif inventory.servers[server]['jump'] == True:
                # send ssh cmd via jump server
                jump_ssh(
                    inventory.servers[server]['jump_server'],
                    inventory.servers[server]['jump_user'],
                    inventory.servers[server]['jump_pass'],
                    inventory.servers[server]['port'],
                    server,
                    inventory.servers[server]['user'],
                    inventory.servers[server]['pass'],
                    inventory.servers[server]['port'],
                    whattorun,
                    inventory.servers[server]['host'],
                )

                # new line
                print('-'*80)

        # check for target
        elif sys.argv[1] == 'all':
            # iterate through inventory list
            for server, value in inventory.servers.items():

                # debug check
                if debug == True:
                    print(inventory.servers[server])

                # check for jump server flag
                if inventory.servers[server]['jump'] == False:
                    try:
                        # send ssh cmd
                        ssh(
                            server,
                            inventory.servers[server]['user'],
                            inventory.servers[server]['pass'],
                            inventory.servers[server]['port'],
                            inventory.servers[server]['host'],
                            whattorun,
                        )

                    # panic
                    except KeyboardInterrupt:
                        print('Bye.\n')
                    except:
                        print('Ops.\n')

                    # new line
                    print('-'*80)

                # check for jump server flag
                elif inventory.servers[server]['jump'] == True:
                    try:
                        # send ssh cmd via jump server
                        jump_ssh(
                            inventory.servers[server]['jump_server'],
                            inventory.servers[server]['jump_user'],
                            inventory.servers[server]['jump_pass'],
                            inventory.servers[server]['port'],
                            server,
                            inventory.servers[server]['user'],
                            inventory.servers[server]['pass'],
                            inventory.servers[server]['port'],
                            whattorun,
                            inventory.servers[server]['host'],
                        )

                    # panic
                    except KeyboardInterrupt:
                        print('Bye.\n')

                    except:
                        print('Ops.\n')

                    # new line
                    print('-'*80)

                else:
                    # not found
                    print('No groups found.')

    if debug == True:
        print('[debug]' + ' 4 test argv')

# ssh no jump
def ssh(server_ip, user, passw, port, hostname, command):

    # ssh to target
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    com = command
    client.connect(
        hostname=server_ip,
        username=user,
        password=passw,
        port=port,
        disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']}
    )
    output = ''

    # print result and log activity on target machine
    stdin, stdout, stderr = client.exec_command(command# + ' && echo "test1" > ~/inhome-ansible.log"'
    )

    stdout=stdout.readlines()

    # clone connection
    client.close()

    # print result back to C2C
    for line in stdout:

        if (output+line)!="":
            print(line.strip())

# ssh via jump
def jump_ssh(jump_server, jump_user, jump_pass, jump_port, server2, username, passwd, port, command, server_name):

    # connect to jump
    with SSHJumpClient() as jumper:
        jumper.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        jumper.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
        jumper.connect(
            hostname = jump_server,
            username = jump_user,
            password = jump_pass,
            port = jump_port,
            disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']},
        )

        # connect to target after/via jump
        target1 = SSHJumpClient(jump_session=jumper)
        target1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        target1.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
        target1.connect(
            hostname = server2,
            username = username,
            password = passwd,
            look_for_keys = False,
            allow_agent = False,
            port = port,
            disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']},
        )

        # print result and add log on target
        _, stdout, _ = target1.exec_command(command# + ' && echo "test1" > ~/inhome-ansible.log"'
        )

        # print back to C2C
        print(stdout.read().decode().strip())

        # close connection
        target1.close()

# self check/test
def sane_check():

    # debug check
    if debug == True:
        print('[debug]' + ' 2 test argv')

    run_logic(inventory.servers, '"ls -la | grep bashrc"')

    # debug check
    if debug == True:
        print('[debug]' + ' 5 test argv')

# where logic is run            
def main():
    try:
        run_logic(inventory.servers, sys.argv[2])

    # panic
    except KeyboardInterrupt:
        print('Bye.\n')
    except:

        # debug check
        if debug == True:
            print(run_logic())

        print('Ops.\n')

##########    BEGIN    ##########
# entry point checks

# check for length
if len(sys.argv) > max_argv:
    print('Too many arguments.\nExample: python .\llama.py syslog "ls -la | grep history"\nBye.\n')
    exit()

else:
    # check for the first word
    # help
    if sys.argv[1] == 'version':
        os.system('cls')
        print('llama.py v1.0.0\nBye.\n')
        exit()

    # self check
    elif sys.argv[1] == 'test': 

        # debug check
        if debug == True:
            print('[debug]' + ' 1 test argv')
            print(sane_check)

        sane_check()

        # debug check
        if debug == True:
            print('[debug]' + ' 6 test argv')

    else:
        # begin main
        print('-'*80)
        main()

