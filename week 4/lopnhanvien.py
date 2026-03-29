class NhanVien:
    def __init__(self, tenNhanVien, luongCoBan, heSoLuong, LUONG_MAX):
        # Các thuộc tính private (dấu - trong sơ đồ)
        self.__tenNhanVien = tenNhanVien
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong
        # Thuộc tính public (dấu + trong sơ đồ)
        self.LUONG_MAX = LUONG_MAX

    # --- Viết các phương thức GET và SET cho các thuộc tính ---
    @property
    def tenNhanVien(self):
        return self.__tenNhanVien

    @tenNhanVien.setter
    def tenNhanVien(self, value):
        self.__tenNhanVien = value

    @property
    def luongCoBan(self):
        return self.__luongCoBan

    @luongCoBan.setter
    def luongCoBan(self, value):
        self.__luongCoBan = value

    @property
    def heSoLuong(self):
        return self.__heSoLuong

    @heSoLuong.setter
    def heSoLuong(self, value):
        self.__heSoLuong = value

    # --- Các phương thức xử lý (nghiệp vụ) ---
    def tinhLuong(self):
        """Tính lương = Lương cơ bản * Hệ số lương"""
        return self.__luongCoBan * self.__heSoLuong

    def tangLuong(self, heSoTang):
        """Tăng hệ số lương, kiểm tra điều kiện không vượt quá LUONG_MAX"""
        heSoMoi = self.__heSoLuong + heSoTang
        luongMoi = self.__luongCoBan * heSoMoi
        
        if luongMoi > self.LUONG_MAX:
            print("Thông báo: Không thể tăng lương! Lương mới vượt quá LUONG_MAX cho phép.")
            return False
        else:
            self.__heSoLuong = heSoMoi
            return True

    def inTTin(self):
        """Hiển thị thông tin nhân viên"""
        print(f"--- Thông tin nhân viên ---")
        print(f"Tên nhân viên : {self.__tenNhanVien}")
        print(f"Lương cơ bản  : {self.__luongCoBan:,.0f}")
        print(f"Hệ số lương   : {self.__heSoLuong}")
        print(f"Lương hiện tại: {self.tinhLuong():,.0f}")
        print(f"LUONG_MAX     : {self.LUONG_MAX:,.0f}")
        print("-" * 27)

# ==========================================
# CHẠY THỬ CHƯƠNG TRÌNH (TEST)
# ==========================================
if __name__ == "__main__":
    # Khởi tạo nhân viên: Lương CB = 5 triệu, Hệ số = 2.0, Lương Max = 15 triệu
    nv = NhanVien("Trần Văn Python", 5000000, 2.0, 15000000)
    
    # In thông tin ban đầu (Lương hiện tại = 10 triệu)
    nv.inTTin()

    # Trường hợp 1: Tăng hệ số thêm 0.5 -> Hệ số mới 2.5 -> Lương mới 12.5 triệu (Hợp lệ)
    print(">> Đang thử tăng hệ số lương thêm 0.5...")
    thanh_cong = nv.tangLuong(0.5)
    print(f"Kết quả trả về: {thanh_cong}")
    nv.inTTin()

    # Trường hợp 2: Tăng hệ số thêm 1.0 -> Hệ số mới 3.5 -> Lương mới 17.5 triệu (Vượt 15 triệu -> Báo lỗi)
    print(">> Đang thử tăng hệ số lương thêm 1.0...")
    thanh_cong = nv.tangLuong(1.0)
    print(f"Kết quả trả về: {thanh_cong}")
    nv.inTTin()
