# 目录

[TOC]

<div STYLE="page-break-after: always;"></div>

# 一、PyAutoGUI简介与模块的安装

​		web上进行自动化操作可以使用Selenium，GUI 界面自动化操作可以使用PyAotuGUI模块。其中pyautogui模块是模拟键盘、鼠标在界面上操作。pyautogui是跨平台的，模块的函数主要分成通用功能、鼠标控制、键盘控制、消息窗口、截图5大类。

​		而pywin32模块包含windows的所有API，windows的API又分为win32api、win32gui、win32com。

​		安装方法：

```shell
		pip install pyautogui
```



# 二、函数及用法

## 2.1 通用功能

```python
	import pyautogui as pag
	
	pag.size()				# 获取屏幕尺寸
	Size(width=1918, height=918)
	
	pag.position()			# 获取鼠标当前位置
	Point(x=102, y=92)
	
	pag.onScreen(100,200)	# 判断坐标是否在屏幕范围内
	True
    
    # 默认这项功能为True, 这项功能意味着：当鼠标的指针在屏幕的最坐上方，程序会报错；目的是为了防止程序无法停止
	pag.FAILSAFE =False

    # 意味着所有pyautogui的指令都要暂停一秒；其他指令不会停顿；这样做，可以防止键盘鼠标操作太快；
	pag.PAUSE = 1
```



## 2.2 鼠标控制

### 2.2.1 鼠标移动

```python
	# 保存屏幕尺寸
	sizex,sizey = pag.size()

	# 绝对位置移动，移动至屏幕正中心，鼠标移动过渡时间duration设为1秒
	pag.moveTo(sizex/2,sizey/2,duration=1)

	# 相对位置移动，向右100、向上200，鼠标移动过渡时间duration设为0.5秒
	pag.moveRel(100, -200, duration=0.5)
```

### 2.2.2 鼠标点击

```python
	# 移动至屏幕中心点击一下左键，过渡时间0.5秒
	pag.click(sizex/2,sizey/2, duration=0.5)

	# 不指定x、y，在当前位置点击一下右键
	pag.click(button='right')

	# 移动至(100,100)点击3次左键，点击间隔0.1s，鼠标移动过渡时间0.5秒
	pag.click(100,100, clicks=3,interval=0.1,duration=0.5)

	# 移动至(100,100)点击2次右键，点击间隔0.5s，鼠标移动过渡时间0.2秒
	pag.click(100,100, clicks=2,interval=0.5,button='right',duration=0.2)
    
    # 单击中间
    pag.click(1000,300,button='middle')
    
    pag.doubleClick(10,10)  # 指定位置，双击左键
    pag.rightClick(10,10)   # 指定位置，双击右键
    pag.middleClick(10,10)  # 指定位置，双击中键
```

### 2.2.3 鼠标滚轮滚动

```python
	# 鼠标位置不动，向上回滚2个单位，项目文档对滚动量参数说明不详
	pag.scroll(2)

	# 鼠标移动至(1000,700)，前下滚动10个单位
	# 运行发现鼠标并没有动
	pag.scroll(-10,1000,700)
```

### 2.2.4 鼠标拖拽

​		从当前位置按下鼠标，移动至目标位置再释放的过程

```python
	pag.mouseDown()   	# 鼠标按下
	pag.mouseUp()    	# 鼠标释放
    
    # 将鼠标从当前位置拖至屏幕中心，默认左键
	pag.dragTo(sizex/2,sizey/2)

	# 将鼠标从当前位置向左100像素、向右200像素拖动，过渡时间0.5秒，指定右键
	pag.dragRel(-100,200,duration=0.5,button='right')
```

### 2.2.4 鼠标位置

```python
	# 得到当前鼠标位置；输出：Point(x=1414, y=129)
	print(pag.position())
```



## 2.3 键盘控制

