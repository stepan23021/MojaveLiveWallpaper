#!/bin/bash
wallpaperTime=('8:20' '8:55' '9:30' '10:05' '10:40' '11:15' '11:50' '12:25' '13:00' '13:35' '14:10' '14:45' '15:20' '15:55' '16:30' '17:30');

changeWallpaper() {
	dbus-send --session --dest=org.kde.plasmashell --type=method_call /PlasmaShell org.kde.PlasmaShell.evaluateScript '
	string: var Desktops = desktops(); for (i=0;i-ltDesktops.length;i++) { d = Desktops[i]; d.wallpaperPlugin = "org.kde.image"; 
	d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General"); d.writeConfig("Image", "file]///home/igorvdovicenco/Wallpapers/4.jpeg"); }'
}

while true
do
	# echo ${wallpaperTime[0]} | cut -d':' -f 2;
	currentHour=$(date +"%H");
	currentMinutes=$(date +"%M");
	if (($currentHour <= $(echo ${wallpaperTime[0]} | cut -d':' -f 1) && $currentMinutes < $(echo ${wallpaperTime[0]} | cut -d':' -f 2)))
	then
		changeWallpaper 1
	elif (($currentHour >= $(echo ${wallpaperTime[0]} | cut -d':' -f 1) && $currentMinutes < $(echo ${wallpaperTime[0]} | cut -d':' -f 2) &&))
	then	
		changeWallpaper 2
	# elif [$currentTime -gt ${wallpaperTime[1]} && ${wallpaperTime[1]} -lt ${wallpaperTime[2]}]
	# then
	# 	changeWallpaper 3
	# elif [$currentTime -gt ${wallpaperTime[2]} && ${wallpaperTime[2]} -lt ${wallpaperTime[3]}]
	# then
	# 	changeWallpaper 4
	# elif [$currentTime -gt ${wallpaperTime[3]} && ${wallpaperTime[3]} -lt ${wallpaperTime[4]}]
	# then
	# 	changeWallpaper 5
	# elif [$currentTime -gt ${wallpaperTime[4]} && ${wallpaperTime[4]} -lt ${wallpaperTime[5]}]
	# then
	# 	changeWallpaper 6
	# elif [$currentTime -gt ${wallpaperTime[5]} && ${wallpaperTime[5]} -lt ${wallpaperTime[6]}]
	# then
	# 	changeWallpaper 7
	# elif [$currentTime -gt ${wallpaperTime[6]} && ${wallpaperTime[6]} -lt ${wallpaperTime[7]}]
	# then
	# 	changeWallpaper 8
	# elif [$currentTime -gt ${wallpaperTime[7]} && ${wallpaperTime[7]} -lt ${wallpaperTime[8]}]
	# then
	# 	changeWallpaper 9
	# elif [$currentTime -gt ${wallpaperTime[8]} && ${wallpaperTime[8]} -lt ${wallpaperTime[9]}]
	# then
	# 	changeWallpaper 10
	# elif [$currentTime -gt ${wallpaperTime[9]} && ${wallpaperTime[9]} -lt ${wallpaperTime[10]}]
	# then
	# 	changeWallpaper 11
	# elif [$currentTime -gt ${wallpaperTime[10]} && ${wallpaperTime[10]} -lt ${wallpaperTime[11]}]
	# then
	# 	changeWallpaper 12
	# elif [$currentTime -gt ${wallpaperTime[11]} && ${wallpaperTime[11]} -lt ${wallpaperTime[12]}]
	# then
	# 	changeWallpaper 13
	# elif [$currentTime -gt ${wallpaperTime[12]} && ${wallpaperTime[12]} -lt ${wallpaperTime[13]}]
	# then
	# 	changeWallpaper 14
	# elif [$currentTime -gt ${wallpaperTime[13]} && ${wallpaperTime[13]} -lt ${wallpaperTime[14]}]
	# then
	# 	changeWallpaper 15
	# elif [$currentTime -gt ${wallpaperTime[14]} && ${wallpaperTime[14]} -lt ${wallpaperTime[15]}]
	# then
	# 	changeWallpaper 16
	fi
	sleep 1
done
