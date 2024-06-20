
import wx
import wx.xrc
from Thu_vien.tv_chung import *
from Thu_vien.Khoa import *

class Panel_73_Khoa ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 617,218 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"CẬP NHẬT KHOA", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer2.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Mã khoa:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gbSizer5.Add( self.m_staticText8, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Tên khoa:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gbSizer5.Add( self.m_staticText9, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtTenKhoa = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gbSizer5.Add( self.txtTenKhoa, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMaKhoa = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gbSizer5.Add( self.txtMaKhoa, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btnThem = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		gbSizer5.Add( self.btnThem, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 15 )

		self.btnTim = wx.Button( self, wx.ID_ANY, u"Tìm", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.btnTim, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 15 )

		self.btnCapNhat = wx.Button( self, wx.ID_ANY, u"Cập nhật", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.btnCapNhat, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 15 )


		bSizer2.Add( gbSizer5, 1, wx.ALIGN_CENTER, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.btnThem.Bind( wx.EVT_BUTTON, self.OnCliCkThem )
		self.btnTim.Bind( wx.EVT_BUTTON, self.OnClickTim )
		self.btnCapNhat.Bind( wx.EVT_BUTTON, self.OnClickCapnhat )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnCliCkThem( self, event ):
		ma_khoa = self.txtMaKhoa.GetValue()
		ten = self.txtTenKhoa.GetValue()
		if ten == " " or ma_khoa == "":
			wx.MessageBox("Bạn chưa nhập thông tin","Thông báo",wx.OK|wx.ICON_ERROR)
			self.txtMaKhoa.SetFocus()
			return
		khoa = Khoa(duong_dan_QLSinhVien)
		kq = khoa.Add_Khoa(ma_khoa,ten)
		if kq != 0:
			self.txtMaKhoa.SetValue("")
			self.txtTenKhoa.SetValue("")
			wx.MessageBox("Thêm thông tin thành công","Thông báo",wx.OK|wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Thêm thông tin thất bại","Thông báo",wx.OK|wx.ICON_ERROR)
	def OnClickTim( self, event ):
		ma_khoa = self.txtMaKhoa.GetValue()
		if ma_khoa == "":
			wx.MessageBox("Bạn chưa nhập thông tin","Thông báo",wx.OK|wx.ICON_ERROR)
			self.txtMaKhoa.SetFocus()
			return
		khoa = Khoa(duong_dan_QLSinhVien)
		kq = khoa.Read_Khoa_maso(ma_khoa)
		if kq!=None:
			self.txtTenKhoa.SetValue(kq[2])
		else:
			wx.MessageBox("Không có khoa này","Thông báo",wx.OK|wx.ICON_INFORMATION)
	def OnClickCapnhat( self, event ):
		ma_khoa = self.txtMaKhoa.GetValue()
		ten = self.txtTenKhoa.GetValue()
		if ten == " " or ma_khoa == "":
			wx.MessageBox("Bạn chưa nhập thông tin","Thông báo",wx.OK|wx.ICON_ERROR)
			self.txtMaKhoa.SetFocus()
			return
		khoa = Khoa(duong_dan_QLSinhVien)
		kq = khoa.Read_Khoa_maso(ma_khoa)
		if kq!=None:
			kq = khoa.Update_khoa(ten,ma_khoa)
			if kq !=0:
				wx.MessageBox("Cập nhật thông tin thành công","Thông báo",wx.OK|wx.ICON_INFORMATION)
			else:
				wx.MessageBox("Cập nhật thông tin thất bại","Thông báo",wx.OK|wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Không có môn học này","Thông báo", wx.OK | wx.ICON_INFORMATION)


