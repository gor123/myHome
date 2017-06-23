import os
tt=os.system('ls')
print(tt)
listfile_name = 'd:/to_be_backup/temp_2016.txt'
print ("hello")
f = open(listfile_name, 'r')
data = f.readlines()
for filen in data:
	print(filen)
