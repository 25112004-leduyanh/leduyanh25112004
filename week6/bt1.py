from abc import ABC, abstractmethod

# ==========================================
# 1. CUSTOM EXCEPTIONS
# ==========================================
class GiaKhongHopLe(Exception):
    """Lỗi ném ra khi giá sản phẩm nhỏ hơn 0"""
    pass

class MaHangTrungLap(Exception):
    """Lỗi ném ra khi thêm hàng hóa bị trùng mã"""
    pass

# ==========================================
# 2. LỚP TRỪU TƯỢNG HÀNG HÓA (ABC)
# ==========================================
class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia  # Sẽ tự động gọi vào @gia.setter

    # @property: Getter cho ma_hang (read-only)
    @property
    def ma_hang(self):
        return self._ma_hang

    # @property: Getter cho ten_hang (read-only)
    @property
    def ten_hang(self):
        return self._ten_hang

    # @property: Getter và Setter cho gia (kèm validation)
    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(f"Giá {value} không hợp lệ. Giá phải >= 0.")
        self._gia = value

    # Abstract methods
    @abstractmethod
    def loai_hang(self):
        pass

    @abstractmethod
    def inTTin(self):
        pass

    # ==========================================
    # 3. MAGIC METHODS
    # ==========================================
    def __str__(self):
        # Hiển thị đẹp khi dùng print(sp)
        return self.inTTin()

    def __eq__(self, other):
        # So sánh bằng nhau dựa trên mã hàng
        if isinstance(other, HangHoa):
            return self.ma_hang == other.ma_hang
        return False

    def __lt__(self, other):
        # So sánh nhỏ hơn dựa trên giá (để dùng sorted())
        if isinstance(other, HangHoa):
            return self.gia < other.gia
        return NotImplemented

    def __hash__(self):
        # Hàm băm dựa trên mã hàng (để có thể đưa vào set())
        return hash(self.ma_hang)


# ==========================================
# 4. CÁC LỚP CON (METHOD OVERRIDING)
# ==========================================
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def loai_hang(self):
        return "Điện Máy"

    def inTTin(self):
        return f"[{self.loai_hang()}] Mã: {self.ma_hang} | Tên: {self.ten_hang} | Giá: {self.gia} | BH: {self.tg_baohanh} tháng | Công suất: {self.cong_suat}W"


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyenlieu = loai_nguyenlieu

    def loai_hang(self):
        return "Sành Sứ"

    def inTTin(self):
        return f"[{self.loai_hang()}] Mã: {self.ma_hang} | Tên: {self.ten_hang} | Giá: {self.gia} | Nguyên liệu: {self.loai_nguyenlieu}"


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan

    def loai_hang(self):
        return "Thực Phẩm"

    def inTTin(self):
        return f"[{self.loai_hang()}] Mã: {self.ma_hang} | Tên: {self.ten_hang} | Giá: {self.gia} | HSD: {self.ngay_hethan}"


# ==========================================
# 5. QUẢN LÝ HÀNG HÓA VÀ CONTEXT MANAGER
# ==========================================
class QuanLyHangHoa:
    def __init__(self):
        # Dùng set() để lưu trữ, tự động loại bỏ trùng lặp nếu có 
        # (nhưng ta vẫn sẽ ném lỗi thủ công theo yêu cầu bài toán)
        self.danh_sach = set()

    def them_hang(self, hang_hoa):
        # Ném exception nếu mã hàng bị trùng
        if hang_hoa in self.danh_sach:
            raise MaHangTrungLap(f"Không thể thêm. Mã hàng '{hang_hoa.ma_hang}' đã tồn tại!")
        self.danh_sach.add(hang_hoa)

    def luu_danh_sach_ra_file(self, ten_file):
        # Dùng Context Manager (with) để mở và ghi file an toàn
        with open(ten_file, 'w', encoding='utf-8') as f:
            for sp in self.danh_sach:
                f.write(sp.inTTin() + '\n')
            
    def doc_danh_sach_tu_file(self, ten_file):
        # Dùng Context Manager (with) để mở và đọc file
        with open(ten_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
