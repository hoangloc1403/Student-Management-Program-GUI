
import wx
import wx.xrc
from datetime import datetime
from Thu_vien.tv_chung import *
from Thu_vien.SinhVien import *
from Thu_vien.Khoa import *
from Thu_vien.KetQua import *

class Panel_74_SinhVien ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 576,376 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"CẬP NHẬT SINH VIÊN", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer4.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Mã SV:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText11.Wrap( -1 )

		gbSizer5.Add( self.m_staticText11, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMaSV = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		gbSizer5.Add( self.txtMaSV, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Họ:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText12.Wrap( -1 )

		gbSizer5.Add( self.m_staticText12, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtHo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		gbSizer5.Add( self.txtHo, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Tên:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gbSizer5.Add( self.m_staticText13, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtTen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		gbSizer5.Add( self.txtTen, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Ngày sinh:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		gbSizer7.Add( self.m_staticText14, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtNgay = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		gbSizer7.Add( self.txtNgay, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gbSizer7.Add( self.m_staticText15, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.spThang = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.SP_ARROW_KEYS, 1, 12, 1 )
		gbSizer7.Add( self.spThang, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		gbSizer7.Add( self.m_staticText17, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.spNam = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.SP_ARROW_KEYS, 0, 2025, 1900 )
		gbSizer7.Add( self.spNam, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		gbSizer5.Add( gbSizer7, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 6 ), 0, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Giới tính:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gbSizer5.Add( self.m_staticText18, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.chkGioiTinh = wx.CheckBox( self, wx.ID_ANY, u"Nam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chkGioiTinh.SetValue(True)
		gbSizer5.Add( self.chkGioiTinh, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Khoa:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		gbSizer5.Add( self.m_staticText19, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		cmbDsKhoaChoices = []
		self.cmbDsKhoa = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), cmbDsKhoaChoices, 0 )
		gbSizer5.Add( self.cmbDsKhoa, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Email:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		gbSizer5.Add( self.m_staticText21, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		gbSizer5.Add( self.txtMail, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Học bổng:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		gbSizer5.Add( self.m_staticText22, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtHocBong = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		gbSizer5.Add( self.txtHocBong, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.m_button9, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btnXoa = wx.Button( self, wx.ID_ANY, u"Xóa", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.btnXoa, wx.GBPosition( 7, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer4.Add( gbSizer5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.chkGioiTinh.Bind( wx.EVT_CHECKBOX, self.OnChecked_GioiTinh )
		self.cmbDsKhoa.Bind( wx.EVT_COMBOBOX, self.OnComboBox )
		self.m_button9.Bind( wx.EVT_BUTTON, self.OnCliCkThem )
		self.btnXoa.Bind( wx.EVT_BUTTON, self.OnCliCkXoa )

	def __del__( self ):
		pass

	# Virtual event handlers, override them in your derived class
	def OnChecked_GioiTinh( self, event ):
		cb = self.chkGioiTinh.GetValue()
		label = "Nam" if cb ==True else "Nữ"
		self.chkGioiTinh.SetLabel( label )
	def OnComboBox( self, event ):
		khoa = Khoa(duong_dan_QLSinhVien)
		ten_khoa = self.cmbDsKhoa.GetValue()
		id_khoa = khoa.Read_ID_tu_ten_khoa(ten_khoa)[0]
		return id_khoa
	def is_valid_date(self,year, month, day):
		if month < 1 or month > 12:
			return False
		
		if month in [1, 3, 5, 7, 8, 10, 12]:
			return 1 <= day <= 31
		elif month in [4, 6, 9, 11]:
			return 1 <= day <= 30
		elif month == 2:
			if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # Năm nhuận
				return 1 <= day <= 29
			else:
				return 1 <= day <= 28
		else:
			return False

	def OnCliCkThem(self, event):
		ma_sv = self.txtMaSV.GetValue()
		ho = self.txtHo.GetValue()
		ten = self.txtTen.GetValue()
		if ma_sv == "" or ho == "" or ten == "":
			wx.MessageBox("Bạn chưa nhập thông tin", "Thông báo", wx.OK | wx.ICON_ERROR)
			self.txtMaSV.SetFocus()
			return
		try: 
			day = int(self.txtNgay.GetValue())
		except ValueError:
			wx.MessageBox("Ngày sinh không hợp lệ", "Thông báo", wx.OK | wx.ICON_ERROR)
			return
		month = self.spThang.GetValue()
		year = self.spNam.GetValue()
		if not self.is_valid_date(year, month, day):
			wx.MessageBox("Ngày tháng năm không hợp lệ", "Thông báo", wx.OK | wx.ICON_ERROR)
			return

		# try:
		ngay_sinh = datetime(year, month, day)
		# except ValueError:
		# 	wx.MessageBox("Ngày sinh không hợp lệ", "Thông báo", wx.OK | wx.ICON_ERROR)
		# 	return

		gioi_tinh = self.chkGioiTinh.GetValue()
		ma_khoa = self.OnComboBox(self)  
		mail = self.txtMail.GetValue()
		hocbong = self.txtHocBong.GetValue() if self.txtHocBong.GetValue() != "" else "0"
		
		try:
			int(hocbong)
		except ValueError:
			wx.MessageBox("Học bổng không hợp lệ", "Thông báo", wx.OK | wx.ICON_ERROR)
			return
		sinhvien = SinhVien(duong_dan_QLSinhVien)
		kq = sinhvien.Add_sinh_vien(ma_sv, ho, ten, gioi_tinh, ngay_sinh, mail, "", "", hocbong, ma_khoa)
		
		if kq != 0:
			self.txtMaSV.SetValue("")
			self.txtHo.SetValue("")
			self.txtTen.SetValue("")
			self.txtNgay.SetValue("")
			self.spThang.SetValue(1)
			self.spNam.SetValue(1900)
			self.chkGioiTinh.SetValue(True)
			# self.cmbDsKhoa.SetValue("CN")
			self.txtMail.SetValue("")
			self.txtHocBong.SetValue("0")
			wx.MessageBox("Thêm thông tin thành công", "Thông báo", wx.OK | wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Sinh viên đã tồn tại", "Thông báo", wx.OK | wx.ICON_ERROR)

	def OnCliCkXoa( self, event ):
		tl = wx.MessageBox("Bạn có muốn xóa?","Thông báo",wx.YES_NO | wx.ICON_QUESTION)
		sinhvien = SinhVien(duong_dan_QLSinhVien)
		ma_sv = self.txtMaSV.GetValue()
		if ma_sv == "":
			wx.MessageBox("Bạn chưa nhập mã sinh viên","Thông báo",wx.OK|wx.ICON_ERROR)
			self.txtMaSV.SetFocus()
			return
		kq = sinhvien.Read_sinh_vien(ma_sv)
		if kq!=None:
			idsv = kq[0]
			ketqua = KetQua(duong_dan_QLSinhVien)
			dskq = ketqua.Read_danh_sach_ket_qua_theo_SinhVienID(idsv)
			if len(dskq) == 0:
				dem= sinhvien.Delete_sinh_vien(ma_sv)
				if dem>0:
					wx.MessageBox("Xóa sinh vien thành công", "Thông báo", wx.OK | wx.ICON_INFORMATION)
				else:
					wx.MessageBox("Xóa sinh vien không thành công", "Thông báo", wx.OK | wx.ICON_ERROR)
			else:
				wx.MessageBox("Đã có bảng điểm của sinh viên này, không thể xóa", "Thông báo", wx.OK | wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Không có sinh viên này", "Thông báo", wx.OK | wx.ICON_INFORMATION)


					



