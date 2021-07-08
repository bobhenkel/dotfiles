#!/usr/bin/env bash

# if [ $(herbstclient list_monitors | grep 2: | cut -d' ' -f2 | cut -d'x' -f1) == 2900 ];
# then echo "21x9";
# else echo "16x9"
# fi
source .bash_profile #password is stored here
protonvpn_status=$(echo $SUDO_PASSWORD | sudo -S protonvpn s | grep "Status:")

if [ "$protonvpn_status" == "Status:       Connected" ]
then
	echo VPN:UP
else
	echo VPN:DOWN
fi


