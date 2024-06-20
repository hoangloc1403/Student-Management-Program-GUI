import wx
from Giao_dien.gd_Bai73_Khoa import *

app = wx.App()
frame = wx.Frame(None,title = "Bài 7.3 - Khoa", size =(500,250), pos=(500,200))
panel = Panel_73_Khoa(frame)

frame.Show()
app.MainLoop()