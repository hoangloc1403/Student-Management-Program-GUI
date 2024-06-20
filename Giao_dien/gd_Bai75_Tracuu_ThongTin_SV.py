import wx
import wx.xrc
from datetime import datetime
from Thu_vien.tv_chung import *
from Thu_vien.SinhVien import *
# from Thu_vien.Khoa import *

class Panel_75_Tracuu_ThongTin_SV ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 599,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Tra cứu thông tin sinh viên\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer5.Add( self.m_staticText21, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Nhập mã sinh viên:", wx.Point( -1,10000 ), wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gbSizer7.Add( self.m_staticText22, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMaSV = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 190,-1 ), 0 )
		gbSizer7.Add( self.txtMaSV, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Tra cứu", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_button11, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"[Thông tin chi tiết sinh viên]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		self.m_staticText23.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText23.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		gbSizer7.Add( self.m_staticText23, wx.GBPosition( 1, 1 ), wx.GBSpan( 3, 1 ), wx.ALL, 5 )


		bSizer5.Add( gbSizer7, 1, wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.btnTracuu_OnClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def btnTracuu_OnClick( self, event ):
		maso = self.txtMaSV.GetValue()
		if maso!="":
			sv = SinhVien(duong_dan_QLSinhVien)
			kq = sv.Read_sinh_vien_Tenkhoa(maso)
			if kq!=None:
				gt = "Nam" if kq[4] else "Nữ"
				mangngay = kq[5].split("/")
				ngaysinh = datetime(int(mangngay[2]),int(mangngay[0]),int(mangngay[1])).strftime("%d/%m/%Y")
				chuoi = f"- Mã: {kq[1]}\n- Họ tên: {kq[2]} {kq[3]}\n- Ngày sinh: {ngaysinh} - {gt}\n- Học bổng: {kq[9]:,}\n- Khoa: {kq[11]}"
				self.m_staticText23.SetLabel(chuoi)
			else:
				wx.MessageBox("Không có sinh viên này", "Thông báo", wx.OK | wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Chưa nhập mã số", "Thông báo", wx.OK | wx.ICON_ERROR)
			


