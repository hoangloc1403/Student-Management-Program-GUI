
import wx
import wx.xrc
from Thu_vien.Database import *
from Thu_vien.tv_chung import *
from Thu_vien.NhanVien import *
from Giao_dien.gd_Main import *


###########################################################################
## Class Panel_71_DangNhap
###########################################################################

class Panel_71_DangNhap ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 460,179 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Thông tin đăng nhập" ), wx.VERTICAL )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gbSizer4.SetMinSize( wx.Size( 300,-1 ) )
		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Mã đăng nhập:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gbSizer4.Add( self.m_staticText2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMaDangNhap = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gbSizer4.Add( self.txtMaDangNhap, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Mật khẩu:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gbSizer4.Add( self.m_staticText4, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMatKhau = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PASSWORD )
		gbSizer4.Add( self.txtMatKhau, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		sbSizer1.Add( gbSizer4, 1, wx.EXPAND, 5 )


		bSizer1.Add( sbSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.btnDongY = wx.Button( self, wx.ID_ANY, u"Đồng ý", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.btnDongY, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), 0, 5 )

		self.btnKhong = wx.Button( self, wx.ID_ANY, u"Không", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.btnKhong, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), 0, 5 )


		bSizer1.Add( gbSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.btnDongY.Bind( wx.EVT_BUTTON, self.Chon_DongY )
		self.btnKhong.Bind( wx.EVT_BUTTON, self.Chon_Khong )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Chon_DongY( self, event ):
		userName = self.txtMaDangNhap.GetValue()
		password = self.txtMatKhau.GetValue()
		if userName!="":
			nhanvien = NhanVien(duong_dan_QLSinhVien)
			nv = nhanvien.Read_nhan_vien(userName)
			if nv!=None:
				if nv[3] == password:
					frame  = self.GetParent()
					frame.Hide()
					frame.Close()
					app = wx.App()
					frame = FrameQLSV(None,userName)
					frame.Show()
					app.MainLoop()
				else:
					wx.MessageBox("Sai mật khẩu","Thông báo",wx.OK|wx.ICON_ERROR)
			else:
				wx.MessageBox("Không có user này","Thông báo",wx.OK|wx.ICON_ERROR)
		else:
			wx.MessageBox("Vui lòng nhập Mã","Thông báo",wx.OK|wx.ICON_ERROR)

	def Chon_Khong( self, event ):
		self.GetParent().Close()