```python
	pag.keyDown('shift')    # 按下shift
    pag.press('4')    		# 按下 4
    pag.keyUp('shift')   	# 释放 shift
    
    # 键名用字符串表示，支持的所有键名，存在pyautogui.KEYBOARD_KEYS变量中，包括26个字母、数字、符号、F1~F20、方向等等所有按键
	pag.press('a') # 按字母A键，字母支持大小写
	# 程序向终端输入了字符a，若程序运行时输入法为中文状态，由于没有继续输入空格或回车，输入法仅列出候选字，并不会输入到终端
	a 

	# 传入键名列表（按键p、按键y、空格），按键之间间隔0.1秒（默认0）
	pag.press(['p','y','space'], interval=0.1)
	# 运行前将输入法切换到中文状态，往终端直接输入了“培养”
	培养

    # typewrite方式一：传入字符串，不支持中文字符，因为函数无法知道输入法需要什么按键才能得到中文字符
	pag.typewrite('hello, PyAutoGUI!\n')
    # 程序把字符串"'hello, PyAutoGUI!"和换行符输入到了终端
	hello, PyAutoGUI!

	# typewrite方式二：传入键名列表，按键之间间隔0.1秒（默认0）
	pag.typewrite(['s','r','f','space'], interval=0.1)
	# 运行前将输入法切换到中文状态，往终端直接输入了“输入法”3个字
	输入法

	# 大小写字母是自动支持的，仍然尝试一次切换到大写
	pag.typewrite(['capslock','p','y'])
	# CapsLock按键灯被点亮，程序往终端输入了"PY"
	PY

	# hotkey屏蔽了需要反复keyDown、keyUp的细节，参数是任意个键名，而非列表
	pag.hotkey('ctrl', 'shift', 'esc') #调出任务管理器
	pag.hotkey('alt','ctrl','delete') # 并未调出重启界面
```

​		**特殊按键**

| 键盘字符串                      | 说明                             |
| :------------------------------ | :------------------------------- |
| enter（或 return 或 \n）        | 回车                             |
| esc                             | ESC键                            |
| shiftleft，shiftright           | 左右SHIFT键                      |
| altleft，altright               | 左右ALT键                        |
| ctrlleft，ctrlright             | 左右CTRL键                       |
| tab（或 \t）                    | TAB键                            |
| backspace，delete               | BACKSPACE，DELETE键              |
| pageup，pagedown                | PAGE UP，PAGE DOWN键             |
| home，end                       | HOME，END键                      |
| up，down，left，right           | 箭头键                           |
| f1，f2，...，f12                | F1......F12键                    |
| volumemute, volumedown,volumeup | 声音变大变小静音（有些键盘没有） |
| pause                           | PAUSE键，暂停键                  |
| capslock                        | CAPS LOCK 键                     |
| numlock                         | NUM LOCK 键                      |
| scrolllock                      | SCROLLLOCK 键                    |
| insert                          | INSERT键                         |
| printscreen                     | PRINT SCREEN键                   |
| winleft, winright               | Win键（windows ）                |
| command                         | command键（Mac OS X ）           |
| option                          | option（Mac OS X）               |



## 2.4 消息窗口

```python
	pag.alert(text='警告',title='PyAutoGUI消息框',button='OK')
	'OK' # 点击的按键被返回

	pag.confirm(text='请选择',title='PyAutoGUI消息框',buttons=['1','2'...: ,'3'])
	'2' # 点击的按键被返回

	pag.prompt(text='请输入',title='PyAutoGUI消息框',default='请输入')
	'input by 伪码人' # 点OK按钮后返回输入内容

	pag.password(text='输入密码',title='PyAutoGUI消息框',default='',mask='*')
	'We_Coder' # 点OK按钮后返回输入内容
```



## 2.5 截图(不支持wayland)

```python
	# imageFilename参数，截图要保存的文件全路径名，默认`None`，不保存；
	# region参数，截图区域，由左上角坐标、宽度、高度4个值确定，如果指定区域超出了屏幕范围，超出部分会被黑色填充，默认`None`,截全屏
	pag.screenshot('shot.png',region=(1000,600,600,400))
	<PIL.Image.Image image mode=RGB size=600x400 at 0x20C87497390>
```

