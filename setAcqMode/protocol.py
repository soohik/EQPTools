# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import struct

import ctypes
import time

# 使用python 定义结构体与共用体
class WBCANHEAD(ctypes.Structure):
    __slots__ = ()
    _fields_ = [
        ('DLC', ctypes.c_ubyte,4),
        ('CAN', ctypes.c_ubyte, 4),
        ('Address1', ctypes.c_ubyte, 1),
        ('B', ctypes.c_ubyte, 1),
        ('G', ctypes.c_ubyte, 1),
        ('MS', ctypes.c_ubyte, 1),
        ('DIR', ctypes.c_ubyte, 1),
        ('R0', ctypes.c_ubyte, 3),
        ('TYPE', ctypes.c_ubyte, 3),
        ('Address', ctypes.c_ubyte, 5),
        ('InxFrame', ctypes.c_ubyte),
        ('SumFrame', ctypes.c_ubyte),
        ('CMD', ctypes.c_byte),
        ('CMD2', ctypes.c_byte),
        ('ArrData', ctypes.c_byte * 6)
    ]


class CWBSENDCAN(ctypes.Union):
    __slots__ = ()
    _fields_ = [
        ('HEAD', WBCANHEAD),
        ('binary_data', ctypes.c_ubyte*13)
    ]




#刷新频率
def packetautostime(addr):
    now = int(time.time())

    send = CWBSENDCAN()
    send.HEAD.CAN = 0x8     #向下
    send.HEAD.DLC = 0x6     #长度
    send.HEAD.Address = addr
    send.HEAD.Address1 = addr >>5
    send.HEAD.CMD = 0x1         #一级命令码
    send.HEAD.CMD2 = 0x7F       #二级 校对时钟
    send.HEAD.ArrData[3] = now >> 0
    send.HEAD.ArrData[2] = now >> 8
    send.HEAD.ArrData[1] = now >> 16
    send.HEAD.ArrData[0] = now >> 24
    return send


#刷新采样率
def packetautostime(addr,acqno):

    send = CWBSENDCAN()
    send.HEAD.CAN = 0x8     #向下
    send.HEAD.DLC = 0x6     #长度
    send.HEAD.Address = addr
    send.HEAD.Address1 = addr >>5
    send.HEAD.CMD = 0x1         #一级命令码
    send.HEAD.CMD2 = 0x88
    send.HEAD.ArrData[0] = 0xaa
    send.HEAD.ArrData[1] = 0x28
    send.HEAD.ArrData[1] = 0x00
    return send

nba = packetautostime(63)
for i in nba.binary_data:
    print('%02x ' % i,end="")
