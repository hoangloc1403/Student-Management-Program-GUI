from Thu_vien.Database import *

class KetQua(Database):
	def __init__(self, path_db):
		Database.__init__(self, path_db)

	#Đọc kết quả của 1 sinh viên theo ID
	def Read_ket_qua(self, id):
		chuoi_sql = "SELECT SinhVienID, MonHocID, Diem FROM KetQua WHERE ID=?"
		thong_tin = Database.get_one(self, chuoi_sql, (id,))
		return thong_tin
	
	#Đọc danh sách kết quả của 1 sinh viên theo SinhvienID
	def Read_danh_sach_ket_qua_theo_SinhVienID(self, sinh_vien_id):
		chuoi_sql = 'SELECT * FROM KetQua WHERE SinhVienID=?'
		cursor = Database.get_all(self, chuoi_sql,(sinh_vien_id,) )
		danh_sach = []
		for dong in cursor:
			danh_sach.append(dong)
		return danh_sach

	def Read_danh_sach_ket_qua_theo_dieu_kien(self, ma_so, ten, id_khoa):
		chuoi_sql = "SELECT * FROM KetQua JOIN Sinhvien ON ketqua.SinhVienID=sinhvien.ID WHERE Maso=? AND ten Like '%?%' and KhoaID=?"
		cursor = Database.get_all(self, chuoi_sql,(ma_so, ten, id_khoa,) )
		danh_sach = []
		for dong in cursor:
			danh_sach.append(dong)
		return danh_sach
