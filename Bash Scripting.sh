# this activates the shell script
#!/bin/bash

# this uninstalls all unused dependencies
sudo apt-get --purge autoremove packagename

# this updates the software database
sudo softwareupdate -i -a

# this updates the entire system
sudo chmod +x /usr/local/bin/update.sh