import os
tt=os.system('ls')
print(tt)
listfile_name = 'd:/to_be_backup/temp_2016.txt'
prefix = 'd:/to_be_backup/2016/'
print ("helloddd")
f = open(listfile_name, 'r')
data = f.readlines()
for filen in data:
	gg=filen.rstrip('\n')
	full_path=prefix+gg
	print([full_path])
	cmd = "cp "+full_path+" ."
	print([cmd])
	os.system(cmd)

