# -*- coding:utf-8 -*-
import urllib
import time
import hmac
import requests
from MagicStack.api import logger


class APIRequest(object):
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.header = APIRequest.get_headers(self, self.username, self.password)


    #proxy的username,password
    def get_headers(self, username, password):
        timestamp = time.time()
        headers = dict()
        data = {
            'X-Timestamp':int(timestamp),
            'X-Username':username
        }
        message = urllib.urlencode(data)
        passwd = hmac.new(password)
        passwd.update(message)
        hexdigest = passwd.hexdigest()
        headers['X-Timestamp'] = str(int(timestamp))
        headers['X-Username'] = username
        headers['X-Hexdigest'] = hexdigest
        headers['Content-Type'] = 'application/json'
        return headers

    def req_get(self):
        try:
            req = requests.get(self.url, headers=self.header)
            msg = req.json()
            codes = req.status_code
        except Exception as e:
                logger.error(e)
                codes = 500
                msg = e.message
        return msg, codes

    def req_post(self, data, **kwargs):
        try:
            req = requests.post(self.url, headers=self.header, data=data, **kwargs)
            msg = req.json()
            codes = req.status_code
        except Exception as e:
                logger.error(e)
                codes = 500
                msg = e.message
        return msg, codes

    def req_put(self, data):
        try:
            req = requests.put(self.url, headers=self.header, data=data)
            codes = req.status_code
            msg = req.json()
        except Exception as e:
                logger.error(e)
                codes = 500
                msg = e.message
        return msg, codes

    def req_del(self, data):
        try:
            req = requests.delete(self.url, headers=self.header, data=data)
            codes = req.status_code
            msg = req.json()
            logger.debug("msg:%s    status_codes:%s" % (msg, codes))
        except Exception as e:
                logger.error(e)
                codes = 500
                msg = e.message
        return msg, codes

