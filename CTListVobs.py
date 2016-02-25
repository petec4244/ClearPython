#List vobs active on the current host
#For Determining Paths applicable to use
#Pass in lsvob as root command
#typeOut = -short names or -long
#-short restricts output to VOB-tags only
#-long expands the listing to include all information stored in the Vob
import sys
import CTools as CT

def run(typeOut):
	cmd = 'lsvob ' + str(typeOut)
	vobList = CT.runCT(cmd)
	return vobList

def main():
	if len(sys.argv) == 2:
		listed = run(sys.argv[1])
		print(listed)
	else:
		print("Arguments improperly formatted, 1 arguments expected\n\n1:type of output\noutputs are:\n-short\nor\n-long")
if __name__ == "__main__":
	main()
