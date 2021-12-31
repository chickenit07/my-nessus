from metasploit.msfrpc import MsfRpcClient
from metasploit.msfconsole import MsfRpcConsole
import os
from .config import password

def read_console(console_data):
    global console_status
    console_status = console_data['busy']
    # print(console_status)
    # print(console_data)
    if '[+]' in console_data['data']:
        global sigdata
        sigdata = console_data['data'].rstrip().split('\n')
        for line in sigdata:
            if '[+]' in line:
                print(line)
                vuln_list.append(line)

#template to run msf command
def scan_template(console, ip_addr, modules):
    console.execute('use ' + modules)
    console.execute('set RHOSTS ' + ip_addr)
    console.execute('run')

def start_scan(ip_addr):
    global vuln_list
    vuln_list = list()
    global console_status
    console_status = False 

    # msfrpcd password. This password could be taken when starting msfrpcd daemon by this command: 
    # msfrpcd -P password -n -f -a 127.0.0.1
    msfrpc_pass = password

    client = MsfRpcClient(msfrpc_pass)
    console = MsfRpcConsole(client, cb=read_console)

    # read modules file then start scan 
    file = open("modules.txt", "r")
    modules = file.readlines()

    count = 0
    for module in modules:
        count += 1
        # print(module)
        scan_template(console, ip_addr, module)
#debug    
# start_scan("10.10.39.235")