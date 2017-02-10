#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
IMGFOLDER = os.getcwd() + '/images/'


class BingImage(object):
    """docstring for BingImage"""
    BINGURL = 'http://www.bing.com/'
    JSONURL = 'HPImageArchive.aspx?format=js&idx=0&n=1&mkt=pt-BR'
    LASTIMG = None

    def __init__(self):
        super(BingImage, self).__init__()
        try:
            self.downloadimg()
        except:
            pass

    def getdailyimg(self):
        import json
        import urllib.request
        with urllib.request.urlopen(self.BINGURL + self.JSONURL) as response:
            rawjson = response.read().decode('utf-8')
            parsedjson = json.loads(rawjson)
            return self.BINGURL + parsedjson['images'][0]['url'][1:]

    def downloadimg(self):
        import datetime
        imgurl = self.getdailyimg();
        imgfilename = datetime.datetime.today().strftime('%Y%m%d') + '_' + imgurl.split('/')[-1]
        with open(IMGFOLDER + imgfilename, 'wb') as f:
            f.write(self.readimg(imgurl))
        self.LASTIMG = IMGFOLDER + imgfilename

    def checkfolder(self):
        d = os.path.dirname(IMGFOLDER)
        if not os.path.exists(d):
            os.makedirs(d)

    def readimg(self, url):
        import urllib.request
        with urllib.request.urlopen(url) as response:
            return response.read()


def DefineBackground(src):
    import platform
    if platform.system() == 'Linux':
        MAINCMD = "gsettings set org.gnome.desktop.background picture-uri"
        os.system(MAINCMD + ' file://' + src)


def GetRandomImg():
    """Return a random image already downloaded from the images folder"""
    import random
    f = []
    for (dirpath, dirnames, filenames) in os.walk(IMGFOLDER):
        f.extend(filenames)
        break
    return IMGFOLDER + random.choice(f)


if __name__ == '__main__':
    # get a new today's image from Bing
    img = BingImage()
    # check whether a new image was get or not
    if(img.LASTIMG):
        DefineBackground(img.LASTIMG)
    else:
        DefineBackground(GetRandomImg())
    print('Background defined')



