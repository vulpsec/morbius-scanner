#!/usr/bin/env python3
#*- coding: utf-8 -*--
#Coded by Morbius.os

AUTHOR = 'Morbius.os'
GİTHUB = 'https://github.com/morbius-os'
INSTAGRAM= '@morbius.os'


import time
import os
try:
    import json
except:
    os.system('pip install json')
try:
    import requests
except:
    os.system('pip install requests')


PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'#


def banner():
    print("""{}{}
          ,,,,,,                                                                                                        
          ||((||``,,..                                                                                                  
          ||((//((//||``,,                                                                                              
          ||((||||||////////``..                                  ,,                                                    
          ||//;;;;;;////||//////;;``..                          ..``                                                    
          ||//;;;;;;//||;;||||////||;;````,,                    ``;;``..                                                
          ||//;;;;;;//||;;;;;;||//////||||||;;``..        ..``;;//((((||````..  ``````..                                
        ..||//;;;;;;//||;;;;;;||//||;;||||(({{//``,,....,,``((++++++==++++((;;``////||``..                              
        ..//((||||||//||;;;;;;||//||;;;;;;||;;||//((//;;((++====++++==++++====++++{{((||``                              
        ..||((////////||;;;;;;||//||;;;;;;||````||((++========++{{{{{{{{++========++((||``..                            
        ,,||//||||||((((||||;;||//;;````;;||;;||//((++==========++++++++======++++{{((||;;``                            
        ,,||//;;;;||//////////||//;;;;||//((////(((((({{{{++++==========++++++{{{{{{((||;;``                            
        ``||//;;;;||//||||||||||//||//{{{{++{{{{(((({{(((({{{{++++++++++++{{{{{{{{{{((//;;``                            
        ``||//;;;;||//||;;````;;////{{++====++++{{{{{{{{(((((((({{{{{{{{++++++{{{{{{{{//;;``                            
        ``||//;;;;||||;;````````||{{++==========++{{{{++{{(((((((((({{{{++++{{{{{{{{{{//``,,                            
        ``////;;;;;;||``````````//++==============++{{{{++{{(((((((({{++{{//||(({{++++||,,                              
        ..||((((||``;;``````````((==%%==++++++====++++(({{++(((((((({{{{{{//;;||||//((((((||,,                          
          ..``;;//////;;````````((%%%%++++{{++======++{{((++((//(((({{{{{{//;;;;;;////||||//////``,,..                  
              ..````;;;;||||;;;;((%%%%++++++====++++++++(({{//||//(({{{{{{//;;;;;;//||||||||//((//||;;``,,..            
                    ..````;;;;//{{%%==++++==++++++++++++{{{{//||||(({{{{{{//;;;;;;//||;;;;;;||((//////||||;;``,,        
                          ..``||//++==++++++++{{{{++++==++{{//||||//{{{{{{//;;;;;;//||;;;;;;||((||;;;;||//((//;;``..    
                                ``//==%%++{{{{++++======++((||;;||//(({{{{//||||||//||;;;;;;||//||;;;;;;||;;;;||//||,,  
                                ``//++==================++((||;;||//////((////////((||;;;;;;||//||;;;;``;;``````;;||``  
                          ..``||||||++&&&&&&============++{{//;;;;||;;||////||||||((((//||;;||//;;``````;;``````;;||``  
                          ,,;;||``;;((==%%%%==++++++====++{{//;;;;;;;;||//||;;;;;;((////////////;;``````;;``````;;||``  
                          ..``,,,,,,;;{{%%%%%%==++++====++{{//;;;;``````||||;;;;;;//||||||||||||;;;;````;;``````;;||``  
                                    ,,||==&&&&&&%%========{{||````,,  ``||||;;;;;;//||;;````;;||;;;;;;;;||;;````;;||,,  
                                      ``((&&######&&&&%%%%((``..      ,,||||;;;;;;//;;``````;;;;``````||//||````||||..  
                                      ..``{{&&########&&==||,,        ,,||//||;;;;//````````;;``````````;;||;;;;////..  
                                          ``((%%&&####%%((``          ..;;(({{//``||````````;;``````````;;``````||//..  
                                            ,,||((++{{//``..            ..,,``||//((||``````;;``````````;;``````||||..  
                                              ..``````,,..                    ,,``;;;;;;||||||``````````;;``````||||..  
                                                                                  ..,,````;;////;;``````;;``````||//    
                                                                                          ..``//||;;;;;;||``````||//    
                                                                                                ``;;||||//;;````||//    
                                                                                                    ..``;;//((||((//    
                                                                                                          ..,,;;((//    
                                                                                                              ..,,,,    
                                                                                                    
{}                                                                
Author: {}
Instagram: {}
Github: {}    
   {}""".format(BOLD,CYAN,GREEN,AUTHOR,INSTAGRAM,GİTHUB,END) )

