#Maintaining software on Linux

#Updating VLC Media Player
#If you want to install a software up your linux OS, the first command to run
#is this and if you gonna update a software he version that's installed is out-of-date. 
#You'll fix that now by updating it to the newest version.
#To do that, force an update of the package manager, using this command:
sudo apt-get install -f #remind enter "Y"
#To verify an previous installation or updates runs the follow command:
dpkg -s *softwareName*
#----------
#Installing a new software, previous run the first command
#To make sure these repositories are up-to-date and all dependencies are fixed,
#run this command in the terminal (you will have to enter the letter "Y" at some point
#during the process to confirm your action):
sudo apt-get update
#Now you're ready to install new software. Run the command below in the terminal:
sudo apt-get install *NewSfotware*#remind enter "Y"
#To verify an previous installation or updates runs the follow command:
dpkg -s *softwareName*
#---------------
#Uninstalling a Software
sudo apt-get remove *Software*