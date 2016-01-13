#

import subprocess

def execute(command):    
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    # nothing intersting in stdout, all the action is in stderr
    lines_iterator = iter(popen.stderr.readline, b"")
    for line in lines_iterator:
        print(">" + line) # or match and parse it...

execute(["memtier_benchmark", "--hide-histogram", "--test-time=60"]) # add relevant switches here
