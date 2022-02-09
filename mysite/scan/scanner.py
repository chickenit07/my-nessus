from metasploit.msfrpc import MsfRpcClient
from metasploit.msfconsole import MsfRpcConsole
import simplejson as json

from .config import password
import os.path
import time

BASE = os.path.dirname(os.path.abspath(__file__))
vuln_list = []
sigdata=[]

def read_console(console_data):
    # print('read_console')
    global global_console_status
    global_console_status = console_data['busy']

    # print(global_console_status)
    if '[+]' in console_data['data']:
        
        sigdata = console_data['data'].rstrip().split('\n')

        for line in sigdata:
            if '[+]' in line:
                vuln_list.append(line)
    
def scan_template(console, ip_addr, modules):
    # print('scan_template')
    console.execute('use ' + modules)
    console.execute('set RHOSTS ' + ip_addr)
    console.execute('run')
    time.sleep(5)

def main(ip_addr):
    msfrpc_pass = password

    client = MsfRpcClient(msfrpc_pass)
    # cb - callback function, executes when data arrives to console
    console = MsfRpcConsole(client, cb=read_console)

    # read modules file then start scan 
    file = open(os.path.join(BASE, "modules.txt"))
    modules = file.readlines()
    
    count = 0
    for module in modules:
        count += 1
        print("Loading " + "{0:.0f}%".format(count/len(modules)*100))
        scan_template(console, ip_addr, module)
        while global_console_status:
            time.sleep(3)   
        # print(module)
    # print('vuln_list')
    # print(vuln_list)
    tmp = json.dumps(vuln_list)
    vuln_list.clear()
    return tmp

if __name__ == '__main__':
    main(sys.argv[1:])

# auxiliary/scanner/snmp/snmp_enumshares
# auxiliary/scanner/smb/smb_enumusers
# auxiliary/scanner/ssh/ssh_identify_pubkeys
# auxiliary/scanner/ssh/ssh_version
# auxiliary/scanner/http/mod_negotiation_scanner
# auxiliary/scanner/http/frontpage_credential_dump
# auxiliary/scanner/http/glassfish_traversal
# auxiliary/scanner/oracle/emc_sid
# auxiliary/scanner/oracle/sid_enum
# auxiliary/scanner/ftp/anonymous
# auxiliary/scanner/ftp/ftp_version
# auxiliary/scanner/http/dir_listing