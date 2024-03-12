winecfg
echo -e "\n"
find / -type d -name drive_c
echo -e "\n"

Xvfb :0 -screen 0 1024x768x16 &
jid=$!
DISPLAY=:0.0 WINEPREFIX=~/.wine64 wine cmd.exe


#DISPLAY=:0.0 WINEPREFIX=~/.wine64 wine python --version
#echo -e "\n"
#wine python --version
