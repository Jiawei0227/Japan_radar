from GetDataUtil import GetDataUtil
from GetImageUtil import GetImageUtil

if __name__=='__main__':
    yyyy = '2017'
    mm = '05'
    dd = '26'
    hh = '11'
    min = '20'
    getDataUtil = GetDataUtil()
    getDataUtil.getDataByYY_MM_DD_HH_MIN(yyyy,mm,dd,hh,min)
    getImageUtil = GetImageUtil()
    getImageUtil.getImage(yyyy,mm,dd,hh,min)