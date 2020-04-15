import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  termux-advance-button ')
print(a+'\t  UP,Down,right,Left, CTRL ')
print(b+'\t  By: Anonym')
print('\t Github : https://github.com/MuhamadFajarGaray')
print(a+'+'*40)
print('\nProcessing..')
sleep(1)
print(b+'\n[!] retrieve default files..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Adding advanced button..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Process  !')
sleep(1)
print(b+'\n[!] Wait a second')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Finished !!')
