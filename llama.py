print('='*80)
print('llama v2.3.0')

from inventory import state
from sys import argv, exit
from packages.tmcolors import yellow, green, red
import paramiko
from packages.jump import SSHJumpClient

#menu
debug = False
max_argv = 3
class pb:
    loc = 'playbooks/'
    ext = '.sh'

#static
skip = [
    'stdin: is not a tty',
    'mesg: ttyname failed: Inappropriate ioctl for device',
    'stty: standard input: Invalid argument',
    '',
]

#var
class task:
    cache = []
    total = len(cache)
    debug = 1
    good = 0
    bad = 0
    target = None
    command = None
    need_jump = []
    no_jump = []
    status = None
    stdout = ''
    ssh_count = len(no_jump)
    jump_count = len(need_jump)
    color = None
    bad_servers = []
    stderr = ''

#fn
def log(text):
    global task
    print('='*80)
    print('[' + yellow('debug') + '] -> ' + str(task.debug))
    print(str(text))
    task.debug += 1

#argv length check
if len(argv) > 1: #pass gate
    if debug: log('pass len(argv) > 1') #pass gate
    if len(argv) > max_argv: #pass gate
        if debug: log('panic len(argv) > ' + str(max_argv))
        print('Too many arguemnts.\nExample: python .\llama.py phantom "ls -la | grep bashrc"\nBye.\n')
        exit()
    else:
        task.target = argv[1]
        if debug: log('pass argv length check, adding argv[1] to task.target')
else:
    if debug: log(red('panic no argv[1]'))
    print('\nNo target provided.\nExample: python .\llama.py phantom "ls -la | grep bashrc"\nBye.\n')
    exit()

#ssh 
def ssh(
    jump_check,
    jump_user,
    jump_pass,
    jump_srv,
    jump_port,
    srv_user,
    srv_pass,
    srv_ip,
    srv_port,
    command,
    hostname,
    ):

    if jump_check == True:
        if debug: log('passed jump check in ssh fn'); print(jump_check)
        # connect to jump
        try:
            with SSHJumpClient() as jumper:
                jumper.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                jumper.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
                if debug: log('attempting to start ssh connection to ' + str(srv_ip))
                jumper.connect(
                    hostname = jump_srv,
                    username = jump_user,
                    password = jump_pass,
                    port = jump_port,
                    disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']},
                )
                if debug: log('passed jump connectivity, attempting to connect to final target')
                # connect to target after/via jump
                target1 = SSHJumpClient(jump_session=jumper)
                target1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                target1.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
                if debug: log('debug check right before ssh attempt')
                target1.connect(
                    hostname = srv_ip,
                    username = srv_user,
                    password = srv_pass,
                    look_for_keys = False,
                    allow_agent = False,
                    port = srv_port,
                    disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']},
                )
                if debug: log('jump ssh, command to be executed'); print(command)
                # print result and add log on target
                _, stdout, stderr = target1.exec_command(command)

                # print back to C2C
                task.stdout = stdout.read().decode().strip()
                task.stderr = stderr.read().decode().strip()
                task.status = stdout.channel.recv_exit_status()
                if debug: log('jump ssh closing connection')
                # close connection
                target1.close()
                if debug: log('connection closed')
                task.good += 1
                task.color = 'g'

        except KeyboardInterrupt:
            print('Bye.\n')
            exit()
        except:
            task.stdout = red('Something went wrong. Could not ssh.')
            task.color = 'r'
            task.bad += 1
            task.bad_servers += [hostname]
            pass

    elif jump_check == False:
        if debug: log('normal ssh to be used in ssh fn'); print(jump_check)
            
        try:    
            # connect to target
            target1 = SSHJumpClient()
            target1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            target1.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
            if debug: log('debug check right before ssh attempt to ' + str(srv_ip))
            target1.connect(
                hostname = srv_ip,
                username = srv_user,
                password = srv_pass,
                look_for_keys = False,
                allow_agent = False,
                port = srv_port,
                disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']},
            )
            if debug: log('ssh, command to be executed'); print(command)
            # print result and add log on target
            _, stdout, stderr = target1.exec_command(command)

            # print back to C2C
            task.stdout = stdout.read().decode().strip()
            task.stderr = stderr.read().decode().strip()
            task.status = stdout.channel.recv_exit_status()
            if debug: log('ssh closing connection')
            # close connection
            target1.close()
            if debug: log('connection closed')
            task.color = 'g'
            task.good += 1
        except KeyboardInterrupt:
            print('Bye.\n')
            exit()
        except:
            task.stdout = red('Something went wrong. Could not ssh.')
            task.color = 'r'
            task.bad += 1
            task.bad_servers += [hostname]
            pass
            

