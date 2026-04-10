# Lớp cha: Hàng Hóa
class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        # Các thuộc tính private theo sơ đồ (-)
        self.__ma_hang = ma_hang
        self.__ten_hang = ten_hang
        self.__nha_sx = nha_sx
        self.__gia = gia

    def xuat_thong_tin(self):
        """Phương thức xuất thông tin cơ bản của hàng hóa"""
        print(f"Mã hàng      : {self.__ma_hang}")
        print(f"Tên hàng     : {self.__ten_hang}")
        print(f"Nhà sản xuất : {self.__nha_sx}")
        print(f"Giá bán      : {self.__gia:,.0f} VNĐ")


# Lớp con 1: Hàng Điện Máy kế thừa từ HangHoa
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        # Gọi hàm khởi tạo của lớp cha
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        # Bổ sung các thuộc tính riêng
        self.__tg_baohanh = tg_baohanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat

    def xuat_thong_tin(self):
        print("--- THÔNG TIN HÀNG ĐIỆN MÁY ---")
        super().xuat_thong_tin() # Gọi lại phương thức in của lớp cha
        print(f"Bảo hành     : {self.__tg_baohanh} tháng")
        print(f"Điện áp      : {self.__dien_ap} V")
        print(f"Công suất    : {self.__cong_suat} W")
        print("-" * 31)


# Lớp con 2: Hàng Sành Sứ kế thừa từ HangHoa
class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__loai_nguyenlieu = loai_nguyenlieu

    def xuat_thong_tin(self):
        print("--- THÔNG TIN HÀNG SÀNH SỨ ---")
        super().xuat_thong_tin()
        print(f"Nguyên liệu  : {self.__loai_nguyenlieu}")
        print("-" * 30)


# Lớp con 3: Hàng Thực Phẩm kế thừa từ HangHoa
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__ngay_sx = ngay_sx
        self.__ngay_hethan = ngay_hethan

    def xuat_thong_tin(self):
        print("--- THÔNG TIN HÀNG THỰC PHẨM ---")
        super().xuat_thong_tin()
        print(f"Ngày SX      : {self.__ngay_sx}")
        print(f"Ngày hết hạn : {self.__ngay_hethan}")
        print("-" * 32)


# ==========================================
# CHƯƠNG TRÌNH CHÍNH (TEST VÀ XUẤT THÔNG TIN)
# ==========================================
if __name__ == "__main__":
    # 1. Tạo 1 mặt hàng điện máy
    may_giat = HangDienMay("DM01", "Máy giặt Inverter", "LG", 12500000, 24, 220, 2000)
    
    # 2. Tạo 1 mặt hàng sành sứ
    bo_am_tra = HangSanhSu("SS01", "Bộ ấm trà cao cấp", "Gốm sứ Bát Tràng", 850000, "Đất sét trắng")
    
    # 3. Tạo 1 mặt hàng thực phẩm
    sua_tuoi = HangThucPham("TP01", "Sữa tươi ít đường", "Vinamilk", 35000, "01/10/2023", "01/04/2024")

    # Xuất thông tin các mặt hàng vừa tạo
    may_giat.xuat_thong_tin()
    bo_am_tra.xuat_thong_tin()
    sua_tuoi.xuat_thong_tin()
