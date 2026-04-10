import sys

# ==========================================
# YÊU CẦU 1: XÂY DỰNG CÁC LỚP CÁN BỘ
# ==========================================
class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def hien_thi_thong_tin(self):
        return f"Họ tên: {self.ho_ten} | Tuổi: {self.tuoi} | Giới tính: {self.gioi_tinh} | Địa chỉ: {self.dia_chi}"

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        # Bậc công nhân giới hạn từ 1 đến 10
        if not (1 <= bac <= 10):
            raise ValueError("Bậc của công nhân phải nằm trong khoảng từ 1 đến 10.")
        self.bac = bac

    def hien_thi_thong_tin(self):
        return "[Công nhân] " + super().hien_thi_thong_tin() + f" | Bậc: {self.bac}"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def hien_thi_thong_tin(self):
        return "[Kỹ sư] " + super().hien_thi_thong_tin() + f" | Ngành đào tạo: {self.nganh_dao_tao}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def hien_thi_thong_tin(self):
        return "[Nhân viên] " + super().hien_thi_thong_tin() + f" | Công việc: {self.cong_viec}"


# ==========================================
# YÊU CẦU 2: XÂY DỰNG LỚP QUẢN LÝ CÁN BỘ (QLCB)
# ==========================================
class QLCB:
    def __init__(self):
        self.danh_sach_can_bo = []

    def them_moi_can_bo(self, can_bo):
        """Thêm mới cán bộ vào danh sách"""
        self.danh_sach_can_bo.append(can_bo)
        print("-> Đã thêm cán bộ thành công!\n")

    def tim_kiem_theo_ho_ten(self, tu_khoa):
        """Tìm kiếm cán bộ theo họ tên"""
        ket_qua = [cb for cb in self.danh_sach_can_bo if tu_khoa.lower() in cb.ho_ten.lower()]
        
        if not ket_qua:
            print(f"-> Không tìm thấy cán bộ nào có tên chứa '{tu_khoa}'.\n")
        else:
            print(f"--- KẾT QUẢ TÌM KIẾM CHO '{tu_khoa}' ---")
            for cb in ket_qua:
                print(cb.hien_thi_thong_tin())
            print()

    def hien_thi_danh_sach(self):
        """Hiển thị thông tin về danh sách các cán bộ"""
        if not self.danh_sach_can_bo:
            print("-> Danh sách cán bộ hiện đang trống.\n")
            return
            
        print("--- DANH SÁCH CÁN BỘ ---")
        for cb in self.danh_sach_can_bo:
            print(cb.hien_thi_thong_tin())
        print()

    def thoat_chuong_trinh(self):
        """Thoát khỏi chương trình"""
        print("-> Đang thoát chương trình. Tạm biệt!")
        sys.exit()
