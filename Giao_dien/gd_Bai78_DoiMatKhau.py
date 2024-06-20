
import wx
import wx.xrc
from Thu_vien.tv_chung import *
from Thu_vien.NhanVien import *
from Giao_dien.gd_Main import *
class Panel_78_DoiMatKhau ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 454,240 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )
		self.MasoNV = parent.GetParent().Ma_dang_nhap
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Đổi mật khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer8.Add( self.m_staticText30, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gbSizer11 = wx.GridBagSizer( 0, 0 )
		gbSizer11.SetFlexibleDirection( wx.BOTH )
		gbSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Mật khẩu cũ:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gbSizer11.Add( self.m_staticText31, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMatkhau_old = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD)
		gbSizer11.Add( self.txtMatkhau_old, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Mật khẩu mới:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gbSizer11.Add( self.m_staticText33, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMatkhau_new = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD)
		gbSizer11.Add( self.txtMatkhau_new, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btnThucHien = wx.Button( self, wx.ID_ANY, u"Đổi mật khẩu", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		gbSizer11.Add( self.btnThucHien, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer8.Add( gbSizer11, 1, wx.ALL|wx.EXPAND, 20 )


		self.SetSizer( bSizer8 )
		self.Layout()

		# Connect Events
		self.btnThucHien.Bind( wx.EVT_BUTTON, self.btnDoiMatKhau_OnClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def btnDoiMatKhau_OnClick( self, event ):
		user = self.MasoNV
		matkhau_old = self.txtMatkhau_old.GetValue()
		matkhau_new = self.txtMatkhau_new.GetValue()
		if matkhau_old.strip()=="" or matkhau_new.strip()=="":
			wx.MessageBox("Chưa nhập thông tin", "Thông báo", wx.OK | wx.ICON_ERROR)
			return
		nv = NhanVien(duong_dan_QLSinhVien)
		nhanvien = nv.Read_nhan_vien(user)
		if nhanvien[3] == matkhau_old:
			kq = nv.Update_mat_khau_moi(matkhau_new,user)
			if kq!=0:
				wx.MessageBox("Cập nhật mật khẩu thành công", "Thông báo", wx.OK | wx.ICON_INFORMATION)
				self.GetParent().Close()
			else:
				wx.MessageBox("Cập nhật không mật khẩu thành công", "Thông báo", wx.OK | wx.ICON_ERROR)
		else:
			self.txtMatkhau_old.SetFocus()
			wx.MessageBox("Mật khẩu cũ không đúng", "Thông báo", wx.OK | wx.ICON_ERROR)
            
				
				



