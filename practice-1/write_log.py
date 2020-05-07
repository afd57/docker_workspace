import os

with open("test.txt",'w') as file:
    for key, val in os.environ.items():
        print(f"{key}: {val}")
        file.write(f"{key}: {val}\n")
