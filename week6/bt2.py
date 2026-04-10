from abc import ABC, abstractmethod
import sys

# ==========================================
# 1. CUSTOM EXCEPTIONS
# ==========================================
class TuoiKhongHopLe(Exception):
    """Ném ra khi tuổi không nằm trong khoảng 18 - 65"""
    pass

class BacKhongHopLe(Exception):
    """Ném ra khi bậc công nhân không nằm trong khoảng 1 - 10"""
    pass

# ==========================================
# 2. LỚP TRỪU TƯỢNG CÁN BỘ (ABC)
# ==========================================
class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi  # Tự động gọi đến @tuoi.setter
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    # @property + validation cho Tuổi
    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(f"Tuổi {value} không hợp lệ. Chỉ nhận tuổi từ 18-65.")
        self._tuoi = value

    # Abstract method
    @abstractmethod
    def mo_ta(self):
        pass

    # ==========================================
    # 3. MAGIC METHODS
    # ==========================================
    def __str__(self):
        return self.mo_ta()

    def __repr__(self):
        return self.mo_ta()

    def __eq__(self, other):
        # So sánh dựa theo họ tên và tuổi
        if isinstance(other, CanBo):
            return self.ho_ten == other.ho_ten and self.tuoi == other.tuoi
        return False

    def __lt__(self, other):
        # Sắp xếp theo tên (ABC)
        if isinstance(other, CanBo):
            return self.ho_ten < other.ho_ten
        return NotImplemented


# ==========================================
# 4. CÁC LỚP CON (OVERRIDE mo_ta)
# ==========================================
class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac  # Tự động gọi đến @bac.setter

    # @property + validation cho Bậc công nhân
    @property
    def bac(self):
        return self._bac

    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe(f"Bậc {value} không hợp lệ. Chỉ nhận bậc từ 1-10.")
        self._bac = value

    def mo_ta(self):
        return f"[Công Nhân] {self.ho_ten} | {self.tuoi} tuổi | {self.gioi_tinh} | {self.dia_chi} | Bậc: {self.bac}"


class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def mo_ta(self):
        return f"[Kỹ Sư] {self.ho_ten} | {self.tuoi} tuổi | {self.gioi_tinh} | {self.dia_chi} | Ngành ĐT: {self.nganh_dao_tao}"


class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def mo_ta(self):
        return f"[Nhân Viên] {self.ho_ten} | {self.tuoi} tuổi | {self.gioi_tinh} | {self.dia_chi} | Công việc: {self.cong_viec}"


# ==========================================
# 5. LỚP QUẢN LÝ CÁN BỘ (VỚI CONTEXT MANAGER)
# ==========================================
class QLCB:
    def __init__(self):
        self.danh_sach = []

    def them_moi(self, can_bo):
        self.danh_sach.append(can_bo)

    def tim_kiem_theo_ten(self, tu_khoa):
        return [cb for cb in self.danh_sach if tu_khoa.lower() in cb.ho_ten.lower()]

    def hien_thi_danh_sach(self):
        # Có thể dùng sorted(self.danh_sach) để hiển thị danh sách đã được sắp xếp theo __lt__
        for cb in self.danh_sach:
            print(cb)  # Sẽ tự động gọi __str__

    def luu_danh_sach_ra_file(self, ten_file):
        # Dùng 'with' để lưu file
        with open(ten_file, 'w', encoding='utf-8') as f:
            for cb in self.danh_sach:
                f.write(repr(cb) + '\n')

    def doc_danh_sach_tu_file(self, ten_file):
        # Dùng 'with' để đọc file
        with open(ten_file, 'r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())

    def thoat(self):
        sys.exit()
