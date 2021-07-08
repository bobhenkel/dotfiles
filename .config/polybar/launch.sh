#!/usr/bin/env bash

# Terminate already running bar instances
if pgrep -x polybar >/dev/null
then
    killall -q polybar
fi
# Wait until the processes have been shut down
while pgrep -x polybar >/dev/null; do sleep 1; done

if type "xrandr"; then
	  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
		      MONITOR=$m polybar --reload mainbar-herbstluftwm &
		        done
		else
			  polybar mainbar-herbstluftwm &
fi

echo "Bars launched..."

#polybar mainbar-herbstluftwm &
