import wx
from Giao_dien.gd_Bai77_Tracuu_Ketqua import *

app = wx.App()
frame = wx.Frame(None,title = "Bài 7.7 - Tra cứu kết quả", size =(720,560), pos=(400,100))
khoa = Khoa(duong_dan_QLSinhVien)
list_khoa = khoa.Read_ds_tenkhoa()
panel = Panel_77_Tracuu(frame)
panel.chDsKhoa.Append(list_khoa)
panel.chDsKhoa.SetStringSelection(list_khoa[0])

panel.lcrtlDanhsach.InsertColumn(0,'Mã SV',width=70)
panel.lcrtlDanhsach.InsertColumn(1,'Họ',wx.LIST_FORMAT_LEFT,width=150)
panel.lcrtlDanhsach.InsertColumn(2,'Tên',wx.LIST_FORMAT_LEFT,width=70)
panel.lcrtlDanhsach.InsertColumn(3,'Môn học',wx.LIST_FORMAT_LEFT,width=150)
panel.lcrtlDanhsach.InsertColumn(4,'Điểm',wx.LIST_FORMAT_RIGHT,width=70)
panel.lcrtlDanhsach.InsertColumn(5,'Khoa',wx.LIST_ALIGN_LEFT,width=210)   

frame.Show()
app.MainLoop()