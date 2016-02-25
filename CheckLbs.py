#This Uses Cleartool to compare a label vs Latest
# Or A label vs A label.
# Or 
#1.Call path to execute
#2.Label
#3.Branch or 2nd label
#4.Verbose output?
#5.Find or Compare?
# find, finds all instances of a vob object
#Compare finds all instances of an object that are not the same element as another object.
#Ie all items with one label without another, or all items of one branch that dont have one label.

import sys
import CTools as CT

def triage(path, command1, command2, output, method):
    cwd = os.getcwd()
    if cwd.endswith(path):
        if output == '0':
            run(command1, command2, False, method)
        if output == '1':
            run(command1, command2, True, method)
    else: 
        #change to path #May need work.
        os.chdir(path)

def run(command1, command2, output, method):
    #debug
    print(os.getcwd)
    comparison = ['']
    Cpart1 = 'Find . -ver "version('
    Cpart2 = ') && !version('
    Cpart3 = ')" -print'
    if method == 'Compare':
        cmdOut = '%s%s%s%s%s' % Cpart1, command1, Cpart2, command2, Cpart3
    if method == 'Find':
        cmdOut = '%s%s%s' % Cpart1, command1, Cpart3
    comparison = CT.triage(cmdOut, output)


def main():
    if len(sys.argv) == 5:
        triage(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
if __name__ == "__main__":
    main()
