import wx
from Giao_dien.gd_Bai72_MonHoc import *

app = wx.App()
frame = wx.Frame(None,title = "Bài 7.2 - Môn học", size =(500,250), pos=(500,200))
panel = Panel_72_MonHoc(frame)

frame.Show()
app.MainLoop()