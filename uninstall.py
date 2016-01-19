import winreg
import os

def delKeyIgnoreInexistant(key):
	try:
		winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, key)
	except:
		pass

delKeyIgnoreInexistant('Directory\\shell\\ssd-hdd\\command')
delKeyIgnoreInexistant('Directory\\shell\\ssd-hdd')

print('ssd-hdd uninstalled successfully.')

os.system("pause")