#gui
def gui(z, x, c):

    if task.color == 'g':
        name_color = green(str(z))
    else:
        name_color = red(str(z))


    print('-'*80)
    print('[' + name_color + '] <=> ' + x + ' -> "' + c + '"')
    print('')
    if debug: log('printing stdout');print(task.stdout)
    if task.stdout == '':
        task.stdout = yellow('There is not output. This does not mean the cmd was not run.')
    print(task.stdout)

    if task.stderr in skip:
        pass
    else:
        print(task.stderr)
    print('')

#check argv[1] to be valid target
for entry in state:

    if task.target == entry[2]: #check by group
        if debug: log('pass found group'); print(entry)
        task.cache += [entry]

    if task.target == entry[1]: #check by hostname
        if debug: log('pass found hostname'); print(entry)
        if entry[2] == 'all':
            pass
        else:
            task.cache += [entry]


    if task.target == entry[10]: #check by ip
        if debug: log('pass found ip'); print(entry)
        if entry[2] == 'all':
            pass
        else:
            task.cache += [entry]

if len(task.cache) == 0:
    if debug: log(red('panic cache is empty')) #nothing found
    print('\nNo known target.\nExample: python .\llama.py phantom "ls -la | grep bashrc"\nBye.\n')
    exit()

#current task cache
if debug:
    log('current cache')
    for entry in task.cache:
        print(entry)
    print(task.cache)

#check argv[2] exists
if len(argv) > 2: #pass gates
    if debug: log('pass len(argv) > 2, adding argv[2] to task.command')
    task.command = argv[2]
    if debug: log('task command -> "' + str(task.command) + '"')
else:
    if debug: log(red('panic len(argv) > 2, too few argv'))
    print('\nTarget found, but no command provided.\nExample: python .\llama.py phantom "ls -lash | grep bashrc"\nBye\n')
    exit()

#check for empty task items
if debug:
    log('checking that task items are empty')
    print(task.need_jump, task.no_jump)

#check if jump server is needed
if debug: log('jump needed ?')
for entry in task.cache:
    if debug: print(entry[3])
    if entry[3] == True:
        if debug: log('found entry which needs jump server'); print(entry)
        task.need_jump += [entry]
    elif entry[3] == False:
        if debug: log('found entry which does not need jump server'); print(entry)
        task.no_jump += [entry] 

if debug: log('checking task len for ssh'); print(task.ssh_count, task.jump_count)

task.ssh_count = len(task.no_jump)
task.jump_count = len(task.need_jump)


#validate for task items
if debug:
    log(task.cache)
if debug:
    log('those don\'t need jump server')
    for entry in task.no_jump:
        print(entry)
if debug:
    if debug: log('those need jump server')
    for entry in task.need_jump:
        print(entry)

#sane check
if debug: log('validated\nargv({}) -> targets({})=>grouped -> cmd("{}")\nPRINTING CACHE'.format(str(len(argv)), task.target, task.command))
if debug:
    for entry in task.no_jump:
        log(entry[1])
    for entry in task.need_jump:
        log(entry[1])

#attempt to ssh for every entry in cache
if debug: log('checking task len for ssh'); print(task.ssh_count, task.jump_count)

for entry in task.no_jump:
    task.color = None
    task.stdout = ''
    task.status = None
    task.stderr = ''
    ssh(
        entry[3], entry[4], entry[5], entry[6], entry[7], entry[8], entry[9], entry[10], entry[11],
        task.command, entry[1],
    )
    gui(entry[1], entry[2], task.command)
    #task.stdout = ''
    if debug: log('checking stdout = cleared');print(task.stdout)

if debug: log('checking task len for ssh'); print(task.ssh_count, task.jump_count)

for entry in task.need_jump:
    ssh(
        entry[3], entry[4], entry[5], entry[6], entry[7], entry[8], entry[9], entry[10], entry[11], task.command, entry[1],
    )
    gui(entry[1], entry[2], task.command)
    #task.stdout = ''
    if debug: log('checking stdout = cleared');print(task.stdout)
task.bad_servers = ' '.join(task.bad_servers)
    
##
print('='*80)
print('Good:' + green(str(task.good)) + ' Bad:' + yellow(str(task.bad)) + ' -> ' + task.bad_servers)
print('')