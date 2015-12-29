#!/usr/bin/env python

import os, sys
import urllib2
import urllib
import time

USERNAME = 'admin'
PASSWORD = 'admin'
URL = "http://192.168.0.5"
CMD = {'form_id':'firmware_update', 'reboot_value':'', 'tftp_server_ip_address':'192.168.0.2', 'submit': 'Start', 'reboot': 'Reboot'}

class Firmware_Downloader(object):
    def __init__(self, url=None):
        if url:
            self.url = url
        else:
            self.url = self.guess_ip()

    def auth(self, url):
        p = urllib2.HTTPPasswordMgrWithDefaultRealm()
        p.add_password(None, url, USERNAME, PASSWORD)
        handler = urllib2.HTTPBasicAuthHandler(p)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

    def post(self, posturl, params):
        '''
            do the POST action of form in html

        :param posturl: POST url
        :param params: dict to orgnize the parameters that needed in post action
        :return:
        '''
        self.auth(posturl)
        data = urllib.urlencode(params)
        req = urllib2.Request(posturl, data)
        try:
            response = urllib2.urlopen(req, timeout=3)
        except:
            # after reboot, controller will lost response
            print "rebooting..."

    def get(self, url):
        '''
            do the GET action of form in html

        :param url: GET url
        :return:
        '''
        self.auth(url)
        return urllib2.urlopen(url).read()

    def guess_ip(self):
        found = False
        for i in range(0, 256):
            if found:
                break
            url = "http://192.168.0." + str(i) + "/firmware_update.html"
            self.auth(url)
            try:
                result = urllib2.urlopen(url, timeout=1).read()
                found = True
            except:
                found = False
        if found:
            url = "http://192.168.0." + str(i-1)
            print "found correct ip: %s" % url
        else:
            print "can't find controller's ip"
            raise TypeError
        return url

    def wait(self, timeout=600):
        '''
            wait the download procedure complete

        :param timeout: timeout of download
        :return:
        '''
        start_time = time.time()
        geturl = self.url + "/get.cgi?firmware_update=status"
        current_time = time.time()
        result = self.get(geturl)
        print result
        while 'SUCCESS' not in result and (current_time-start_time) < timeout:
            if 'ERROR' in result:
                print "something error, can't download firmware!!!"
                raise TypeError
                break
            time.sleep(5)
            current_time = time.time()
            result = self.get(geturl)
            print result

        if (current_time-start_time) >= timeout:
            print "Timeout!!!"
            raise TypeError

        print "Download complete, elapsed time: %ds" % (current_time-start_time)

    def download(self):
        # auth this url to connect firstly, otherwise post timeout
        print self.url
        url = self.url + "/firmware_update.html"
        self.auth(url)
        posturl = self.url + "/post.cgi"
        download_cmd = CMD
        self.post(posturl, download_cmd)

    def reboot(self):
        posturl = self.url + "/post.cgi"
        reboot_cmd = CMD
        reboot_cmd['reboot_value'] = 'do_it'
        self.post(posturl, reboot_cmd)

    def confirm(self):
        # reboot, wait 2 min to get status to confirm download complete
        time.sleep(120)
        geturl = self.url + "/get.cgi?firmware_update=status"
        result = self.get(geturl)
        if "idle" in result.lower():
            print "download successful!!!"
        else:
            print "download fail!!!"
            raise TypeError

if __name__ == '__main__':
    f = Firmware_Downloader()
    f.download()
    f.wait()
    f.reboot()
    f.confirm()

