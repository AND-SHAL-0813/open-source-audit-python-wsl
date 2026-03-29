#!/bin/bash
# Script 2: FOSS Package Inspector

PACKAGE="python3"

# Check if package is installed
if dpkg -l | grep -q $PACKAGE; then
    echo "$PACKAGE is installed."
    dpkg -l | grep $PACKAGE | head -1
    python3 --version
else
    echo "$PACKAGE is NOT installed."
fi

# Case statement
case $PACKAGE in
    python3) echo "Python: simple and powerful open source language" ;;
    apache2) echo "Apache: the web server that built the open internet" ;;
    mysql) echo "MySQL: open source database used worldwide" ;;
    vlc) echo "VLC: open source media player that plays anything" ;;
    *) echo "Unknown package" ;;
esac
