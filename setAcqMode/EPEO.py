# -*- coding: utf-8 -*-
import socket,traceback
from socketserver import TCPServer, BaseRequestHandler
import traceback
import tcpSer
import threading

DicAcq = {10:"0188000a00",20:"0188000a00",30:"0188000a00",40:"0188000a00"}

#CmdMS1 = "0188000a0000"
#CmdMS1 = "0188000a0000"

ValidMS=(10,20,30,40)

HOST='127.0.0.1'
PORT = 5011 ##服务器IP

def IsValidMS(nAcqMS):
    if nAcqMS in ValidMS:
        return  True
    else:
        return False


def refeashEQP():
    while(True):
        try:
            InputACQ = int(input("请选择输入[10,20,30,40]："))
            if IsValidMS(InputACQ) == False:
                print("无效输入!")
                break
            else:
                break
        except ValueError as e:
            print("请输入数字!")
            continue
    print (DicAcq[InputACQ])


print("###########################################################")
print("本程序需要使用IP:[192.168.0.101]\t端口[5011]")
print("采集时长:3秒,数据刷新率:10ms\n采集时长:6秒,数据刷新率:20ms\n采集时长:9秒,数据刷新率:30ms\n"+
        "采集时长:12秒, 数据刷新率:40ms\n")
print("###########################################################")

def jointhread():
    try:
        tcpSer.startsocket(HOST, PORT)
    except:
        raise

def main():
    while (True):
        try:
            switchType = str((input("请输入命令[L:显示已连接设备,R:刷新设备采集频率]："))).upper()
        except ValueError as e:
            print("请输入数字!")
            continue
        if switchType == 'R':
            refeashEQP()
        elif switchType == 'L':
            tcpSer.listallclient()
        else:
            print("无效选择，请重新输入!")
        continue

if __name__ == '__main__':
    # 启动线程
    server_thread = threading.Thread(target=jointhread)
    server_thread.setDaemon(True)
    server_thread.start()
    main()






