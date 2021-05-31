#!/bin/sh
xset r rate 250 35 &
compton &
wal -R &
nm-applet&
blueman-applet&
exec qtile start
