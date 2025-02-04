# -*- coding: utf-8 -*-
"""
Created on Thr Jan 10 09:13:24 2018

@author: takata@innovotion.co.jp
@author: harada@keigan.co.jp
"""

import sys
import pathlib
from time import sleep

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from pykeigan import usbcontroller
from pykeigan import utils

"""
----------------------
モーターを5rpmで 正転(10秒) -> 逆転(10秒) -> 停止(トルクあり) -> 停止(トルク無し)
----------------------

"""
dev=usbcontroller.USBController('/dev/ttyUSB0',False)#モーターのアドレス 参照 usb-simple-connection.py
dev.enable_action()#安全装置。初めてモーターを動作させる場合に必ず必要。
dev.set_speed(utils.rpm2rad_per_sec(5))#rpm -> radian/sec

dev.set_led(1, 0, 200, 0)
dev.run_forward()

sleep(10)

dev.set_led(1, 0, 0, 200)
dev.run_reverse()

sleep(10)

dev.set_led(1, 200, 0, 0)
dev.stop_motor()

sleep(10)

dev.set_led(1, 100, 100, 100)
dev.free_motor()


"""
Exit with key input
"""
while True:
    print("---------------------------------------")
    inp=input('Exit:[Other key] >>')
    if inp !=None:
        dev.set_led(1, 100, 100, 100)
        dev.disconnect()
        break