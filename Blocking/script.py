import os
from time import sleep


os.system('start cmd /k "cd /d %cd% & python registryServer.py"')
sleep(3)
os.system('start cmd /k "cd /d %cd% & python server.py s1 8000"')
os.system('start cmd /k "cd /d %cd% & python server.py s2 8001"')
sleep(3)

command='start cmd /k "cd /d %cd% & python client.py'
command+=' 1 1 "test1" "Hello world" "uuid1"'
command+=' 1 2 "test2" "Hello world by yash" "uuid2"'
command+=' 2 1 "uuid2"'
command+=' 3 1 "uuid2"'
command+=' 2 2 "uuid2"'
command+=' 1 1 "test2" "Hello world" "uuid2" 4"'


os.system(command)

