#! bash
import dbus
import argparse
import time
from datetime import datetime

jscript = """
var allDesktops = desktops();
print (allDesktops);
for (i=0;i<allDesktops.length;i++) {
    d = allDesktops[i];
    d.wallpaperPlugin = "org.kde.image";
    d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
    d.writeConfig("Image", "file://%s")
}
"""

wallpaperTime = [datetime.strptime('8:20', '%H:%M'), 
					datetime.strptime('8:55', '%H:%M'), 
					datetime.strptime('9:30', '%H:%M'), 
					datetime.strptime('10:05', '%H:%M'), 
					datetime.strptime('10:40', '%H:%M'), 
					datetime.strptime('11:15', '%H:%M'), 
					datetime.strptime('11:50', '%H:%M'), 
					datetime.strptime('12:25', '%H:%M'), 
					datetime.strptime('13:00', '%H:%M'), 
					datetime.strptime('13:35', '%H:%M'), 
					datetime.strptime('14:10', '%H:%M'), 
					datetime.strptime('14:45', '%H:%M'), 
					datetime.strptime('15:20', '%H:%M'), 
					datetime.strptime('15:55', '%H:%M'), 
					datetime.strptime('16:30', '%H:%M'), 
					datetime.strptime('17:30', '%H:%M')]
# wall = ["8:20", 
# 		"8:55", 
# 		"9:30", 
# 		"10:05", 
# 		"10:40", 
# 		"11:15", 
# 		"11:50", 
# 		"12:25", 
# 		"13:00", 
# 		"13:35", 
# 		"14:10", 
# 		"14:45", 
# 		"15:20", 
# 		"15:55", 
# 		"16:30", 
# 		"17:30"]
wallpapersPath = '/home/dmitriistepcenco/Wallpapers/macOS/Mojave/Mojave/'
print wallpaperTime
bus = dbus.SessionBus()
plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
currentWallpapper = 0

def changeWallpaper(wallpaper):
	plasma.evaluateScript(jscript % "{0}{1}.jpeg".format(wallpapersPath, wallpaper))

while True:
	currentTime = "{0}:{1}".format(datetime.now().hour, datetime.now().minute)
	print("Current time " + currentTime)
	currentTime = datetime.strptime(currentTime, '%H:%M')
	print("Current time " + str(currentTime))
	changeWallpaper(currentWallpapper)
	# currentWallpapper += 1
	# time.sleep(1)
	# if currentWallpapper>16:
	# 	currentWallpapper=0
	if currentTime <= wallpaperTime[0]:
		changeWallpaper(0)
	elif currentTime > wallpaperTime[0] and currentTime < wallpaperTime[1]:
		changeWallpaper(1)
	elif currentTime > wallpaperTime[1] and currentTime < wallpaperTime[2]:
		changeWallpaper(2)
	elif currentTime > wallpaperTime[2] and currentTime < wallpaperTime[3]:
		changeWallpaper(3)
	elif currentTime > wallpaperTime[3] and currentTime < wallpaperTime[4]:
		changeWallpaper(4)
	elif currentTime > wallpaperTime[4] and currentTime < wallpaperTime[5]:
		changeWallpaper(5)
	elif currentTime > wallpaperTime[5] and currentTime < wallpaperTime[6]:
		changeWallpaper(6)
	elif currentTime > wallpaperTime[6] and currentTime < wallpaperTime[7]:
		changeWallpaper(7)
	elif currentTime > wallpaperTime[7] and currentTime < wallpaperTime[8]:
		changeWallpaper(8)
	elif currentTime > wallpaperTime[8] and currentTime < wallpaperTime[9]:
		changeWallpaper(9)
	elif currentTime > wallpaperTime[9] and currentTime < wallpaperTime[10]:
		changeWallpaper(10)
	elif currentTime > wallpaperTime[10] and currentTime < wallpaperTime[11]:
		changeWallpaper(11)
	elif currentTime > wallpaperTime[11] and currentTime < wallpaperTime[12]:
		changeWallpaper(12)
	elif currentTime > wallpaperTime[12] and currentTime < wallpaperTime[13]:
		changeWallpaper(13)
	elif currentTime > wallpaperTime[13] and currentTime < wallpaperTime[14]:
		changeWallpaper(14)
	elif currentTime > wallpaperTime[14] and currentTime < wallpaperTime[15]:
		changeWallpaper(15)
	elif currentTime > wallpaperTime[15]:
		changeWallpaper(16)
	time.sleep(60)