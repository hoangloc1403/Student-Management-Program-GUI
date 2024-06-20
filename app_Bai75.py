import wx
from Giao_dien.gd_Bai75_Tracuu_ThongTin_SV import *

app = wx.App()
frame = wx.Frame(None,title = "Bài 7.5 - Tra cứu thông tin Sinh viên ", size =(550,300), pos=(450,200))
panel = Panel_75_Tracuu_ThongTin_SV(frame)

frame.Show()
app.MainLoop()