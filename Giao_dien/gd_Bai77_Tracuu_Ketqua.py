
import wx
import wx.xrc
from Thu_vien.tv_chung import *
from Thu_vien.SinhVien import *
from Thu_vien.Khoa import *
from Thu_vien.KetQua import *

class Panel_77_Tracuu ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 708,494 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nhập thông tin tra cứu" ), wx.VERTICAL )

		gbSizer9 = wx.GridBagSizer( 0, 0 )
		gbSizer9.SetFlexibleDirection( wx.BOTH )
		gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.txtMa = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		gbSizer9.Add( self.txtMa, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Tên:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		gbSizer9.Add( self.m_staticText30, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtTen = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		gbSizer9.Add( self.txtTen, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Chọn khoa:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		gbSizer9.Add( self.m_staticText31, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		chDsKhoaChoices = []
		self.chDsKhoa = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 220,-1 ), chDsKhoaChoices, 0 )
		self.chDsKhoa.SetSelection( 0 )
		gbSizer9.Add( self.chDsKhoa, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Mã:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		gbSizer9.Add( self.m_staticText29, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btnTracuu = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Tra cứu", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.btnTracuu, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		sbSizer2.Add( gbSizer9, 1, wx.ALL|wx.EXPAND, 20 )


		bSizer7.Add( sbSizer2, 1, wx.ALL|wx.EXPAND, 30 )

		gbSizer10 = wx.GridBagSizer( 0, 0 )
		gbSizer10.SetFlexibleDirection( wx.BOTH )
		gbSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Kết quả tìm được", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gbSizer10.Add( self.m_staticText32, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.lcrtlDanhsach = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,-1 ), wx.LC_REPORT )
		gbSizer10.Add( self.lcrtlDanhsach, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.btn_Thoat = wx.Button( self, wx.ID_ANY, u"Thoát", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.btn_Thoat, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer7.Add( gbSizer10, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		# Connect Events
		self.btnTracuu.Bind( wx.EVT_BUTTON, self.btnTracuu_OnClick )
		self.btn_Thoat.Bind( wx.EVT_BUTTON, self.btnThoat_OnClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def btnTracuu_OnClick( self, event ):
		self.lcrtlDanhsach.DeleteAllItems()
		sv = SinhVien(duong_dan_QLSinhVien)
		masv = self.txtMa.GetValue()
		tensv = self.txtTen.GetValue()
		khoa = Khoa(duong_dan_QLSinhVien)
		item = self.chDsKhoa.GetSelection()
		ten_khoa = self.chDsKhoa.GetString(item)
		khoa_id = khoa.Read_ID_tu_ten_khoa(ten_khoa)[0]
		dsketqua = sv.Read_ket_qua(masv,tensv,khoa_id)
		if len(dsketqua) > 0:
			index = 0
			for dong in dsketqua:
				self.lcrtlDanhsach.InsertItem(index,dong[0])
				self.lcrtlDanhsach.SetItem(index,1,dong[1])
				self.lcrtlDanhsach.SetItem(index,2,dong[2])
				self.lcrtlDanhsach.SetItem(index,3,dong[3])
				self.lcrtlDanhsach.SetItem(index,4,str(dong[4]))
				self.lcrtlDanhsach.SetItem(index,5,dong[5])
		else:
			wx.MessageBox("Không có kết quả nào thỏa điều kiện", "Thông báo", wx.OK | wx.ICON_INFORMATION)
	def btnThoat_OnClick( self, event ):
		self.GetParent().Close()


