import urllib
import urllib2
import datetime
import sys
import os
import json

##########################################################

##########################################################
def getData():
    mainUrl="http://h.bilibili.com/wallpaperApi?action=getOptions&page=1"
    resp=urllib2.urlopen(mainUrl).read()
    data=json.loads(resp)
    return data
def toPic():
    data=getData()

    for i in range(1, len(data)):
        for j in range(0, len(data[i]['detail'])):
            if data[i]['detail'][j]['height'] == "1080" or data[i]['detail'][j]['width'] == "1920":
                id0=data[i]['detail'][j]['id']
                picUrl="http://h.bilibili.com/wallpaper?action=download&img_id="+id0
                picName="./pic/"+str(i)+".png"
                #try:
                urllib.urlretrieve(picUrl, picName)
                #except Exception, e:
                #    print str(e)
                print("NO"+str(i)+" Pic Saved!")
                break

def main():
    print("===%s start===%s"%(sys.argv[0], datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")))
    if not os.path.exists('pic'):
        os.mkdir('pic')
    toPic()
    print("===%s end===%s"%(sys.argv[0], datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d )%H:%M:%S")))

if __name__ == "__main__":
    main()
