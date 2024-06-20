import sqlite3

class Database:
    def __init__(self,path_db):
        self.conn = sqlite3.connect(path_db)
    
    def get_all(self,chuoi_sql,bieu_thu_dieu_kieu=()):
        cursor = self.conn.execute(chuoi_sql,bieu_thu_dieu_kieu)
        danh_sach = cursor.fetchall()
        return danh_sach
    
    def get_one(self,chuoi_sql,bieu_thu_dieu_kieu=()):
        cursor = self.conn.execute(chuoi_sql,bieu_thu_dieu_kieu)
        doi_tuong = cursor.fetchone()
        return doi_tuong

    def execute(self,chuoi_sql,bieu_thu_dieu_kieu=()):
        cursor = self.conn.execute(chuoi_sql,bieu_thu_dieu_kieu)
        self.conn.commit()
        return cursor.rowcount
    
    def disconnect(self):
        self.conn.close()
