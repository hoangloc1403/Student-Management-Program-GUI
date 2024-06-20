from Thu_vien.Database import *

class Khoa(Database):
	def __init__(self, path_db):
		Database.__init__(self, path_db)

	# viết các hàm truy xuất
	def Read_Khoa_id(self, id):
		chuoi_sql = "SELECT * FROM Khoa WHERE id=?"
		thong_tin = Database.get_one(self, chuoi_sql, (id,))
		return thong_tin

	def Read_Khoa_maso(self, ma_so):
		chuoi_sql = "SELECT * FROM Khoa WHERE MaSo=?"
		thong_tin = Database.get_one(self, chuoi_sql, (ma_so,))
		return thong_tin
	
	def Read_danh_sach_khoa(self):
		chuoi_sql = 'SELECT * FROM Khoa'
		cursor = Database.get_all(self, chuoi_sql)
		danh_sach = []
		for dong in cursor:
			danh_sach.append(dong)
		return danh_sach

	def Read_ID_tu_ten_khoa(self, ten_khoa):
		chuoi_sql = "SELECT ID FROM Khoa WHERE Ten=?"
		thong_tin = Database.get_one(self, chuoi_sql, (ten_khoa,))
		return thong_tin
	def Read_ds_tenkhoa(self):
		chuoi_sql="Select ten from Khoa "
		cursor = Database.get_all(self, chuoi_sql)
		danh_sach = []
		for dong in cursor:
			danh_sach.append(dong[0])
		return danh_sach
	#====Viết các hàm cập nhật ===============================
	def Add_Khoa(self, ma_so, ten):
		#kiểm tra MaSo bị trùng
		chuoi_sql="Select * from Khoa Where Maso=?"
		cursor = Database.get_one(self, chuoi_sql,(ma_so,))
		if cursor!=None:	#đã có khóa rồi
			kq =0
		else:
			chuoi_sql = "INSERT INTO Khoa(MaSo, Ten) VALUES (?, ?)"
			kq = Database.execute(self, chuoi_sql, (ma_so, ten))
		return kq
	
	def Update_khoa(self, ten, ma_so ):
		chuoi_sql = "UPDATE Khoa SET Ten=? WHERE MaSo=?"
		kq = Database.execute(self, chuoi_sql, (ten, ma_so ))
		return kq
	
	def Delete_khoa(self, ma_so ):
		chuoi_sql = "DELETE FROM Khoa WHERE MaSo=?"
		kq = Database.execute(self, chuoi_sql, (ma_so,))
		return kq