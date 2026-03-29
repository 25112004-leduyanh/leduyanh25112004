import copy

# Định nghĩa lớp Point (Điểm) cơ bản để LineSegment có thể sử dụng
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

# Định nghĩa lớp LineSegment (Đoạn thẳng) theo yêu cầu
class LineSegment:
    def __init__(self, *args):
        # Thuộc tính d1, d2 kiểu truy cập private (dùng __)
        self.__d1 = None
        self.__d2 = None

        # 1. Hàm xây dựng mặc định, không đối số
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
            
        # 2. Hàm xây dựng sao chép: LineSegment(LineSegment S)
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            S = args[0]
            # Sao chép sâu (Deep copy) đối tượng S để không bị dính tham chiếu
            self.__d1 = copy.deepcopy(S.get_d1())
            self.__d2 = copy.deepcopy(S.get_d2())
            
        # 3. Hàm xây dựng 2 đối số: LineSegment(Point d1, Point d2)
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            # Lấy d1 và d2 làm hai điểm đầu mút, KHÔNG tạo thêm điểm mới (gán trực tiếp)
            self.__d1 = args[0]
            self.__d2 = args[1]
            
        # 4. Hàm xây dựng 4 đối số: LineSegment(int x1, int y1, int x2, int y2)
        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
            
        else:
            raise ValueError("Tham số truyền vào không hợp lệ!")

    # --- Các phương thức hỗ trợ ---
    
    # Getter để lấy d1, d2 phục vụ cho việc sao chép
    def get_d1(self):
        return self.__d1

    def get_d2(self):
        return self.__d2

    # Hàm in ra thông tin đoạn thẳng để dễ kiểm tra
    def in_thong_tin(self):
        print(f"Đoạn thẳng tạo bởi 2 điểm: d1{self.__d1} và d2{self.__d2}")


# ==========================================
# CHẠY THỬ CHƯƠNG TRÌNH (TEST)
# ==========================================
if __name__ == "__main__":
    print("1. Khởi tạo mặc định:")
    line1 = LineSegment()
    line1.in_thong_tin()

    print("\n2. Khởi tạo bằng 2 đối tượng Point:")
    p1 = Point(3, 4)
    p2 = Point(7, 8)
    line2 = LineSegment(p1, p2)
    line2.in_thong_tin()

    print("\n3. Khởi tạo bằng 4 tọa độ (int/float):")
    line3 = LineSegment(10, 20, 30, 40)
    line3.in_thong_tin()

    print("\n4. Khởi tạo sao chép sâu (từ line3):")
    line4 = LineSegment(line3)
    line4.in_thong_tin()
