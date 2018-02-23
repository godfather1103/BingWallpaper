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
	#n这个参数的值为最多获取几张图片，实际获得的图片数可能少于n
	url = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10"
	conn = urllib.urlopen(url)
	resp = json.loads(conn.read())
	imgUrls = []
	#获取分辨率为1366X768的壁纸
	for x in range(len(resp['images'])):
		imgUrls.append('http://cn.bing.com'+(resp['images'][x]['url'].replace('1920x1080','1366x768')))
	imgUrls = list(set(imgUrls))
	#return resp['images'][0]['url'].replace('1920x1080','1366x768')
	return imgUrls

def downloadImg():
	imgUrls = getImgUrl()
	for x in range(len(imgUrls)):
		imgUrl = imgUrls[x]
		image = open(name=path+date+"-"+str(x)+'.jpg',mode='wb')
		conn = urllib.urlopen(url=imgUrl)
		image.write(conn.read())
		image.close()
	return len(imgUrls)

if __name__ == '__main__':
	haveNetWork = False
	while not haveNetWork:
		msg = os.system('ping -c 1 cn.bing.com')
		if msg:
			#每2分钟测试连一次网，看看是否连接成功！
			time.sleep(60*2)
		else:
			haveNetWork = True
	length = downloadImg()
	a = 0
	while True:
		os.system('gsettings set org.gnome.desktop.background picture-uri "file://'+path+date+"-"+str(a)+'.jpg"')
		a += 1
		a = a%length
		#print a
		#每小时切换一次壁纸
		time.sleep(60*60)
	#os.system('gsettings set org.gnome.desktop.background picture-uri "file://'+path+date+'.jpg"')