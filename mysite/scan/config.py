from metasploit.msfrpc import MsfRpcClient
from metasploit.msfconsole import MsfRpcConsole
import os

# global global_positive_out
# global_positive_out = list()
# global global_console_status
# global_console_status = False

msfrpc_pass = 'password'

# sigdata = 0

def read_console(console_data):
    print(console_data)
    if '[+]' in console_data['data']:
        sigdata = console_data['data'].rstrip().split('\n')
        print(sigdata)
	

client = MsfRpcClient(msfrpc_pass)

console = MsfRpcConsole(client, cb=read_console)

console.execute('use auxiliary/scanner/smb/smb_ms17_010')
console.execute('set RHOSTS 10.10.99.11')
console.execute('set THREADS 20')
console.execute('run')

# os.system("py3clean .")
# while global_console_status:
#     print('global_console_status: ' + str(global_console_status))
#     time.sleep(5)
# time.sleep(5)

# targets = list()
# for line in global_positive_out:
#     if 'FreeFloat' in line:
#     	ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)[0]
# 	targets.append(ip)



# exploit = client.modules.use('auxiliary', 'scanner/smb/smb_ms17_010')
# exploit['RHOSTS'] = '10.10.99.11'
# exploit['RPORT'] = 445

# print(exploit.execute())

# alo = client
# print(dir(alo))
# print(alo)


