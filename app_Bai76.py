import wx
from Giao_dien.gd_Bai76_Tracuu_SV_Khoa import *

app = wx.App()
frame = wx.Frame(None,title = "Bài 7.6 - Tra cứu Sinh viên theo khoa ", size =(800,500), pos=(240,150))
panel = Panel_76_Tracuu_SV_Khoa(frame)
khoa = Khoa(duong_dan_QLSinhVien)
list_khoa = khoa.Read_ds_tenkhoa()
panel.choiceKhoa.Append(list_khoa)
panel.choiceKhoa.SetStringSelection(list_khoa[0])

panel.listDS_SV.InsertColumn(0,'Mã số',width=100)
panel.listDS_SV.InsertColumn(1,'Họ',wx.LIST_FORMAT_LEFT,width=150)
panel.listDS_SV.InsertColumn(2,'Tên',wx.LIST_FORMAT_LEFT,width=100)
panel.listDS_SV.InsertColumn(3,'Giới tính',wx.LIST_FORMAT_LEFT,width=100)
panel.listDS_SV.InsertColumn(4,'Ngày sinh',wx.LIST_FORMAT_RIGHT,width=100)
panel.listDS_SV.InsertColumn(5,'Học bổng',wx.LIST_FORMAT_RIGHT,width=100)   
frame.Show()
app.MainLoop()