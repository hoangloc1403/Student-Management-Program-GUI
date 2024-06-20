
import wx
import wx.xrc

from Giao_dien.gd_Bai73_Khoa import *
from Giao_dien.gd_Bai72_MonHoc import *
from Giao_dien.gd_Bai74_SinhVien import *
from Giao_dien.gd_Bai75_Tracuu_ThongTin_SV import *
from Giao_dien.gd_Bai76_Tracuu_SV_Khoa import *
from Giao_dien.gd_Bai77_Tracuu_Ketqua import *
from Giao_dien.gd_Bai78_DoiMatKhau import *

from Thu_vien.KetQua import *
from Thu_vien.Khoa import *
from Thu_vien.tv_chung import *
from Thu_vien.NhanVien import *


class FrameQLSV ( wx.MDIParentFrame ):

	def __init__( self, parent,Ma_dang_nhap ):
		self.Ma_dang_nhap = Ma_dang_nhap
		wx.MDIParentFrame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Chương trình Quản Lý Sinh Viên", pos = wx.DefaultPosition, size = wx.Size( 588,303 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.mHeThong = wx.Menu()
		self.subDoiMatKhau = wx.MenuItem( self.mHeThong, wx.ID_ANY, u"Đổi mật khẩu", wx.EmptyString, wx.ITEM_NORMAL )
		self.mHeThong.Append( self.subDoiMatKhau )

		self.mHeThong.AppendSeparator()

		self.subThoat = wx.MenuItem( self.mHeThong, wx.ID_ANY, u"Thoát"+ u"\t" + u"Ctrl+T", wx.EmptyString, wx.ITEM_NORMAL )
		self.mHeThong.Append( self.subThoat )

		self.m_menubar1.Append( self.mHeThong, u"Hệ Thống" )

		self.mDanhMuc = wx.Menu()
		self.subKhoa = wx.MenuItem( self.mDanhMuc, wx.ID_ANY, u"Khoa", wx.EmptyString, wx.ITEM_NORMAL )
		self.mDanhMuc.Append( self.subKhoa )

		self.subMonHoc = wx.MenuItem( self.mDanhMuc, wx.ID_ANY, u"Môn Học", wx.EmptyString, wx.ITEM_NORMAL )
		self.mDanhMuc.Append( self.subMonHoc )

		self.subSinhVien = wx.MenuItem( self.mDanhMuc, wx.ID_ANY, u"Sinh Viên", wx.EmptyString, wx.ITEM_NORMAL )
		self.mDanhMuc.Append( self.subSinhVien )

		self.m_menubar1.Append( self.mDanhMuc, u"Danh Mục" )

		self.mTraCuu = wx.Menu()
		self.subTracuu_Sinhvien = wx.MenuItem( self.mTraCuu, wx.ID_ANY, u"Tra cứu sinh viên", wx.EmptyString, wx.ITEM_NORMAL )
		self.mTraCuu.Append( self.subTracuu_Sinhvien )

		self.subTracuu_dssv_Khoa = wx.MenuItem( self.mTraCuu, wx.ID_ANY, u"Tra cứu dssv Khoa", wx.EmptyString, wx.ITEM_NORMAL )
		self.mTraCuu.Append( self.subTracuu_dssv_Khoa )

		self.subTracuu_Ketqua = wx.MenuItem( self.mTraCuu, wx.ID_ANY, u"Tra cứu kết quả", wx.EmptyString, wx.ITEM_NORMAL )
		self.mTraCuu.Append( self.subTracuu_Ketqua )

		self.m_menubar1.Append( self.mTraCuu, u"Tra Cứu" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose_Frame )
		self.Bind( wx.EVT_MENU, self.Chon_DMK, id = self.subDoiMatKhau.GetId() )
		self.Bind( wx.EVT_MENU, self.Chon_Thoat, id = self.subThoat.GetId() )
		self.Bind( wx.EVT_MENU, self.ChonKhoa, id = self.subKhoa.GetId() )
		self.Bind( wx.EVT_MENU, self.ChonMonHoc, id = self.subMonHoc.GetId() )
		self.Bind( wx.EVT_MENU, self.ChonSinhVien, id = self.subSinhVien.GetId() )
		self.Bind( wx.EVT_MENU, self.Chon_tcSinhVien, id = self.subTracuu_Sinhvien.GetId() )
		self.Bind( wx.EVT_MENU, self.Chon_tcKhoa, id = self.subTracuu_dssv_Khoa.GetId() )
		self.Bind( wx.EVT_MENU, self.Chon_tcKetqua, id = self.subTracuu_Ketqua.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def kiemtra_cuasocon(self,idCS):
		ds_children = self.GetChildren()
		for children in ds_children:
			if children.GetId() ==  idCS:
				children.Activate()
				return True
		return False
	def OnClose_Frame( self, event ):
		dial = wx.MessageDialog(None,"Bạn có muốn thoát không?","Thông báo",wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			self.Destroy()
		else:
			event.Veto()

	def Chon_DMK( self, event ):
		if self.kiemtra_cuasocon(7):
			return
		app = wx.App()
		frame = wx.Frame(self,id = 7,title = "Bài 7.8 - Đổi mật khẩu", size =(400,250), pos=(500,200))
		panel = Panel_78_DoiMatKhau(frame)

		frame.Show()
		app.MainLoop()

	def Chon_Thoat( self, event ):
		self.Destroy()

	def ChonKhoa( self, event ):
		if self.kiemtra_cuasocon(1):
			return
		app = wx.App()
		frame = wx.MDIChildFrame(self,id=1,title = "Bài 7.3 - Khoa", size =(500,250), pos=(500,200))
		panel = Panel_73_Khoa(frame)
		frame.Show()
		app.MainLoop()
	def ChonMonHoc( self, event ):
		if self.kiemtra_cuasocon(2):
			return
		app = wx.App()
		frame = wx.MDIChildFrame(self,id=2,title = "Bài 7.2 - Môn học", size =(500,250), pos=(500,200))
		panel = Panel_72_MonHoc(frame)

		frame.Show()
		app.MainLoop()

	def ChonSinhVien( self, event ):
		if self.kiemtra_cuasocon(3):
			return
		app = wx.App()
		frame = wx.MDIChildFrame(self,id=3,title = "Bài 7.4 - SinhVien", size =(550,370), pos=(500,150))

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

	def Chon_tcSinhVien( self, event ):
		if self.kiemtra_cuasocon(4):
			return
		app = wx.App()
		frame = wx.MDIChildFrame(self,id=4,title = "Bài 7.5 - Tra cứu thông tin Sinh viên ", size =(550,300), pos=(450,200))
		panel = Panel_75_Tracuu_ThongTin_SV(frame)

		frame.Show()
		app.MainLoop()

	def Chon_tcKhoa( self, event ):
		if self.kiemtra_cuasocon(5):
			return
		app = wx.App()
		frame = wx.MDIChildFrame(self,id =5,title = "Bài 7.6 - Tra cứu Sinh viên theo khoa ", size =(800,500), pos=(240,150))
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

	def Chon_tcKetqua( self, event ):
		if self.kiemtra_cuasocon(6):
			return
		app = wx.App()
		frame = wx.MDIChildFrame(self,id =6,title = "Bài 7.7 - Tra cứu kết quả", size =(720,560), pos=(400,100))
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


