#python script to find all elements
#inputs are:
# 1 - Start search location
# 2 - Label 1

import sys
import os
from os import system
		
def run(Path, Label1, type):
	import time
	startTime = time.time()
	startDir = os.getcwd()
	if "\\\\\\\\" in Path: # passed in VS args do this.
		Path = Path.replace("\\\\\\\\", "\\\\")
	os.chdir(Path)
	cmd1 = "cleartool find . "
	if type == '0':
		cmd1 = cmd1 + "-ver \"version"
	if type == '1':
		cmd1 = cmd1 + "-elem \"brtype"
	if type == '2':
		cmd1 = cmd1 + "-elem \"lbtype"
	cmd2 = "("+Label1+")\" -print"
	print("Command is: " +cmd1+cmd2)
	system(" ".join([cmd1 + cmd2]))
	print("Searched for: " +Label1)
	elapsedTime = time.time() - startTime
	m, s = divmod(elapsedTime, 60)
	h, m = divmod(m, 60)
	print("Time to Run Command: %02d:Hrs, %02d:Mins, %02d:Secs" % (h, m, s))
	os.chdir(startDir)

def main():
	print(sys.argv)
	if len(sys.argv) == 4:
		run(sys.argv[1], sys.argv[2], sys.argv[3])
		sys.exit()
	else:
		print("\n\n#######\nArguments improperly formatted!!!")
if __name__ == "__main__":
	main()
