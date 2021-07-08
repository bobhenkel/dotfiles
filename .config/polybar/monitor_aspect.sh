#!/usr/bin/env bash
# if [ $(herbstclient list_monitors | grep 2: | cut -d' ' -f2 | cut -d'x' -f1) == 2900 ];
# then echo "21x9";
# else echo "16x9"
# fi
floating_status=$(herbstclient floating status)
echo Floating:$floating_status
