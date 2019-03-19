# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\v1.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sys
import socket
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IPCatcher(object):
    NUM = 0
    def setupUi(self, IPCatcher):
        # 创建主界面
        IPCatcher.setObjectName("IPCatcher")
        IPCatcher.setWindowModality(QtCore.Qt.NonModal)
        IPCatcher.resize(1545, 580)
        IPCatcher.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(IPCatcher)
        self.centralwidget.setObjectName("centralwidget")
        # 创建捕获按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 20, 91, 31))
        # 创建清空按钮
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(490, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.showIPData)
        self.pushButton2.setFont(font)
        self.pushButton2.setAutoFillBackground(True)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.dataClear)
        # 创建标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 221, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # 创建spinBox控件
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(250, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        # 创建表格显示框tableView控件
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 80, 1504, 471))
        self.tableView.setObjectName("tableView")
        self.model = QtGui.QStandardItemModel(self.tableView)
        self.model.setColumnCount(16)
        self.model.setRowCount(0)
        self.setHeaderData()
        self.tableView.setModel(self.model)
        self.setColumnWidth()

        IPCatcher.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(IPCatcher)
        self.statusbar.setObjectName("statusbar")
        IPCatcher.setStatusBar(self.statusbar)

        self.retranslateUi(IPCatcher)
        QtCore.QMetaObject.connectSlotsByName(IPCatcher)

    def retranslateUi(self, IPCatcher):
        _translate = QtCore.QCoreApplication.translate
        IPCatcher.setWindowTitle(_translate("IPCatcher", "IP数据包捕获程序"))
        self.pushButton.setText(_translate("IPCatcher", "捕获"))
        self.pushButton2.setText(_translate("IPCatcher", "清空"))
        self.label.setText(_translate("IPCatcher", "需要捕获的数据包的个数："))

    def catchIPData(self):
        # 获取本机IP作为公共网络接口
        HOST = socket.gethostbyname(socket.gethostname())
        # 创建一个原始套接字
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        # 将该套接字与公共网络接口绑定
        s.bind((HOST, 0))
        # 设定该套接字包含IP数据报首部
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        # 设定该套接字接收所有数据包
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        # 接收一个数据包并返回
        packet = s.recvfrom(4096)
        return packet

    def showIPData(self):
        # 获取用户选择的捕获次数
        num = self.spinBox.value()
        for i in range(num):
            # 调用捕获模块
            packet = self.catchIPData()
            # 调用解析模块并将数据显示在表格框中
            self.setItem(decodeIpHeader(packet[0]), self.NUM)
            # 设置表格框的高度
            self.tableView.setRowHeight(self.NUM, 30)
            # 记录当前行+1
            self.NUM += 1
        # 设置表格框的宽度
        self.setColumnWidth()


        # disabled promiscuous mode
        #s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

    def setHeaderData(self):
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "版本")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "首部长度")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "服务类型")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "总长度")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "标识")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "标志")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "还有分片")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "不能分片")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "片偏移")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, "TTL")
        self.model.setHeaderData(10, QtCore.Qt.Horizontal, "协议")
        self.model.setHeaderData(11, QtCore.Qt.Horizontal, "首部检验和")
        self.model.setHeaderData(12, QtCore.Qt.Horizontal, "源IP地址")
        self.model.setHeaderData(13, QtCore.Qt.Horizontal, "目的IP地址")
        self.model.setHeaderData(14, QtCore.Qt.Horizontal, "选项")
        self.model.setHeaderData(15, QtCore.Qt.Horizontal, "数据")

    def setColumnWidth(self):
        self.tableView.setColumnWidth(0, 40)
        self.tableView.setColumnWidth(1, 60)
        self.tableView.setColumnWidth(2, 60)
        self.tableView.setColumnWidth(3, 60)
        self.tableView.setColumnWidth(4, 60)
        self.tableView.setColumnWidth(5, 60)
        self.tableView.setColumnWidth(6, 60)
        self.tableView.setColumnWidth(7, 60)
        self.tableView.setColumnWidth(8, 60)
        self.tableView.setColumnWidth(9, 60)
        self.tableView.setColumnWidth(10, 60)
        self.tableView.setColumnWidth(11, 100)
        self.tableView.setColumnWidth(12, 140)
        self.tableView.setColumnWidth(13, 140)
        self.tableView.setColumnWidth(14, 100)
        self.tableView.setColumnWidth(15, 420)

    def setItem(self, data, row):
        self.model.setItem(row, 0, QtGui.QStandardItem(str(data['version'])))
        self.model.item(row, 0).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 1, QtGui.QStandardItem(str(data['headLength'])))
        self.model.item(row, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 2, QtGui.QStandardItem(str(data['serviceType'])))
        self.model.item(row, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 3, QtGui.QStandardItem(str(data['totalLength'])))
        self.model.item(row, 3).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 4, QtGui.QStandardItem(str(data['identification'])))
        self.model.item(row, 4).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 5, QtGui.QStandardItem(str(data['flag'])))
        self.model.item(row, 5).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 6, QtGui.QStandardItem(str(data['moreFragment'])))
        self.model.item(row, 6).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 7, QtGui.QStandardItem(str(data['dontFragment'])))
        self.model.item(row, 7).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 8, QtGui.QStandardItem(str(data['fragmentOffset'])))
        self.model.item(row, 8).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 9, QtGui.QStandardItem(str(data['TTL'])))
        self.model.item(row, 9).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 10, QtGui.QStandardItem(str(data['protocol'])))
        self.model.item(row, 10).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 11, QtGui.QStandardItem(str(data['headerCheckSum'])))
        self.model.item(row, 11).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 12, QtGui.QStandardItem(data['sourceAddress']))
        self.model.item(row, 12).setTextAlignment(QtCore.Qt.AlignCenter)
        self.model.setItem(row, 13, QtGui.QStandardItem(data['destinationAddress']))
        self.model.item(row, 13).setTextAlignment(QtCore.Qt.AlignCenter)
        options = ''
        for op in data['options']:
            options += str(op)
            options += ','
        self.model.setItem(row, 14, QtGui.QStandardItem(options))
        self.model.item(row, 14).setTextAlignment(QtCore.Qt.AlignCenter)
        dat = '   '
        for da in data['data']:
            dat += str(da)
            dat +=','
        self.model.setItem(row, 15, QtGui.QStandardItem(dat))
        # self.model.item(row, 15).setTextAlignment(QtCore.Qt.AlignCenter)

    def dataClear(self):
        self.NUM = 0
        self.model.setRowCount(0)


