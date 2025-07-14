import os 

dirname = "./Task3/Logs"

try :
    os.mkdir(dirname)
    print("Directory created")
except Exception as e:
    print(f"Exception occured : {e}")


print(os.getcwd())
os.chdir(dirname) 

for i in range(7):
    
    with open(f"file{i+1}","w") as file:
        file.write(f"Hello from log{i+1}")
        filename = f"file{i+1}"
    os.rename(filename,f"file{i+1}.txt")
    with open(f"file{i+1}.txt",'r') as file:
        print(file.read())
