import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support Tolls\033[1;37m")
    os.system('git pull')
    try:os.system('mkdir /sdcard/4MBF-DATA')
    except:pass
    try:os.system('mkdir /sdcard/4MBF-DATA/OK')
    except:pass
    try:os.system('mkdir /sdcard/4MBF-DATA/CP')
    except:pass
    try:os.system('mkdir /sdcard/4MBF-DATA/TAP-A2F')
    except:pass
    try:os.system('touch .prox.txt')
        from KING import Subscription
        Subscription()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
