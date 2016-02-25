#python script to compare 2 labels
#inputs are:
# 1 - Start search location
# 2 - Label 1
# 3 - Label 2

import sys
import os
from os import system
		
def run(Path, Label1, Label2):
	import time
	startTime = time.time()
	startDir = os.getcwd()
	if "\\\\\\\\" in Path: #this is coming from VS passed in arguments.
		Path = Path.replace("\\\\\\\\", "\\\\")
	os.chdir(Path)
	cmd1 = "cleartool find . -ver \"lbtype(" +Label1
	cmd2 = ") && !lbtype("+Label2+")\" -print"
	system(" ".join([cmd1 + cmd2]))
	print("Compared - " +Label1+ " To Label - "+Label2)
	elapsedTime = time.time() - startTime
	m, s = divmod(elapsedTime, 60)
	h, m = divmod(m, 60)
	print("Time to Run Command: %02d:Hrs, %02d:Mins, %02d:Secs" % (h, m, s))
	os.chdir(startDir)

def main():
	if len(sys.argv) == 4:
		run(sys.argv[1], sys.argv[2], sys.argv[3])
		sys.exit()
	else:
		print("\n\n#######\nArguments improperly formatted!!!")
if __name__ == "__main__":
	main()
