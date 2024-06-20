import wx
from Giao_dien.gd_Bai78_DoiMatKhau import *

app = wx.App()
frame = wx.Frame(None,title = "Bài 7.8 - Đổi mật khẩu", size =(400,250), pos=(500,200))
panel = Panel_78_DoiMatKhau(frame)

frame.Show()
app.MainLoop()