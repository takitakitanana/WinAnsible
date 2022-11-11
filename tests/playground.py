from os import popen

print('Checking for python..')
if popen('python --version').read():
    print('Py Found.')
else:
    print('Py Not Found.')
