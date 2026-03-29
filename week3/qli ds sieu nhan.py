# 1. Khởi tạo class siêu nhân (thuộc tính tùy chọn)
class SieuNhan:
    def __init__(self, ten, nang_luc, khu_vuc):
        self.ten = ten
        self.nang_luc = nang_luc
        self.khu_vuc = khu_vuc

# Tạo một danh sách rỗng để lưu trữ các siêu nhân
danh_sach_sieu_nhan = []

print("=== CHƯƠNG TRÌNH QUẢN LÝ SIÊU NHÂN TOÀN THẾ GIỚI ===")
print("(Nhập 'thoat' ở phần Tên để kết thúc việc nhập dữ liệu)\n")

# 2. Dùng while để nhập danh sách
while True:
    ten = input("Nhập tên siêu nhân: ")
    
    # Điều kiện dừng vòng lặp while
    if ten.lower() == 'thoat':
        break
        
    nang_luc = input("Nhập năng lực: ")
    khu_vuc = input("Nhập khu vực bảo vệ: ")
    
    # Tạo đối tượng siêu nhân mới và thêm vào danh sách
    sn_moi = SieuNhan(ten, nang_luc, khu_vuc)
    danh_sach_sieu_nhan.append(sn_moi)
    print("-> Đã thêm vào cơ sở dữ liệu!\n")

# 3. Dùng for để in danh sách kèm thuộc tính
print("\n==================================================")
print("       DANH SÁCH SIÊU NHÂN TRÊN TOÀN THẾ GIỚI     ")
print("==================================================")

if len(danh_sach_sieu_nhan) == 0:
    print("Hiện chưa có siêu nhân nào trong danh sách.")
else:
    for i, sn in enumerate(danh_sach_sieu_nhan, 1):
        print(f"{i}. Tên: {sn.ten}")
        print(f"   - Năng lực: {sn.nang_luc}")
        print(f"   - Khu vực : {sn.khu_vuc}")
        print("-" * 30)
