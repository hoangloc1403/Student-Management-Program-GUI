import wx
from Giao_dien.gd_Bai71_DangNhap import *

app = wx.App()
frame = wx.Frame(None,title = "Bài 7.1 - Đăng nhập", size =(500,200), pos=(500,200))
panel = Panel_71_DangNhap(frame)

frame.Show()
app.MainLoop()