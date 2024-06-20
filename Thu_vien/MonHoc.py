from Thu_vien.Database import *

class MonHoc(Database):
    def __init__(self,path_db):
        Database.__init__(self,path_db)

    def Read_mon_hoc(self,ma_so):
        chuoi_sql = "SELECT * FROM MonHoc WHERE MaSo=?"
        thong_tin = Database.get_one(self,chuoi_sql,(ma_so,))
        return thong_tin
    
    def Read_danh_sach_mon_hoc(self):
        chuoi_sql = "SELECT * FROM MonHoc"
        danh_sach = Database.get_all(self,chuoi_sql)
        return danh_sach
    
    def Add_mon_hoc(self,ma_so,ten):
        chuoi_sql = "SELECT * FROM MonHoc WHERE MaSo=?"
        cursor = Database.get_one(self,chuoi_sql,(ma_so,))
        if cursor != None:
            kq = 0
        else:
            chuoi_sql = "INSERT INTO MonHoc (MaSo,Ten) VALUES (?,?)"
            kq = Database.execute(self,chuoi_sql,(ma_so,ten))
        return kq
    
    def Update_mon_hoc(self,ten,ma_so):
        chuoi_sql = "UPDATE MonHoc SET Ten=?  WHERE MaSo=?"
        kq = Database.execute(self,chuoi_sql,(ten,ma_so))
        return kq

    def Delete_mon_hoc(self,ma_so,ten):
        chuoi_sql = "DELETE FROM MonHoc WHERE MaSo=?"
        kq = Database.execute(self,chuoi_sql,(ma_so,))
        return kq
