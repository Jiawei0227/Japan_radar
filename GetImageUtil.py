#coding=utf-8
import grads
import os
from grads.ganum import GaNum



class GetImageUtil(object):

    def __init__(self):
        self.__ga = grads.GrADS()
        self.stations = [[120,30],[125,35]]
        self.radius = 3
        pass

    def getImage(self,yyyy,mm,dd,hh,min):
        ga = self.__ga
        fh = ga.open('%s/%s/%s/%s/dat/%s%s%s%s%sview_radar.ctl'%(yyyy,mm,dd,hh,yyyy,mm,dd,hh,min))
        ts = ga.exp("rr")  # export variable ts from GrADS)
        #ga("run define_color.gs")
        for station in self.stations:
            ga("clear")
            ga("set lon %s %s"%(station[0],station[0]+self.radius))
            ga("set lat %s %s"%(station[1],station[1]+self.radius))
            ga("set cmin 0")
            ga("set gxout shaded")
            ga("set display color white")
            ga("set annot 0<0>")
            ga("set grid off")
            ga("set mpdraw off")
            ga("set poli off")
            ga("display rr")
        #    self.__savePicture("%s/%s/%s/%s/pic"%(yyyy,mm,dd,hh),"%s%s%s%s%s"%(yyyy,mm,dd,hh,min))

        return

    def __savePicture(self,path,name):
        ga=self.__ga
        ga("printim %s.png  White"%(name))
        os.system("mkdir -p %s"%(path))
        os.system("mv %s.png %s/%s.png"%(name,path,name))


if __name__ == '__main__':
    g = GetImageUtil()
    g.getImage("2017","05","28","09","20")
    height = int( input("Please enter the height: ") )
