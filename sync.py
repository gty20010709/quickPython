import sys
import os
import time

content = time.ctime()
input_list = sys.argv
cur_work_path = os.getcwd()

if input_list[1] == 'push':
	os.system('cd {path} && git add . && git commit -m "{commit}" && git push'.format(path=cur_work_path,commit=content))
elif input_list[1] == 'pull':
	os.system('cd {path} && git pull'.format(cur_work_path))
else:
	pass
if os.name == 'nt':
	os.system('pause')
elif os.name == 'posix':
	os.system('read -p "Press any key to continue..."')



# print(sys.argv) 
