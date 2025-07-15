import os


os.chdir('/home/rajs11')
try:
    os.system('rm -r Backup')
except Exception as e:
    print(e)


try:
    os.mkdir('/home/rajs11/Backup')
    print("Dir created")
except Exception as e:
    print(e)

try:
    os.mkdir('/home/rajs11/zipDir')
    os.mkdir('/home/rajs11/zipDir/zipFinal')
except Exception as e: 
    print(e)    
os.system('cp -r /home/rajs11/Books /home/rajs11/zipDir/zipFinal')

os.chdir('/home/rajs11/zipDir')
os.system('zip -r zipFinal.zip zipFinal')
# os.system('rm -r zipFinal')
os.system('cp zipFinal.zip /home/rajs11/Backup')