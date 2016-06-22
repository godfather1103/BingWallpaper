#!/usr/bin/python
#-*- coding: utf-8 -*-

import urllib
import os
import time
import datetime
import getpass
import json

date = str(datetime.date.today())

who = getpass.getuser()
path = '/home/'+who+'/Wallpaper/'+date+'/'
def exitsDir():
	if not os.path.exists(path):
		os.system('mkdir -p '+path)

def getImgUrl():
	exitsDir()
	#url = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1361089515117&FORM=HYLH1"
	#url = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1466571090995&pid=hp"
	url = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
	conn = urllib.urlopen(url)
	resp = json.loads(conn.read())
	#获取分辨率为1366X768的壁纸
	return resp['images'][0]['url'].replace('1920x1080','1366x768')

def downloadImg():
	imgUrl = getImgUrl()
	image = open(name=path+date+'.jpg',mode='wb')
	conn = urllib.urlopen(url=imgUrl)
	image.write(conn.read())
	image.close()

if __name__ == '__main__':
	haveNetWork = False
	while not haveNetWork:
		msg = os.system('ping -c 1 cn.bing.com')
		if msg:
			time.sleep(1000)
		else:
			haveNetWork = True
	downloadImg()
	os.system('gsettings set org.gnome.desktop.background picture-uri "file://'+path+date+'.jpg"')