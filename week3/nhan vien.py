class NhanVien:
    # Hằng số của lớp (Tương đương LUONG_MAX : double)
    LUONG_MAX = 30000000.0  # Giả sử đặt mức lương tối đa là 30 triệu

    def __init__(self, ten_nhan_vien, luong_co_ban, he_so_luong):
        # Thuộc tính private (thêm 1 dấu gạch dưới theo quy ước Python)
        self._tenNhanVien = ten_nhan_vien
        self._luongCoBan = luong_co_ban
        self._heSoLuong = he_so_luong

    # -----------------------------------------------------------------
    # YÊU CẦU 4: Viết đầy đủ getter/setter cho tất cả thuộc tính
    # -----------------------------------------------------------------
    def get_tenNhanVien(self):
        return self._tenNhanVien

    def set_tenNhanVien(self, ten_moi):
        self._tenNhanVien = ten_moi

    def get_luongCoBan(self):
        return self._luongCoBan

    def set_luongCoBan(self, luong_moi):
        self._luongCoBan = luong_moi

    def get_heSoLuong(self):
        return self._heSoLuong

    def set_heSoLuong(self, he_so_moi):
        self._heSoLuong = he_so_moi

    # -----------------------------------------------------------------
    # YÊU CẦU 1: Phương thức tính lương
    # -----------------------------------------------------------------
    def tinhLuong(self):
        return self._luongCoBan * self._heSoLuong

    # -----------------------------------------------------------------
    # YÊU CẦU 2: Phương thức in thông tin
    # -----------------------------------------------------------------
    def inTTin(self):
        print("--- THÔNG TIN NHÂN VIÊN ---")
        print(f"Tên nhân viên: {self._tenNhanVien}")
        print(f"Lương cơ bản: {self._luongCoBan:,.0f} VNĐ")
        print(f"Hệ số lương: {self._heSoLuong}")
        print(f"Tổng lương: {self.tinhLuong():,.0f} VNĐ")
        print("---------------------------")

    # -----------------------------------------------------------------
    # YÊU CẦU 3: Phương thức tăng lương
    # -----------------------------------------------------------------
    def tangLuong(self, delta):
        # Giả sử 'delta' là phần hệ số lương được cộng thêm
        luong_moi = self._luongCoBan * (self._heSoLuong + delta)
        
        if luong_moi > NhanVien.LUONG_MAX:
            print(f"Thông báo: Không thể tăng lương! Lương mới ({luong_moi:,.0f}) vượt quá LUONG_MAX ({NhanVien.LUONG_MAX:,.0f}).")
            return False
        else:
            self._heSoLuong += delta
            print(f"Tăng lương thành công! Hệ số lương mới là {self._heSoLuong}")
            return True
