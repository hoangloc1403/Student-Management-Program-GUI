from Thu_vien.Database import *

class NhanVien(Database):
	def __init__(self, path_db):
		Database.__init__(self, path_db)

	def Read_nhan_vien(self, ma_so):
		chuoi_sql = "SELECT * FROM NhanVien WHERE MaSo=?"
		thong_tin = Database.get_one(self, chuoi_sql, (ma_so,))
		return thong_tin
	
	def Read_danh_sach_nhan_vien(self):
		chuoi_sql = 'SELECT * FROM NhanVien'
		cursor = Database.get_all(self, chuoi_sql)
		danh_sach = []
		for dong in cursor:
			danh_sach.append(dong)
		return danh_sach

	def Add_nhan_vien(self, ma_so, ho_ten, mat_khau):
		#kiểm tra MaSo bị trùng
		chuoi_sql="Select * from NhanVien Where Maso=?"
		cursor = Database.get_one(self, chuoi_sql,(ma_so,))
		if cursor!=None:	#đã có khóa rồi
			kq =0
		else:
			chuoi_sql = "INSERT INTO NhanVien(MaSo, HoTen, MatKhau) VALUES (?, ?, ?)"
			kq = Database.execute(self, chuoi_sql, (ma_so, ho_ten, mat_khau))
		return kq
	
	def Update_nhan_vien(self,ho_ten, mat_khau, ma_so ):
		chuoi_sql = "UPDATE NhanVien SET HoTen=?, MatKhau=? WHERE MaSo=?"
		kq = Database.execute(self, chuoi_sql, (ho_ten, mat_khau, ma_so ))
		return kq
	
	def Delete_nhan_vien(self, ma_so ):
		chuoi_sql = "DELETE FROM NhanVien WHERE MaSo=?"
		kq = Database.execute(self, chuoi_sql, (ma_so,))
		return kq

	def Update_mat_khau_moi(self, mat_khau_new, ma_so ):
		chuoi_sql = "UPDATE NhanVien SET  MatKhau=? WHERE MaSo=?"
		kq = Database.execute(self, chuoi_sql, ( mat_khau_new, ma_so ))
		return kq
