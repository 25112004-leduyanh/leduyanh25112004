# 1. Lớp Con chó (Dog)
class ConCho:
    def __init__(self, ten, mau_sac, giong, cam_xuc):
        # Thuộc tính
        self.ten = ten
        self.mau_sac = mau_sac
        self.giong = giong
        self.cam_xuc = cam_xuc

    # Phương thức
    def sua(self):
        print(f"{self.ten} đang sủa: Gâu gâu!")

    def vay_duoi(self):
        print(f"{self.ten} đang vẫy đuôi vui vẻ.")

    def an(self):
        print(f"{self.ten} đang ăn xương.")

    def chay(self):
        print(f"{self.ten} đang chạy rất nhanh.")

# ---------------------------------------------------------

# 2. Lớp Ô tô (Car)
class OTo:
    def __init__(self, hang, kich_thuoc, mau, gia):
        # Thuộc tính
        self.hang = hang
        self.kich_thuoc = kich_thuoc
        self.mau = mau
        self.gia = gia

    # Phương thức
    def tang_toc(self):
        print(f"Xe {self.hang} đang tăng tốc!")

    def giam_toc(self):
        print(f"Xe {self.hang} đang giảm tốc.")

    def dam(self):
        print(f"Cảnh báo: Xe {self.hang} vừa va chạm!")

# ---------------------------------------------------------

# 3. Lớp Tài khoản (Account)
class TaiKhoan:
    def __init__(self, ten_tk, so_tk, ngan_hang, so_du=0):
        # Thuộc tính
        self.ten_tk = ten_tk
        self.so_tk = so_tk
        self.ngan_hang = ngan_hang
        self.so_du = so_du  # Khởi tạo số dư mặc định có thể là 0

    # Phương thức
    def rut(self, so_tien):
        if so_tien <= self.so_du:
            self.so_du -= so_tien
            print(f"Đã rút {so_tien}. Số dư còn lại: {self.so_du}")
        else:
            print("Lỗi: Số dư không đủ để rút tiền.")

    def gui(self, so_tien):
        self.so_du += so_tien
        print(f"Đã gửi {so_tien}. Số dư hiện tại: {self.so_du}")

    def kiem_tra_so_du(self):
        print(f"Số dư tài khoản {self.so_tk} là: {self.so_du}")
