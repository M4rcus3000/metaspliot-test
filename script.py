import subprocess
import ipaddress
import os
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
           return 0
       elif (confirmT == "no" or confirmT == "n" or confirmT == "N"):
           ip_new = input("Enter manually your target's IP:\n")
           if (loop(ip_new)):
               return ip_new
       else:
           continue

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
            nmapScan(network)