import os
import sys
import shutil, errno

ssdDrive = 'c:'
hddDrive = 'd:'
hddRootFolder = hddDrive+'\\ssd-hdd'


def mirrorOnHDD(drive, tail):
	origin = drive + tail
	dest = hddRootFolder + '\\' + drive.replace(':','-drive').lower() + tail;
	
	if os.path.exists(dest) :
		print('mirror folder already exists...')
		print('see ' + dest)
		return 
	print('move ' +origin + ' to ' + dest)
	print('copy to hdd...')

	try:
		shutil.copytree(origin, dest)
	except OSError as exc: # python >2.5
		if exc.errno == errno.ENOTDIR:
			shutil.copy(origin, dest)
		else:
			print('Directory not copied. Error: %s' % e)
			raise
			
	print('ok')
	
	print('remove original...')
	shutil.rmtree(origin)
	print('ok')
	
	print('make the junction')
	cmd = 'mklink /J "' + origin + '" "' + dest + '"'
	print(cmd)
	os.system(cmd)
	print('ok')
	
	print('done!')
	
	
	
def handlePath(p):
	print('handle '+p)
	absPath = os.path.abspath(p)
	if not os.path.isdir(absPath) :
		print('This is not a directory. Bye.')
		return
	(drive,tail) = os.path.splitdrive(absPath)
	if drive.lower() == ssdDrive :
		print('this is an ssd folder')
		mirrorOnHDD(drive, tail)
	else:
		print('this is an hdd folder')
	

if __name__ == "__main__":
	len(sys.argv)
	for arg in sys.argv:
		print(arg)
	for arg in sys.argv[1:] :
		print(arg)
		handlePath(arg)
	print("done")
	os.system("pause")
	