import math

class Point:
    def __init__(self, x=0, y=0):
        # Thuộc tính x, y (ép kiểu về int theo yêu cầu đề bài)
        self.x = int(x)
        self.y = int(y)

    def hien_thi(self):
        """Hiển thị tọa độ của điểm dưới dạng (x, y)"""
        print(f"({self.x}, {self.y})")

    def doi_xung_qua_O(self):
        """Trả về một đối tượng Point mới đối xứng qua gốc tọa độ O(0,0)"""
        return Point(-self.x, -self.y)

    def khoang_cach_den_O(self):
        """Tính khoảng cách từ điểm hiện tại đến gốc tọa độ O"""
        return math.sqrt(self.x**2 + self.y**2)

    def khoang_cach_den_diem_khac(self, diem_khac):
        """Tính khoảng cách từ điểm hiện tại đến một điểm khác"""
        return math.sqrt((self.x - diem_khac.x)**2 + (self.y - diem_khac.y)**2)


# ==========================================
# THỰC THI CÁC YÊU CẦU CỦA ĐỀ BÀI
# ==========================================

# 1. Tạo điểm A(3, 4) và hiển thị tọa độ
A = Point(3, 4)
print("1. Tọa độ điểm A: ", end="")
A.hien_thi()

# 2. Tạo điểm B từ bàn phím
print("\n2. Nhập tọa độ cho điểm B:")
x_b = int(input("   Nhập x: "))
y_b = int(input("   Nhập y: "))
B = Point(x_b, y_b)
print("   Tọa độ điểm B vừa nhập: ", end="")
B.hien_thi()

# 3. Tạo điểm C đối xứng với B qua gốc O
C = B.doi_xung_qua_O()
print("\n3. Tọa độ điểm C (đối xứng với B qua O): ", end="")
C.hien_thi()

# 4. Tính khoảng cách từ B đến O
d_BO = B.khoang_cach_den_O()
print(f"\n4. Khoảng cách từ B đến gốc O: {d_BO:.2f}")

# 5. Tính khoảng cách từ A đến B
d_AB = A.khoang_cach_den_diem_khac(B)
print(f"5. Khoảng cách từ A đến B: {d_AB:.2f}")
