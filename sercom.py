import serial
import serial.tools.list_ports
import time

plist = list(serial.tools.list_ports.comports())

for i in plist:
    print(str(plist.index(i)+1),i)
    time.sleep(0.01)
portName = input('Please alter the port number you will operate...\n')
portName = int(portName) - 1

def WriteData():
    a = True

    print("Please input string")
    #portUsed.open()
    while(a == True):
        #ret = portUsed.read(200000)
        #print(str(ret, "utf-8"))
        # 实现回车换行，而不是结束
        endstr = "endline"  # 重新定义结束符
        strIn = ""
        for line in iter(input, endstr):  # 每行接收的东西
            strIn += line + "\n"  # 换行
        #strIn = input()
        if strIn =="exit":
            a = False
        strIn = bytes(strIn,"ascii")
        #print(strIn)
        portUsed.write(strIn)
        ret = portUsed.read(200000)
        #print(ret,"utf-8",end='')
        print(str(ret,"utf-8"),end="")
    time.sleep(1)
    pass


try:
    portUsed = serial.Serial(port=plist[portName][0], baudrate=115200, bytesize=8, stopbits=1, timeout=1)
    print("Connection Established...")
    print(portUsed.name)
    WriteData()
except Exception as e:
    print("error:",e)