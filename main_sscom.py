import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
import time
from sscom import *
import serial

class MyPyQT_Form(QtWidgets.QWidget,Sscom_Form):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)
        self.portSelected = None
        self.connectionStatus = False
        self.baudrate = 110
        self.Port = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.RefreshOutput)  # 计时结束调用operate()方法
        self.timer.start(1000)  # 设置计时间隔并启动
        self.readPast = ''
        self.returnType = 'char'
        self.sendType = 'char'
        self.textBrowser_2.setText("OFF")

    def RefreshOutput(self):
        try:
            if self.connectionStatus == True:
                #self.Port = serial.Serial(port=self.portSelected, baudrate=self.baudrate, bytesize=8, stopbits=1, timeout=1)
                self.readNow = self.Port.read(2000000)
                if self.readNow != self.readPast:
                    self.readPast = self.readNow
                    if self.returnType == 'char':
                        self.textBrowser.append(str(self.readNow,"utf-8"))
                    else:
                        pass
                else:
                    pass
        except Exception as E:
            self.RecordError(E)

    def SetBaudrate(self):
        self.baudrate = int(self.comboBox.currentText())

    def CheckPortSelected(self):#查看选中的端口

        try:
            self.Port.close()
        except:
            pass

        self.portSelected = self.comboBox_2.currentText()
        self.SetBaudrate()

        try:
            self.Port = serial.Serial(port=self.portSelected, baudrate=self.baudrate, bytesize=8, stopbits=1, timeout=0.1)
            self.Port.close()
        except Exception as e:
            self.textBrowser.append(e,"\n")

    def SwitchDevice(self):#打开/关闭设备
        #self.Port = serial.Serial(port=self.portSelected, baudrate=self.baudrate, bytesize=8, stopbits=1, timeout=1)
        try:
            if self.connectionStatus == False:
                self.CheckPortSelected()
                self.Port.open()
                self.connectionStatus = True
                self.textBrowser.append("System Report: Connection Established...")
                self.textBrowser.append(time.asctime( time.localtime(time.time()) ))
                self.textBrowser_2.setText("On")

            else:
                self.Port.close()
                self.textBrowser.append("System Report: Port Closed...")
                self.connectionStatus = False
                self.textBrowser_2.setText("OFF")
        except Exception as E:
            self.RecordError(E)

    def refreshdevice(self):
        pass

    def SaveAsLog(self):#记录日志

        StrText = self.textBrowser.toPlainText()
        qS = str(StrText)
        date = time.strftime("%d-%m-%Y")
        logFilename = str(date) + ".txt"
        f = open(logFilename, 'a')
        print(f.write('\n{}'.format(qS)))
        f.close()

    def RecordError(self,E):            #记录错误进入日志
        date = time.strftime("%d-%m-%Y")
        errorLogName = str(date) + "Errpr.txt"
        f = open(errorLogName, 'a')
        print(f.write('\n{}'.format(E)))
        f.write(time.asctime( time.localtime(time.time()) ))
        f.close()
        print(E)

    def SendMessage(self):
        try:
            self.sendArea = self.textEdit.toPlainText()
            self.sendArea = str(self.sendArea)
            #endstr = "endline"  # 重新定义结束符
            #strIn = ""
            #for line in iter(self.sendArea, endstr):  # 每行接收的东西
                #strIn += line + "\n"  # 换行
            #if strIn == "exit":
                #a = False
            strIn = bytes(self.sendArea, "ascii")
            # print(strIn)
            self.Port.write(strIn)
            self.textBrowser.append(time.asctime( time.localtime(time.time()) ))
            self.textBrowser.append("Send→")
            self.textBrowser.append(self.sendArea)
            self.textBrowser.append("Received←")
            self.textBrowser.append(str(self.Port.read(2000000), "utf-8"))
        except Exception as E:
            self.RecordError(E)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyPyQT_Form()
    window.show()
    sys.exit(app.exec_())
