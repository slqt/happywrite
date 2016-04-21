#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016-04-07
@author: slqt
'''
import commands
import platform
import logging

def getInformation():
    try:
        grains = {}
        grains['resCentOS'] ={'resName': _resName()}
        return grains['resCentOS']
    except Exception,e:
        logging.debug(e)
        return {'error':'Error had happened!'}
        
def _resName():
    '''
    get resource name for minions
    '''
    try:
        resName_info = platform.node()
        return resName_info
    except Exception,e:
        logging.info(e)
        resName_info = commands.getstatusoutput('hostname')
        return resName_info
    except Exception, e:
        logging.debug(e)
        return ""
        
if __name__=="__main__":
    a=getInformation()
    print a
