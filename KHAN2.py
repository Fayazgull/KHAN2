#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/3017062245271082/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf KHAN2.so KHAN2.so')
except:
    pass
os.system('rm -rf KHAN2.so KHAN2.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('KHAN2.so'):
        os.system('curl -L https://github.com/KHAN2-XD/executables/blob/main/KHAN2.cpython-311.so?raw=true -o KHAN2.so') 
        import KHAN2
    else:
        import KHAN2

elif bit == '32bit':
    if not os.path.isfile('KHAN2.so'):
        os.system('curl -L https://github.com/KHAN2-XD/executables/blob/main/KHAN2.cpython-311.so?raw=true -o KHAN2.so') 
        import KHAN2
    else:
        import KHAN2
