class NhanVien:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        
        # Kiểm tra điều kiện hệ số lương > 0
        if he_so_luong <= 0:
            raise ValueError("Hệ số lương phải lớn hơn 0")
        self.he_so_luong = he_so_luong
        self.luong_toi_da = luong_toi_da

    def tinh_thu_nhap(self, luong_co_ban):
        # Tính lương thông thường
        thu_nhap = luong_co_ban * self.he_so_luong
        # Đảm bảo thu nhập không vượt quá lương tối đa
        return min(thu_nhap, self.luong_toi_da)

    def hien_thi_thong_tin(self):
        print(f"[{self.ma_nv}] {self.ho_ten} | Sinh năm: {self.nam_sinh} | Giới tính: {self.gioi_tinh}")
        print(f"Địa chỉ: {self.dia_chi} | Hệ số lương: {self.he_so_luong}")


class CongTacVien(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, thoi_han_hd, phu_cap_ld):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        
        # Kiểm tra thời hạn hợp đồng hợp lệ
        hop_dong_hop_le = ["3 tháng", "6 tháng", "1 năm"]
        if thoi_han_hd not in hop_dong_hop_le:
            raise ValueError("Thời hạn hợp đồng chỉ được là '3 tháng', '6 tháng' hoặc '1 năm'")
        self.thoi_han_hd = thoi_han_hd
        self.phu_cap_ld = phu_cap_ld

    def tinh_thu_nhap(self, luong_co_ban):
        # Cộng thêm phụ cấp lao động
        thu_nhap = (luong_co_ban * self.he_so_luong) + self.phu_cap_ld
        return min(thu_nhap, self.luong_toi_da)

    def hien_thi_thong_tin(self):
        print("\n--- CỘNG TÁC VIÊN ---")
        super().hien_thi_thong_tin()
        print(f"Hợp đồng: {self.thoi_han_hd} | Phụ cấp LĐ: {self.phu_cap_ld:,.0f} VNĐ")


class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, vi_tri_cv):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.vi_tri_cv = vi_tri_cv

    def hien_thi_thong_tin(self):
        print("\n--- NHÂN VIÊN CHÍNH THỨC ---")
        super().hien_thi_thong_tin()
        print(f"Vị trí công việc: {self.vi_tri_cv}")


class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, ngay_bat_dau_ql, phu_cap_ql):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.ngay_bat_dau_ql = ngay_bat_dau_ql
        self.phu_cap_ql = phu_cap_ql

    def tinh_thu_nhap(self, luong_co_ban):
        # Cộng thêm phụ cấp quản lý
        thu_nhap = (luong_co_ban * self.he_so_luong) + self.phu_cap_ql
        return min(thu_nhap, self.luong_toi_da)

    def hien_thi_thong_tin(self):
        print("\n--- TRƯỞNG PHÒNG ---")
        super().hien_thi_thong_tin()
        print(f"Ngày BĐ quản lý: {self.ngay_bat_dau_ql} | Phụ cấp QL: {self.phu_cap_ql:,.0f} VNĐ")
