#!/bin/python3

import pyautogui as pag

class AutoGUI(object):
    def __init__(self):
        # 保存屏幕尺寸
        self.sizex, self.sizey = pag.size()

        self.show_generic_api()

        self.show_mouse_api()
        

    def show_generic_api(self):
        print('------------------ generic start ------------------')
        # 获取屏幕尺寸
        print(pag.size(), end='\n\n')

        # 获取鼠标当前位置
        print(pag.position(), end='\n\n')

        # 判断坐标(100,200)是否在屏幕内
        print(pag.onScreen(100,200), end='\n\n')

        # 所有pyautogui指令暂停一秒
        pag.PAUSE = 1


    def show_mouse_api(self):
        print('------------------ mouse start --------------------')
        # 绝对位置移动至正中心
        pag.moveTo(self.sizex/2, self.sizey/2 ,duration=1)
        print(pag.position(), end='\n\n')
        
        # 相对位置移动
        pag.moveRel(100, -200, duration=0.5)
        print(pag.position(), end='\n\n')

        # 移至屏幕中心点左键
        pag.click(self.sizex/2, self.sizey/2, duration=0.5)

        # 当前位置点右键
        pag.click(button='right', duration=1)

        # 移动至(100,100)点击3次左键，点击间隔0.1s，鼠标移动过渡时间0.5秒
        pag.click(100, 100, clicks=3, interval=0.1, duration=0.5)

        # 移至(100,100)点击2次右键，点击间隔0.5s，鼠标移动过渡时间0.2
        pag.click(100,100,clicks=2,interval=0.5,button='right',duration=0.2)

        # 单击中键
        pag.click(1000, 300,button='middle')

        # 指定位置，双击左键
        pag.doubleClick(10,10)

        # 指定位置，双击右键
        pag.rightClick(10,10)

        # 指定位置，双击中键
        pag.middleClick(10,10)

        # 鼠标位置不动，向上回滚2个单位
        pag.scroll(2)

        # 鼠标移动至(1000,700)，前下滚动10个单位
        pag.scroll(-10,1000,700)

        # 鼠标按下
        pag.mouseDown()

        # 鼠标释放
        pag.mouseUp()

        # 将鼠标从当前位置拖至屏幕中心，默认左键
        pag.dragTo(self.sizex/2, self.sizey/2)

        # 将鼠标从当前位置向左100像素、向右200像素拖动，过渡时间0.5秒，指定右键
        pag.dragRel(-100,200,duration=0.5,button='right')

        # 得到当前鼠标位置；输出：Point(x=1414, y=129)
        print(pag.position())

        # 按字母A键，字母支持大小写
        pag.press('a')

        # 传入键名列表（按键p、按键y、空格），按键之间间隔0.1秒（默认0）
        pag.press(['p','y','space'], interval=0.1)

if __name__ == '__main__':
    autoGui = AutoGUI()
