# -*- coding:utf-8 -*-
import re,os
import urllib2
import time
from datetime import datetime, timedelta


class GetLatestDataUtil(object):
    def __init__(self):
        self.FILE_NUM = 6
        self.origurl = 'http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/jma-radar/synthetic/original'
        pass

    def getLatestData(self):
        data_list = []
        date_today = datetime.utcnow().strftime("%Y/%m/%d")
        url = "%s/%s/" % (self.origurl, date_today)

        response = urllib2.urlopen(url)
        content = response.read()
        #print content
        #获取<a href></a >中的URL
        res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
        all_links = re.findall(res_url, content, re.I|re.S|re.M)
        temp_list = all_links[-self.FILE_NUM: ]
        data_list.extend(temp_list)

        if len(data_list) < self.FILE_NUM:
            date_yesterday = (datetime.utcnow() - timedelta(days=1)).strftime("%Y/%m/%d")
            url = "%s/%s/" % (self.origurl, date_yesterday)

            response = urllib2.urlopen(url)
            content = response.read()
            #print content
            #获取<a href></a >中的URL
            res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
            all_links = re.findall(res_url, content, re.I|re.S|re.M)
            temp_list = all_links[len(data_list)-self.FILE_NUM: ]
            data_list.extend(temp_list)

        return data_list

def main():
    g = GetLatestDataUtil()
    print g.getLatestData()

if __name__ == '__main__':
    main()
