#!/usr/bin/env bash

source .bash_profile #password is stored here
protonvpn_status=$(echo $SUDO_PASSWORD | sudo -S protonvpn s | grep "Status:")

if [ "$protonvpn_status" == "Status:       Connected" ]
then
	echo VPN:UP
else
	echo VPN:DOWN
fi





