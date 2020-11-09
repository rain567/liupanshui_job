from aip import AipBodyAnalysis
import cv2 as cv
def fanHuiTuPianGuanDianX_Y(url):  #从百度AI获取到图片关键点返回值，参数为图片路径
    """ 你的 APPID AK SK """
    APP_ID = '22952436'
    API_KEY = 'a5UrzVfjQHyuK0GSCXk8QoQH'
    SECRET_KEY = '8wguEEmbNTnMfAOOOigMr1cM1SZXvq1c'

    client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(url)

    """ 调用人体关键点识别 """
    ret=client.bodyAnalysis(image)

    return ret

def shuJuChuLi(data):#处理百度AI返回的数据，返回一个列表包含坐标，参数为百度AI返回的数据

    len=data['person_num']
    print('图片中人数',len)
    X_Y=[]
    for value in data['person_info']:
       for key,val in value["body_parts"].items():
           y=int(val['y'])
           x=int(val['x'])
           X_Y.append((x,y))
    return X_Y
def huadian(url,xy):#给图片标点并显示出来，参数1为图片路径，参数2为，坐标列表
    img = cv.imread(url)
    point_size = 1
    point_color = (133, 133, 0)  # BGR
    thickness = 4  # 可以为 0 、4、8
    for point in xy:
        cv.circle(img, point, point_size, point_color, thickness)
    cv.namedWindow("image")
    cv.imshow('image', img)
    cv.waitKey(10000)  # 显示 10000 ms 即 10s 后消失
    cv.destroyAllWindows()
if __name__ == '__main__':

    ret=fanHuiTuPianGuanDianX_Y('1.jpg')
    xy=shuJuChuLi(ret)
    huadian('1.jpg', xy)