def decodeIpHeader(packet):
    # 创建一个空字典
    IPDatagram = {}
    # 根据RFC791协议对数据包进行解析
    IPDatagram['version'] = packet[0] >> 4
    IPDatagram['headLength'] = packet[0] & 0x0f
    IPDatagram['serviceType'] = packet[1]
    IPDatagram['totalLength'] = (packet[2] << 8) + packet[3]
    IPDatagram['identification'] = (packet[4] << 8) + packet[5]
    IPDatagram['flag'] = packet[6] >> 5
    IPDatagram['moreFragment'] = IPDatagram['flag'] & 1
    IPDatagram['dontFragment'] = (IPDatagram['flag'] >> 1) & 1
    IPDatagram['fragmentOffset'] = ((packet[6] & 0x1f) << 8) + packet[7]
    IPDatagram['TTL'] = packet[8]
    IPDatagram['protocol'] = packet[9]
    IPDatagram['headerCheckSum'] = (packet[10] << 8) + packet[11]
    # 源IP地址和目的IP地址都按照IP地址的格式用字符串存储
    IPDatagram['sourceAddress'] = "%d.%d.%d.%d" % (packet[12], packet[13], packet[14], packet[15])
    IPDatagram['destinationAddress'] = "%d.%d.%d.%d" % (packet[16], packet[17], packet[18], packet[19])
    # 根据数据包中头部长度确定是否有选项，如果有则添加至option列表中
    IPDatagram['options'] = []
    if IPDatagram['headLength'] > 5:
        step = 5
        while step < IPDatagram['headLength']:
            IPDatagram['options'].append(packet[step * 4])
            IPDatagram['options'].append(packet[step * 4 + 1])
            IPDatagram['options'].append(packet[step * 4 + 2])
            IPDatagram['options'].append(packet[step * 4 + 3])
            step += 1
    # 根据数据包中的总长度将数据部分添加至data列表中
    IPDatagram['data'] = []
    step = IPDatagram['headLength'] * 4
    while step < IPDatagram['totalLength']:
        IPDatagram['data'].append(packet[step])
        step += 1
    # 返回储存有数据包数据的字典
    return IPDatagram

def catchIPData():
    # 获取本机IP作为公共网络接口
    HOST = socket.gethostbyname(socket.gethostname())
    # 创建一个原始套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    # 将该套接字与公共网络接口绑定
    s.bind((HOST, 0))
    # 设定该套接字包含IP数据报首部
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # 设定该套接字接收所有数据包
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    # 接收一个数据包并返回
    packet = s.recvfrom(4096)
    return packet

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_IPCatcher()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
