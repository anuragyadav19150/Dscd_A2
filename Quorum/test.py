import os
from time import sleep


os.system('start cmd /k "cd /d %cd% & python registryserver.py 3 2 2"')
sleep(3)
os.system('start cmd /k "cd /d %cd% & python server.py server1 9000')
sleep(3)
os.system('start cmd /k "cd /d %cd% & python server.py server2 9001')
sleep(3)
os.system('start cmd /k "cd /d %cd% & python server.py server2 9002')
sleep(3)
os.system('start cmd /k "cd /d %cd% & python client.py 1 uid1 file1 "Hello world!" 2 uid1 1 uid2 file2 "Hello worlds!" 3 uid2 4 1 uid1 file1000 "hiii" 1 uid1 file1 "Updated" 2 uid1 2 uid2 5"')
