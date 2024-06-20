
import wx
import wx.xrc
from Thu_vien.tv_chung import *
from Thu_vien.SinhVien import *
from Thu_vien.Khoa import *
from datetime import *
class Panel_76_Tracuu_SV_Khoa ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 569,433 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Tra cứu sinh viên theo khoa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		self.m_staticText25.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText25.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer6.Add( self.m_staticText25, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gbSizer8 = wx.GridBagSizer( 0, 0 )
		gbSizer8.SetFlexibleDirection( wx.BOTH )
		gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Chọn khoa:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		gbSizer8.Add( self.m_staticText27, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		choiceKhoaChoices = []
		self.choiceKhoa = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,-1 ), choiceKhoaChoices, 0 )
		self.choiceKhoa.SetSelection( 0 )
		gbSizer8.Add( self.choiceKhoa, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.listDS_SV = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,300 ), wx.LC_REPORT )
		gbSizer8.Add( self.listDS_SV, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )


		bSizer6.Add( gbSizer8, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		# Connect Events
		self.choiceKhoa.Bind( wx.EVT_CHOICE, self.choiceKhoa_Selection )

	def __del__( self ):
		pass

	def remove_listCtrl(self):
		self.listDS_SV.DeleteAllItems()
	# Virtual event handlers, override them in your derived class
	def choiceKhoa_Selection( self, event ):
		self.remove_listCtrl()
		khoa = Khoa(duong_dan_QLSinhVien)
		item = self.choiceKhoa.GetSelection()
		ten_khoa = self.choiceKhoa.GetString(item)
		khoa_id = khoa.Read_ID_tu_ten_khoa(ten_khoa)[0]
		sv = SinhVien(duong_dan_QLSinhVien)
		kq = sv.Read_danh_sach_sinh_vien_khoa(khoa_id)

		if len(kq)>0:
			index =0
			for dong in kq:
				self.listDS_SV.InsertItem(index,dong[1])
				self.listDS_SV.SetItem(index,1,dong[2])
				self.listDS_SV.SetItem(index,2,dong[3])
				self.listDS_SV.SetItem(index,3,"Nam" if dong[4] else "Nữ")
				ns = dong[5].split("/")
				ngay = ""
				if len(ns) == 3:
					ngay = datetime(int(ns[2]),int(ns[0]),int(ns[1])).strftime("%d/%m/%Y")
				self.listDS_SV.SetItem(index,4,ngay)
				self.listDS_SV.SetItem(index,5,"{:,}".format(dong[9]))

				


