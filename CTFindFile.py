#python script to search for a file
#inputs are:
# 1 - Start search location
# 2 - File name

import sys
import os
from os import system
		
def run(Path, filename):
	import time
	startTime = time.time()
	startDir = os.getcwd()
	if "\\\\\\\\" in Path: # passed in VS args do this.
		Path = Path.replace("\\\\\\\\", "\\\\")
	os.chdir(Path)
	cmd1 = "dir "
	cmd2 = " /S /B "
	filename = ' \"'+filename+'\"'
	system(" ".join([cmd1 + filename + cmd2]))
	elapsedTime = time.time() - startTime
	m, s = divmod(elapsedTime, 60)
	h, m = divmod(m, 60)
	print("Time to Run Command: %02d:Hrs, %02d:Mins, %02d:Secs" % (h, m, s))
	os.chdir(startDir)

def main():
	if len(sys.argv) == 3:
		run(sys.argv[1], sys.argv[2])
		sys.exit()
	else:
		print("\n\n#######\nArguments improperly formatted!!!")
if __name__ == "__main__":
	main()