while True:
    os.system('clear')
    banner()
    print ("1) Tools     2)M-DoS ")
    print (" ")

    answer = int(input('''
{}┌──({}root㉿m-finder{})-[{}MainMenu{}]
└─{}# {}select '''.format(BLUE,RED,BLUE,END,BLUE,RED,END)))
    
    if answer == 1:
          os.system('clear')
          print(f"""{GREEN}{BOLD}
+----------------------------------------------------+
   _______          _       __  __                  
  |__   __|        | |     |  \/  |                 
     | | ___   ___ | |___  | \  / | ___ _ __  _   _ 
     | |/ _ \ / _ \| / __| | |\/| |/ _ \ '_ \| | | |
     | | (_) | (_) | \__ \ | |  | |  __/ | | | |_| |
     |_|\___/ \___/|_|___/ |_|  |_|\___|_| |_|\__,_|
     
+----------------------------------------------------+
Author: {AUTHOR}
Instagram: {INSTAGRAM}
Github: {GİTHUB}
 
{RED}{BOLD}[00] {END}Port Scan
{RED}{BOLD}[01] {END}IP Scan
{RED}{BOLD}[02] {END}Web Site Scan
{RED}{BOLD}[03] {END}Nmap Scan
{RED}{BOLD}[04] {END}IP İnfo (m-location)
{RED}{BOLD}[05] {END}Firewall Scan
{RED}{BOLD}[06] {END}Whois Scan
{RED}{BOLD}[07] {END}Netdiscover

{RED}[99] EXİT
""")

          select = int(input('''
{}┌──({}root㉿m-scan{})-[{}ToolMenu{}]
└─{}# {}select '''.format(BLUE,RED,BLUE,END,BLUE,RED,END)))

          if select == 0 or select == 00:
            ip_or_web = input('''
{}┌──({}root㉿m-scan{})-[{}ToolMenu{}]
└─{}# {}nmap '''.format(BLUE,RED,BLUE,END,BLUE,RED,END))

            if ip_or_web == 'q':
                break
            os.system('clear')
            os.system('sudo nmap ' + ip_or_web + ' -P' )
            time.sleep(10)
            os.system('clear')
            break


          elif select == 1 or select == 01:
            IP = input('''
{}┌──({}root㉿m-scan{})-[{}menu{}]
└─{}# {}nmap '''.format(BLUE,RED,BLUE,END,BLUE,RED,END))

            if IP == 'q':
                break
            os.system('clear')
            os.system('sudo nmap ' + IP + ' -vv')
            time.sleep(10)
            break


          elif select == 2 or select == 02:
            webSite = input('''
{}┌──({}root㉿m-scan{})-[{}menu{}]
└─{}# {}nmap '''.format(BLUE,RED,BLUE,END,BLUE,RED,END))

            if webSite == 'q':
                break
            os.system('clear')
            os.system('sudo nmap ' + webSite + ' -vv')
            time.sleep(10)
            
            
          elif select == 3 or select == 03:
               scanner = input('''
{}┌──({}root㉿m-scan{})-[{}menu{}]
└─{}# {}nmap  '''.format(BLUE,RED,BLUE,END,BLUE,RED,END))
               os.system('clear')
               os.system(f'nmap {scanner}')
               time.sleep(10)
               
          elif select== 4 or select == 04 :
               os.system('git clone https://github.com/morbius-os/m-ip-to-location')
               os.system('cd morbius_scanner')
               os.system('python3 m-scan-v4.py')
               
          elif select == 5 or select == 05:
              target=input('''
{}┌──({}root㉿m-scan{})-[{}ToolMenu{}]
└─{}# {}wafw00f --target '''.format(BLUE,RED,BLUE,END,BLUE,RED,END))
              os.system('wafw00f {}'.format(target))
              time.sleep(10)
              if target == 'q':
                break

          if select == 6 or select == 06:
              target=input('''
{}┌──({}root㉿m-scan{})-[{}ToolMenu{}]
└─{}# {}whois --target '''.format(BLUE,RED,BLUE,END,BLUE,RED,END))
              
              os.system('whois {}'.format(target))
              time.sleep(10)
              
          if select == 7 or select ==select == 07:
              os.system('netdiscover')
              time.sleep(10)

    elif answer == 2:
        print(""""Morbius Dos İndiriliyor...""")
        os.system('git clone https://github.com/morbius-os/m-dos')
        os.system('cd m-dos')
        os.system('python3 m-dos.py')