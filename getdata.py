import os

class GetDataUtil(object):
    def __init__(self):
        self.min = ["00","10","20","30","40","50"]
        self.hour = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
        pass

    def getDataByYY_MM_DD(self,yyyy,mm,dd):
        for hh in self.hour:
            self.getDataByYY_MM_DD_HH(yyyy,mm,dd,hh)


    def getDataByYY_MM_DD_HH(self,yyyy,mm,dd,hh):
        for min in self.min:
            self.getDataByYY_MM_DD_HH_MIN(yyyy,mm,dd,hh,min)

    def getDataByYY_MM_DD_HH_MIN(self,yyyy,mm,dd,hh,min):
        re = os.system("sh data2grads.sh %s %s %s %s %s"%(yyyy,mm,dd,hh,min))
        if re!=0:
            raise Exception("Cannot get Data in this time or Permission Denied")



if __name__ == '__main__':
    g = GetDataUtil()
    g.getDataByYY_MM_DD_HH("2017","05","21","05")