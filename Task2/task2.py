for i in range(1,6):
    with open(f"./Task2/file{i}.txt",'w') as file:
        file.write(f"Hello from file{i}")
    with open(f"./Task2/file{i}.txt",'r') as file:
        print(file.read())
