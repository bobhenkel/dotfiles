#!/usr/bin/env bash
if [ "true" == "$(herbstclient get focus_follows_mouse)" ]; then echo 'MouseFocus:+'; else echo 'MouseFocus:-'; fi
