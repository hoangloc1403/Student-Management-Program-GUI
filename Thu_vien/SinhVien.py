from Thu_vien.Database import *

class SinhVien(Database):
	def __init__(self, path_db):
		Database.__init__(self, path_db)

	#Đọc 1 sinh viên
	def Read_sinh_vien(self, ma_so):
		chuoi_sql = "SELECT * FROM SinhVien WHERE MaSo=?"
		thong_tin = Database.get_one(self, chuoi_sql, (ma_so,))
		return thong_tin
	#Đọc 1 sinh viên theo khoa ID
	def Read_sinh_vien_Tenkhoa(self, ma_so):
		chuoi_sql = "SELECT sv.*,kh.Ten FROM SinhVien sv INNER JOIN Khoa kh ON sv.KhoaID = kh.ID WHERE sv.MaSo=?"
		thong_tin = Database.get_one(self, chuoi_sql, (ma_so,))
		return thong_tin

	#Đọc ds sinh viên theo khoa hoặc tất cả
	def Read_danh_sach_sinh_vien_khoa(self, id_khoa=""):
		if id_khoa=="":
			chuoi_sql = 'SELECT * FROM SinhVien'
			cursor = Database.get_all(self, chuoi_sql)
		else:
			chuoi_sql = 'SELECT * FROM SinhVien WHERE khoaID=? ORDER BY Maso DESC'
			cursor = Database.get_all(self, chuoi_sql, (id_khoa,))

		danh_sach = []
		for dong in cursor:
			danh_sach.append(dong)
		return danh_sach

	#Đọc kết quả của sinh viên
	def Read_ket_qua(self, ma_sv, ten, id_khoa ):
		chuoi_sql = '''SELECT Sinhvien.MaSo, Ho, Sinhvien.Ten, Monhoc.Ten, Diem, Khoa.Ten  
						FROM ((SinhVien INNER JOIN ketQua ON sinhvien.ID=ketqua.SinhvienID) 
						INNER JOIN Monhoc ON ketqua.MonhocID = Monhoc.ID)
						INNER JOIN Khoa ON khoa.ID = Sinhvien.KhoaID
					'''
		if ma_sv!="":
			chuoi_sql += " WHERE sinhvien.MaSo =?"
			cursor = Database.get_all(self, chuoi_sql, (ma_sv,))
		else:
			if ten!="":
				chuoi_sql += " WHERE sinhvien.Ten=? And sinhvien.KhoaID=?"
				cursor = Database.get_all(self, chuoi_sql, (ten, id_khoa))
			else:
				chuoi_sql += " WHERE sinhvien.KhoaID=?"
				cursor = Database.get_all(self, chuoi_sql, (id_khoa,))

		danh_sach = []
		for dong in cursor:
			danh_sach.append(dong)
		return danh_sach

	def Add_sinh_vien(self, ma_so, ho, ten, gioi_tinh, ngay_sinh, mail, di_dong, cmnd, hoc_bong, id_khoa):
		#kiểm tra MaSo bị trùng
		chuoi_sql="Select * from SinhVien Where Maso=?"
		cursor = Database.get_one(self, chuoi_sql,(ma_so,))
		print(cursor)
		if cursor!=None:	#đã có khóa rồi
			kq =0
		else:
			chuoi_sql = """INSERT INTO SinhVien(MaSo, Ho, Ten, GioiTinh, NgaySinh, Mail, DiDong, CMND, HocBong, KhoaID) 
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
			kq = Database.execute(self, chuoi_sql, (ma_so, ho, ten, gioi_tinh, ngay_sinh, mail, di_dong, cmnd, hoc_bong, id_khoa))
		print("kq = ", kq)
		return kq
	
	def Update_sinh_vien(self,ho, ten, gioi_tinh, ngay_sinh, mail, di_dong, cmnd, hoc_bong, id_khoa, ma_so ):
		chuoi_sql = "UPDATE SinhVien SET Ho=?, Ten=?, GioiTinh=?, NgaySinh=?, Mail=?, DiDong=?, CMND=?, HocBong=?, KhoaID=? WHERE MaSo=?"
		kq = Database.execute(self, chuoi_sql, (ho, ten,gioi_tinh, ngay_sinh, mail, di_dong, cmnd, hoc_bong,id_khoa, ma_so ))
		return kq
	
	def Delete_sinh_vien(self, ma_so ):
		chuoi_sql = "DELETE FROM SinhVien WHERE MaSo=?"
		kq = Database.execute(self, chuoi_sql, (ma_so,))
		return kq

'''
Ghi chú:		
- Gởi trang này cho HV đọc thêm các cú pháp truy vấn: https://www.sqlitetutorial.net/
'''