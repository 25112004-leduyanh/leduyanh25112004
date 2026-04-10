import math

# ==========================================
# 1. CUSTOM EXCEPTION
# ==========================================
class MauSoBangKhong(Exception):
    """Ngoại lệ riêng khi mẫu số bằng 0"""
    pass

# ==========================================
# 2. LỚP PHÂN SỐ
# ==========================================
class PhanSo:
    def __init__(self, tu, mau):
        self.tu_so = tu    # Tự động gọi @tu_so.setter
        self.mau_so = mau  # Tự động gọi @mau_so.setter

    # --- @property + validation ---
    @property
    def tu_so(self):
        return self._tu_so

    @tu_so.setter
    def tu_so(self, value):
        self._tu_so = value

    @property
    def mau_so(self):
        return self._mau_so

    @mau_so.setter
    def mau_so(self, value):
        if value == 0:
            raise MauSoBangKhong("Mẫu số không được phép bằng 0.")
        self._mau_so = value

    # --- Các phương thức xử lý ---
    def toi_gian(self):
        """Phép tìm dạng tối giản của phân số"""
        ucln = math.gcd(self.tu_so, self.mau_so)
        tu = self.tu_so // ucln
        mau = self.mau_so // ucln
        
        # Đảm bảo mẫu số luôn dương sau khi tối giản
        if mau < 0:
            tu = -tu
            mau = -mau
        return PhanSo(tu, mau)

    def is_toi_gian(self):
        """Phép kiểm tra phân số có tối giản hay không"""
        ucln = math.gcd(self.tu_so, self.mau_so)
        return ucln == 1 and self.mau_so > 0

    # ==========================================
    # 3. OPERATOR OVERLOADING (Toán tử + - * /)
    # ==========================================
    def __add__(self, other):
        if isinstance(other, PhanSo):
            tu = self.tu_so * other.mau_so + other.tu_so * self.mau_so
            mau = self.mau_so * other.mau_so
            return PhanSo(tu, mau).toi_gian()
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, PhanSo):
            tu = self.tu_so * other.mau_so - other.tu_so * self.mau_so
            mau = self.mau_so * other.mau_so
            return PhanSo(tu, mau).toi_gian()
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, PhanSo):
            return PhanSo(self.tu_so * other.tu_so, self.mau_so * other.mau_so).toi_gian()
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, PhanSo):
            if other.tu_so == 0:
                raise ZeroDivisionError("Không thể chia cho phân số có tử bằng 0.")
            return PhanSo(self.tu_so * other.mau_so, self.mau_so * other.tu_so).toi_gian()
        return NotImplemented

    # ==========================================
    # 4. MAGIC METHODS (So sánh & Hiển thị)
    # ==========================================
    def __eq__(self, other):
        """So sánh == (so sánh giá trị thực)"""
        if isinstance(other, PhanSo):
            return self.tu_so * other.mau_so == other.tu_so * self.mau_so
        return False

    def __lt__(self, other):
        """So sánh < (để sắp xếp bằng sorted)"""
        if isinstance(other, PhanSo):
            return (self.tu_so / self.mau_so) < (other.tu_so / other.mau_so)
        return NotImplemented

    def __gt__(self, other):
        """So sánh >"""
        if isinstance(other, PhanSo):
            return (self.tu_so / self.mau_so) > (other.tu_so / other.mau_so)
        return NotImplemented

    def __str__(self):
        """Hiển thị phân số đẹp dạng 'tử/mẫu' hoặc số nguyên nếu mẫu = 1"""
        tg = self.toi_gian()
        if tg.mau_so == 1:
            return str(tg.tu_so)
        return f"{tg.tu_so}/{tg.mau_so}"

    def __repr__(self):
        return f"PhanSo({self.tu_so}, {self.mau_so})"

    def __hash__(self):
        """Hash theo dạng tối giản để có thể loại trùng bằng set()"""
        tg = self.toi_gian()
        return hash((tg.tu_so, tg.mau_so))


# ==========================================
# 5. CHƯƠNG TRÌNH ỨNG DỤNG
# ==========================================
if __name__ == "__main__":
    # 1. Nhập vào một dãy các phân số
    # (Ở đây gán cứng để demo, bạn có thể thay bằng hàm input() nếu cần)
    danh_sach_ps = [
        PhanSo(2, 4),    # Trùng giá trị với 1/2
        PhanSo(3, 4), 
        PhanSo(7, -2),   # Phân số âm
        PhanSo(10, 5),   # Sẽ thành số nguyên
        PhanSo(1, 3)
    ]

    # 2. In ra màn hình dạng tối giản của các phân số đó
    print("--- DẠNG TỐI GIẢN CỦA CÁC PHÂN SỐ ---")
    for ps in danh_sach_ps:
        print(f"Gốc: {repr(ps):<15} -> In đẹp (__str__): {ps}")

    # 3. Sắp xếp dãy phân số theo giá trị tăng dần (dùng sorted() nhờ __lt__)
    danh_sach_sap_xep = sorted(danh_sach_ps)
    print("\n--- DÃY SAU KHI SẮP XẾP TĂNG DẦN ---")
    for ps in danh_sach_sap_xep:
        print(ps, end="  |  ")
    print("\n")
