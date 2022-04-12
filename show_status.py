#!/usr/bin/python

# @desc     Tired of having to go into each sub dir to find out whether or
#           not you did a git commit? Tire no more, just use this!
#           - 2022.04.12 - updated for python 3.
#
# @author   Mike Pearce <mike@mikepearce.net>
# @since    18/05/2010

# Grab some libraries
import sys
import os
import glob
import subprocess
from optparse import OptionParser

# Setup some stuff
dirname = './'
gitted  = False
mini    = True

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

#-- END class bcolors --#

parser = OptionParser(description="\
Show Status is awesome. If you tell it a directory to look in, it'll scan \
through all the sub dirs looking for a .git directory. When it finds one \
it'll look to see if there are any changes and let you know. \
It can also push and pull to/from a remote location (like github.com) \
(but only if there are no changes.) \
Contact jonathan.morgan.007@gmail.com for any support.")
parser.add_option("-d", "--dir",
                    dest    = "dirname",
                    action  = "store",
                    help    = "The directory to parse sub dirs from",
                    default = os.path.abspath("./")+"/"
                    )

parser.add_option("-v", "--verbose",
                  action    = "store_true",
                  dest      = "verbose",
                  default   = False,
                  help      = "Show the full detail of git status"
                  )

parser.add_option("-r", "--remote",
                action      = "store",
                dest        = "remote",
                default     = "",
                help        = "Set the remote name (remotename:branchname)"
                )

parser.add_option("--push",
                action      = "store_true",
                dest        = "push",
                default     = False,
                help        = "Do a 'git push' if you've set a remote with -r it will push to there"
                )

parser.add_option("-p", "--pull",
                action      = "store_true",
                dest        = "pull",
                default     = False,
                help        = "Do a 'git pull' if you've set a remote with -r it will pull from there"
                )

# Now, parse the args
(options, args) = parser.parse_args()


#-------------------
def show_error(error="Undefined Error!"):
#-------------------
    """Writes an error to stderr"""
    sys.stderr.write(error)
    sys.exit(1)

#-- END function show_error() --#


#-------------------
# Now, onto the main event!
#-------------------
if __name__ == "__main__":
    os.system('clear')
    sys.stdout.write('-- Starting git status...\n')
    os.environ['LANGUAGE'] = 'en_US:en';
    os.environ['LANG'] = 'en_US.UTF-8';

    sys.stdout.write('Scanning sub directories of %s\n' %options.dirname)

    # See whats here
    for infile in glob.glob( os.path.join(options.dirname, '*') ):

        #is there a .git file
        if os.path.exists( os.path.join(infile, ".git") ):

            #Yay, we found one!
            gitted = True

            # OK, contains a .git file. Let's descend into it
            # and ask git for a status
            out = subprocess.getoutput('cd '+ infile + '; git status')

            # Mini?
            if False == options.verbose:

                j = out.find('On branch');
                k = out.find('\n', j);
                branch = out[j+10:k];
                branchColor = bcolors.WARNING;

                if branch == 'master':

                    branchColor = bcolors.OKGREEN

                #-- END - check if master branch --#

                branch = "[ " + branchColor + branch.ljust(15) + bcolors.ENDC + " ]"

                if -1 != out.find('nothing'):
                    result = bcolors.OKGREEN + "No Changes" + bcolors.ENDC

                    # Pull from the remote
                    if False != options.pull:

                        push = subprocess.getoutput(
                            'cd '+ infile +
                            '; git pull '+
                            ' '.join(options.remote.split(":"))
                        )
                        result = result + " (Pulled) \n" + push

                    #-- END check if we are to pull --#

                    # Push to the remote
                    if False != options.push:

                        push = subprocess.getoutput(
                            'cd '+ infile +
                            '; git push '+
                            ' '.join(options.remote.split(":"))
                        )
                        result = result + " (Pushed) \n" + push

                    #-- END check if we are to push. --#

                else:

                    result = bcolors.FAIL + "Changes" + bcolors.ENDC

                #-- END check if -1 != out.find('nothing'): - check if changes? --#

                # Write to screen
                sys.stdout.write( "-- " + bcolors.OKBLUE + infile.ljust(55) + bcolors.ENDC + branch + " : " + result +"\n")

            else:

                #Print some repo details
                sys.stdout.write("\n---------------- "+ infile +" -----------------\n")
                sys.stdout.write(out)
                sys.stdout.write("\n---------------- "+ infile +" -----------------\n")

            #-- END check if False == options.verbose: --#

            # Come out of the dir and into the next
            subprocess.getoutput('cd ../')

        #-- END check if ".git" folder (if it is a git repo) --#

    #-- END for loop over directories in work directory path. --#

    if ( False == gitted ):

        show_error("Error: None of those sub directories had a .git file.\n")

    #-- END check if "gitted" --#

    sys.stdout.write("Done\n")

#-- END if __name__ == "__main__": --#
