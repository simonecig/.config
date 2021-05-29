#!/bin/sh
xset r rate 250 30 &
compton &
wal -R &
nm-applet&
blueman-applet&
exec qtile start
