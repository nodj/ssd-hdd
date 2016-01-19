import winreg
import os
import sys

pythonPath  = sys.executable
thisPath    = os.path.realpath(__file__)
installPath = os.path.dirname(thisPath)
scriptPath  = installPath + "\\ssd-hdd.py"
iconPath    = installPath+'\\icon.ico'
cmd         = '"' + pythonPath + '" ' + scriptPath + ' "%1"'
menuTitle   = 'ssd -> hdd'

key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\shell\\ssd-hdd')
winreg.SetValueEx(key, '',0, winreg.REG_SZ, menuTitle)
winreg.SetValueEx(key, 'Icon',0, winreg.REG_SZ, iconPath)
winreg.SetValue(key, 'command', winreg.REG_SZ, cmd)

print('Done. ssd-hdd installed with the following parameters:')
print(' -> Python executable: ' + pythonPath)
print(' -> Script executable: ' + scriptPath)
print(' ')
print('If one of those changes, please launch this installer again.')

os.system("pause")
