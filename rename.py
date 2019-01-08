import os

target = int(input("How many characters to remove from front?"))
i = 1
for file in sorted(os.listdir()):
    if ".mp4" in file:
        if i < 10:
            os.rename(file, "0" + str(i) + " " + file[target:])
        else:
            os.rename(file, str(i) + " " + file[target:])
        i += 1 
