#This Applies a label based on input values
#The arguments are:
#-1- Type of Label Application --- Arg[1] = Type definition
# - Defined Types -
#----------------- 1 Apply a Label to another label in Vob -- Arg[2] to Arg[3] in Vob Arg[4]  5
#----------------- 2 Apply a Label to A branch in Vob -- Arg[2] to Arg[3] in Vob arg[4]  5
#----------------- 3 Apply a Label to an entire view, -- Arg [2] to path to view arg[3] NOTE: Parm 3 i null, Param4 used
#----------------- 4 For use by other Scripts
#----------------- 5 Same as 1 except skip where it already exists.
#----------------- 6 Same as 2 except skip where it already exists.
import sys
import os
from os import sys
from os import system
import CTools as CT

def makeCmd(Type, Lbl1, BrLbl2, Path):
	import time
	startTime = time.time()
	startDir = os.getcwd()
	if "\\\\\\\\" in Path:
		Path = Path.replace("\\\\\\\\", "\\\\")
	#print('STARTDIR = '+startDir+'\r\n')  #XXX debug
	os.chdir(Path)
	#print('ENDDIR = '+os.getcwd()+'\r\n') #XXX debug
	cmd = ''
	if Type == '1':
		cmd = 'find . -ver \"version('+BrLbl2+')\" -exec \"cleartool mklabel -rep '+Lbl1+' \"%CLEARCASE_XPN%\"\"'
		print(cmd)
	if Type == '2':
		cmd = 'find . -ver \"version(.../'+BrLbl2+'/LATEST)\" -exec \"cleartool mklabel -rep '+Lbl1+' \"%CLEARCASE_XPN%\"\"'
		print(cmd)	
	if Type == '3': 
		cmd = 'find . -cview -exec \"cleartool mklabel -rep '+Lbl1+" \"%CLEARCASE_XPN%\""
		print(cmd)
	if Type == '4':
		cmd = 'mklabel -rep '+Lbl1+' '+BrLbl2
		print(cmd)
	if Type == '5':
		cmd = 'find . -ver \"version('+BrLbl2+') && !version('+Lbl1+')\" -exec \"cleartool mklabel -rep '+Lbl1+' \"%CLEARCASE_XPN%\"\"'
		print(cmd)
	if Type == '6':
		cmd = 'find . -ver \"version(.../'+BrLbl2+'/LATEST) && !version('+Lbl1+')\" -exec \"cleartool mklabel -rep '+Lbl1+' \"%CLEARCASE_XPN%\"\"'
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
		makeCmd(sys.argv[1], sys.argv[2], '0', sys.argv[3])
	if len(sys.argv) == 5:
		command = sys.argv[1] +" "+ sys.argv[2]+" "+ sys.argv[3]+" "+ sys.argv[4]
		print("The input Command is - " + command+ '\r\n')
		makeCmd(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	else:
		print("Arguments improperly formatted")
if __name__ == "__main__":
	main()
