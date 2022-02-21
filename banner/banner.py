#!/usr/bind/env python
#_*_ coding: utf8 _*_

import os
from termcolor import colored
from pyfiglet import figlet_format

#COLORS
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'


def bannerMenu():
	os.system('clear')
    # NO CHANGE THE NAME, N00B
	print("""
\033[0;32m	  NO!                          MNO!
\033[0;32m     MNO!!       [\033[1;37mR3LI4NT\033[0m\033[0;32m]        MNNOO!
\033[0;32m   MMNO!                           MNNOO!!
\033[0;32m MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!!
\033[0;32m !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO!
\033[0;32m       ! MMMMMMMMMMMMMPPPPOOOOIII! !
\033[0;32m        MMMMMMMMMMMMPPPPPOOOOOOII!!       \033[0;32m╔═══════════════════════════════════╗\033[0m
\033[0;32m        MMMMMOOOOOOPPPPPPPPOOOOMII!       \033[0;32m║              \033[1;37mOPTIONS\033[0m\033[0;32m              ║\033[0m
\033[0;32m        MMMMM..    OPPMMP    .,OMI!       \033[0;32m║═══════════════════════════════════║ \033[0m
\033[0;32m        MMMM::   o.,OPMP,.o   ::I!!       \033[0;32m║ -m/--menu   :  Option menu        ║\033[0m
\033[0;32m          NNM:::.,,OOPM!P,.::::!!         \033[0;32m║                                   ║\033[0m
\033[0;32m         MMNNNNNOOOOPMO!!IIPPO!!O!        \033[0;32m║ -r/--range  :  Scan hosts         ║\033[0m
\033[0;32m         MMMMMNNNNOO:!!:!!IPPPPOO!        \033[0;32m║                                   ║\033[0m 
\033[0;32m          MMMMMNNOOMMNNIIIPPPOO!!         \033[0;32m║ -t/--target :  Target to spoof    ║\033[0m
\033[0;32m             MMMONNMMNNNIIIOO!            \033[0;32m║                                   ║\033[0m                                   
\033[0;32m           MN MOMMMNNNIIIIIO! OO          \033[0;32m║ -s/spoofed  :  IP router          ║\033[0m   
\033[0;32m          MNO! IiiiiiiiiiiiI OOOO         \033[0;32m║                                   ║\033[0m                               
\033[0;32m     NNN.MNO!   O!!!!!!!!!O   OONO NO!    \033[0;32m║ -syn/--synflood : Synflood Attack ║\033[0m
\033[0;32m    MNNNNNO!    OOOOOOOOOOO    MMNNON!    \033[0;32m║                                   ║\033[0m
\033[0;32m      MNNNNO!    PPPPPPPPP    MMNON!      \033[0;32m║ -i/--interface : FTP sniff        ║\033[0m
\033[0;32m         OO!                   ON!\033[0m        \033[0;32m╚═══════════════════════════════════╝\033[0m

\033[1;37m /\033[0;32m$$$$$$$   \033[1;37m/\033[0;32m$$$$$$  \033[1;37m/\033[0;32m$$$$$$  \033[1;37m/\033[0;32m$$$$$$   \033[1;37m/\033[0;32m$$$$$$  \033[1;37m/\033[0;32m$$   \033[1;37m/\033[0;32m$$
\033[1;37m| \033[0;32m$$\033[1;37m\033[1;37m__  \033[0;32m$$ \033[1;37m/\033[0;32m$$\033[1;37m__  \033[0;32m$$\033[1;37m|_  \033[0;32m$$\033[1;37m_/ /\033[0;32m$$\033[1;37m__  \033[0;32m$$ \033[1;37m/\033[0;32m$$\033[1;37m__  \033[0;32m$$\033[1;37m| \033[0;32m$$$ \033[1;37m| \033[0;32m$$
\033[1;37m| \033[0;32m$$  \033[1;37m\ \033[0;32m$$\033[1;37m| \033[0;32m$$  \033[1;37m\ \033[0;32m$$  \033[1;37m| \033[0;32m$$  \033[1;37m| \033[0;32m$$  \033[1;37m\__/| \033[0;32m$$  \033[1;37m\ \033[0;32m$$\033[1;37m| \033[0;32m$$$$\033[1;37m| \033[0;32m$$
\033[1;37m| \033[0;32m$$$$$$$\033[1;37m/| \033[0;32m$$  \033[1;37m| \033[0;32m$$  \033[1;37m| \033[0;32m$$  \033[1;37m|  \033[0;32m$$$$$$ \033[1;37m| \033[0;32m$$  \033[1;37m| \033[0;32m$$\033[1;37m| \033[0;32m$$ $$ $$
\033[1;37m| \033[0;32m$$\033[1;37m____/ | \033[0;32m$$  \033[1;37m| \033[0;32m$$  \033[1;37m| \033[0;32m$$   \033[1;37m\____  \033[0;32m$$\033[1;37m| \033[0;32m$$  \033[1;37m| \033[0;32m$$\033[1;37m| \033[0;32m$$  $$$$
\033[1;37m| \033[0;32m$$      \033[1;37m| \033[0;32m$$  \033[1;37m| \033[0;32m$$  \033[1;37m| \033[0;32m$$   \033[1;37m/\033[0;32m$$  \033[1;37m\ \033[0;32m$$\033[1;37m| \033[0;32m$$  \033[1;37m| \033[0;32m$$\033[1;37m| \033[0;32m$$\033[1;37m\  \033[0;32m$$$
\033[1;37m| \033[0;32m$$      \033[1;37m|  \033[0;32m$$$$$$\033[1;37m/ /\033[0;32m$$$$$$\033[1;37m|  \033[0;32m$$$$$$\033[1;37m/|  \033[0;32m$$$$$$\033[1;37m/| \033[0;32m$$ \033[1;37m\  \033[0;32m$$
\033[1;37m|__/       \______/ |______/ \______/  \______/ |__/  \__/                                                
	""")

def error():
    print("""\033[0;31m
                       ______
                    .-"      "-.
                   /            \ 
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <\033[0m
     \033[0;31m(_/\033[0m      \033[1;31m[ERROR] \033[0;31minvalid parameter\033[0m     \033[0;31m\_)\033[0m
    """)

def scanH():
    os.system('clear')
    banner = print((colored(figlet_format("Scan-Hosts"))))

def spoofing():
    os.system('clear')
    banner = print((colored(figlet_format("Spoofing"))))

def synflood_banner():
    os.system('clear')
    banner = print((colored(figlet_format("Synflood"))))

def ftp_sniff():
    os.system('clear')
    banner = print((colored(figlet_format("FTP-Sniffing"))))

             	