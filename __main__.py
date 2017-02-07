#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

class BingImage(object):
    """docstring for BingImage"""
    BINGURL = 'http://www.bing.com/'
    JSONURL = 'HPImageArchive.aspx?format=js&idx=0&n=1&mkt=pt-BR'
    IMGFOLDER = os.getcwd() + '/images/'
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
            return self.BINGURL + parsedjson['images'][0]['url']

    def downloadimg(self):
        import datetime
        imgurl = self.getdailyimg();
        imgfilename = datetime.datetime.today().strftime('%Y%m%d') + '_' + imgurl.split('/')[-1]
        with open(self.IMGFOLDER + imgfilename, 'wb') as f:
            f.write(self.readimg(imgurl))
        self.LASTIMG = self.IMGFOLDER + imgfilename

    def checkfolder(self):
        d = os.path.dirname(self.IMGFOLDER)
        if not os.path.exists(d):
            os.makedirs(d)

    def readimg(self, url):
        import urllib.request
        with urllib.request.urlopen(url) as response:
            return response.read()


def DefineBackground(src):
    import os
    import platform
    if platform.system() == 'Linux':
        MAINCMD = "gsettings set org.gnome.desktop.background picture-uri"
        os.system(MAINCMD + ' file://' + src)


if __name__ == '__main__':
    # get a new today's image from Bing
    img = BingImage()
    # check whether a new image was get or not
    print(img.LASTIMG)
    if(img.LASTIMG):
        DefineBackground(img.LASTIMG)



