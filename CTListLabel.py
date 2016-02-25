# This lists file and/or folder versions with a label.
# The inputs are:
# Type,  1: Files and Folders  2: Folders only (-d , directories)
# Label to use
# Path to begin 

import sys
import os
from os import sys
from os import system
import CTools as CT

def makeCmd(Type, Lbl1, Path):
	import time
	startTime = time.time()
	startDir = os.getcwd()
	if "\\\\\\\\" in Path:  # passed in VS args do this.
		Path = Path.replace("\\\\\\\\", "\\\\")
	os.chdir(Path)
	cmd = ''
	if Type == '1':
		cmd = 'find . -ver \"version('+Lbl1+')\" -print'
		print(cmd)
	if Type == '2':
		cmd = 'find . -type d -ver \"version('+Lbl1+')\" -print'
		print(cmd)
	if not cmd == '':
		print("The Command is - " + cmd+'\r\n')
		ApplyLbl(cmd)
		elapsedTime = time.time() - startTime
		m, s = divmod(elapsedTime, 60)
		h, m = divmod(m, 60)
		print("Time to Run Command: %02d:Hrs, %02d:Mins, %02d:Secs" % (h, m, s))
	os.chdir(startDir)

def ApplyLbl(command):
	part1 = 'cleartool '
	system(" ".join([part1 + command]))


def main():
	if len(sys.argv) == 4:
		command = sys.argv[1] +" "+ sys.argv[2]+" "+ sys.argv[3]
		print("The input Command is - " + command + '\r\n')
		makeCmd(sys.argv[1], sys.argv[2], sys.argv[3])
		sys.exit()
	if len(sys.argv) > 4:
		print("TOO MANY ARGUMENTS")
	else:
		print("Arguments improperly formatted")
if __name__ == "__main__":
	main()
