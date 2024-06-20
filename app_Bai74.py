import wx
from Giao_dien.gd_Bai74_SinhVien import *
from Thu_vien.Khoa import *
from Thu_vien.tv_chung import *

app = wx.App()
frame = wx.Frame(None,title = "Bài 7.4 - SinhVien", size =(550,370), pos=(500,150))

khoa = Khoa(duong_dan_QLSinhVien)
ds_khoa= khoa.Read_danh_sach_khoa()
list_khoa= []
for item in ds_khoa:
    list_khoa.append(item[2])

panel = Panel_74_SinhVien(frame)
panel.cmbDsKhoa.Append(list_khoa)
panel.cmbDsKhoa.SetStringSelection(list_khoa[0])
frame.Show()
app.MainLoop()