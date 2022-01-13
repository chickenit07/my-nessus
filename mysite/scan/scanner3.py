from metasploit.msfrpc import MsfRpcClient
from metasploit.msfconsole import MsfRpcConsole
import simplejson as json

from .config import password
import os.path

BASE = os.path.dirname(os.path.abspath(__file__))

global vuln_list
vuln_list = list()

def read_console(console_data):
    # print('read_console')
    if '[+]' in console_data['data']:
        global sigdata
        sigdata = console_data['data'].rstrip().split('\n')

        for line in sigdata:
            if '[+]' in line:
                vuln_list.append(line)
    # print(vuln_list)
#template to run msf command
def scan_template(console, ip_addr, modules):
    # print('scan_template')
    console.execute('use ' + modules)
    console.execute('set RHOSTS ' + ip_addr)
    console.execute('run')

def start_scan(ip_addr):
    # msfrpcd password. This password could be taken when starting msfrpcd daemon by this command: 
    # msfrpcd -P password -n -f -a 127.0.0.1
    msfrpc_pass = password

    client = MsfRpcClient(msfrpc_pass)
    console = MsfRpcConsole(client, cb=read_console)

    # read modules file then start scan 
    file = open(os.path.join(BASE, "modules.txt"))
    modules = file.readlines()
    
    count = 1
    for module in modules:
        count += 1
        scan_template(console, ip_addr, module)
        # print(module)
    print('vuln_list')
    print(vuln_list)
    return json.dumps(vuln_list)
    # print("done")
#debug    
# start_scan("10.10.39.235")

