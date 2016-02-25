#Lock an Element
#input 1: -c or -nc "comment if applicable"
#input 2: \vob where you want the label created
import sys
import CTools as CT

#Userlist = list of users to lock
#typeLock = Label or branch type to lock
#Vob = where to lock 
def run(userList, typeLock, Vob):
	cmd = 'lock -nuser ' + str(userList)+ " " + typeLock +'@vob:'+Vob
	vobList = [CT.runCT(cmd)]  
	return vobList

def main(): 
	if len(sys.argv) >= 3 and len(sys.argv) <=4:
		if len(sys.argv) ==4:
			command = sys.argv[1] +" "
			typelock = sys.argv[2]
			vob = sys.argv[3]
		listed = run(command, typelock, vob)
		#print(listed)
	else:
		print("Arguments improperly formatted, 2 arguments expected\n\n1:-c/-nc \"comment if applicable\" Branch\n2:\\VobName")
		print("\nIE: -c \"This is a Branch comment\" MY_NEW_branch \SAMPLEVOB\n\tThis will create MY_NEW_LABEL with " +
			  "Comment \"This is a Branch comment\" in the SAMPLEVOB" )
if __name__ == "__main__":
	main()

