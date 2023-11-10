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

```
	import pyautogui as pag
	
	pag.size()				# 获取屏幕尺寸
	Size(width=1918, height=918)
	
	pag.position()			# 获取鼠标当前位置
	Point(x=102, y=92)
	
	pag.onScreen(100,200)	# 判断
	True

```



## 2.2 鼠标控制



## 2.3 键盘控制



## 2.4 消息窗口



## 2.5 截图