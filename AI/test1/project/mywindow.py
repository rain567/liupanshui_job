import base64

from PyQt5.QtWidgets import QMainWindow,QFileDialog
from PyQt5.QtCore import QTimer,QDateTime,QDate,QTime
from mainwindow import Ui_MainWindow
from cameravideo import camera
import requests,json

class mywindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        #创建一个时间定时器
        self.datetime = QTimer()
        #启动获取系统时间/日期定时器,定时时间为500ms，500ms产生一次信号
        self.datetime.start(500)
        #信号与槽的关联
        #self.actionopen：指定对象
        #triggered：信号
        #connect：关联（槽函数）
        #self.on_actionopen():关联的函数
        self.actionopen.triggered.connect(self.on_actionopen)
        self.actionclose.triggered.connect(self.on_actionclose)
        #关联时间/日期的定时器信号与槽函数
        self.datetime.timeout.connect(self.data_time )

        self.pushButton.clicked.connect(self.get_accesstoken)
        self.pushButton_2.clicked.connect(self.get_face)

    #data_time函数获取日期与时间，添加到对应的定时器
    def data_time(self):
        # 获取日期
        date = QDate.currentDate()
        #print(date)
        self.dateEdit.setDate(date)
        self.label_3.setText(date.toString())
        # 获取时间
        time = QTime.currentTime()
        #print(time)
        self.timeEdit.setTime(time)
        self.label_2.setText(time.toString())
        # 获取日期时间
        datetime = QDateTime.currentDateTime()
        #print(datetime)

    def on_actionclose(self):
        #关闭摄像头
        self.cameravideo.close_camera()
        #关闭定时器，不再去获取摄像头的数据
        self.timeshow.stop()
        self.label.setText("摄像头画面显示")
    '''
    信号槽功能：
        当某个组件设计了信号槽功能（关联信号槽）时，当信号产生，会主动调用槽函数，去完成对应的一个功能
        信号：当以某种特点的操作，操作到这个组件时，就会主动产生对应操作的信号
    '''
    def on_actionopen(self):
        #启动摄像头
        self.cameravideo = camera()
        #启动定时器，进行定时，每个多长时间进行一次获取摄像头数据进行显示
        self.timeshow = QTimer(self)
        self.timeshow.start(10)
        #10ms的定时器启动，每到10ms就会产生一个信号timeout,信号没有（）
        self.timeshow.timeout.connect(self.show_cameradata)
        #self.timeshow.timeout().connect(self.show_cameradata)
        # self.show_cameradata()


    #并处作为摄像头，获取数据，显示画面的功能
    #并只要能够不断重复调用这个函数，不断的从摄像头获取数据进行显示
    #可以通过信号， 信号关联当前函数。只要信号产生，函数就会被调用
    #信号需要不断的产生，可以通过定时器，定时时间到达就会产生信号
    def show_cameradata(self):
        #获取摄像头数据，转换数据
        pic = self.cameravideo.camera_to_pic()
        #显示数据，显示画面
        self.label.setPixmap(pic)

    def get_accesstoken(self):
        print("get_accesstoken")

        #host对象是字符串对象存储是授权的服务地址-----获取accesstoken的地址
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=1cFzLl7ZshdilAAMZnnyX4Ak&client_secret=2OgXkKUAPSEQzQmnkj88LGGoj71Kk3Tj'
        #发送网络请求   requests网络库
        #使用get函数发送网络请求，参数为网络请求的地址，执行时会产生返回结果，结果就是请求的结果
        response = requests.get(host)
        if response:
            # print(response.json())
            data = response.json()
            self.access_token = data.get('access_token')
            print(self.access_token)

    def get_face(self):
        #获取一张图片（一帧画面）
        #getOpenFileName通过对话框的形式获取一个图片（.JPG）路径
        path,ret = QFileDialog.getOpenFileName(self,"open picture",".","图片格式(*.jpg)")
        #把图片转换成base64编码格式
        fp = open(path,'rb')
        base64_imag = base64.b64encode(fp.read())
        print(base64_imag)
        #发送请求的地址
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        #请求参数是一个字典，在字典中存储,百度AI要识别的图片信息，属性内容
        params = {
            "image":base64_imag,#图片信息字符串
            "image_type":"BASE64",#图片信息格式
            "face_field":"gender,age,beauty"#请求识别人脸的属性， 各个属性在字符串中用,逗号隔开
        }

        #访问令牌
        access_token = self.access_token
        #把请求地址和访问令牌组成可用的网络请求
        request_url = request_url + "?access_token=" + access_token
        #参数：设置请求的格式体
        headers = {'content-type': 'application/json'}
        #发送网络post请求,请求百度AI进行人脸检测,返回检测结果
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            data = response.json()
            if data['error_msg'] == 'SUCCESS' :
                age = data['result']['face_list'][0]['age']
                beauty = data['result']['face_list'][0]['beauty']
                print(age)
                print(beauty)