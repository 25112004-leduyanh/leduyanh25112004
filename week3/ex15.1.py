import math

# ---------------------------------------------------------
# CÁC LỚP PHỤ TRỢ (Point và Rectangle)
# ---------------------------------------------------------
class Point:
    """Đại diện cho một điểm trong không gian 2D."""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class Rectangle:
    """Đại diện cho một hình chữ nhật.
    Thuộc tính: corner (góc dưới cùng bên trái - đối tượng Point), width, height.
    """
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

# ---------------------------------------------------------
# GIẢI QUYẾT BÀI TẬP 15.1
# ---------------------------------------------------------

# 1. Định nghĩa lớp Circle
class Circle:
    """Đại diện cho một hình tròn.
    Thuộc tính: center (đối tượng Point), radius (số thực).
    """
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

# 2. Hàm kiểm tra điểm có nằm trong/trên đường tròn hay không
def point_in_circle(circle, point):
    # Sử dụng công thức tính khoảng cách Pytago giữa 2 điểm
    distance = math.sqrt((point.x - circle.center.x)**2 + (point.y - circle.center.y)**2)
    return distance <= circle.radius

# 3. Hàm kiểm tra hình chữ nhật có nằm HOÀN TOÀN trong đường tròn không
def rect_in_circle(circle, rect):
    # Xác định tọa độ 4 góc của hình chữ nhật
    p1 = Point(rect.corner.x, rect.corner.y)                                  # Góc dưới trái
    p2 = Point(rect.corner.x + rect.width, rect.corner.y)                     # Góc dưới phải
    p3 = Point(rect.corner.x, rect.corner.y + rect.height)                    # Góc trên trái
    p4 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height)       # Góc trên phải

    # Trả về True nếu CẢ 4 điểm đều nằm trong hình tròn
    return (point_in_circle(circle, p1) and
            point_in_circle(circle, p2) and
            point_in_circle(circle, p3) and
            point_in_circle(circle, p4))

# 4. Hàm kiểm tra xem có MỘT GÓC NÀO của hình chữ nhật đè/nằm trong đường tròn không
def rect_circle_overlap(circle, rect):
    # Xác định tọa độ 4 góc của hình chữ nhật
    p1 = Point(rect.corner.x, rect.corner.y)
    p2 = Point(rect.corner.x + rect.width, rect.corner.y)
    p3 = Point(rect.corner.x, rect.corner.y + rect.height)
    p4 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height)

    # Trả về True nếu CÓ ÍT NHẤT 1 điểm nằm trong hình tròn
    return (point_in_circle(circle, p1) or
            point_in_circle(circle, p2) or
            point_in_circle(circle, p3) or
            point_in_circle(circle, p4))

# ---------------------------------------------------------
# THỰC THI (Instantiate) THEO YÊU CẦU ĐỀ BÀI
# ---------------------------------------------------------

# Tạo đối tượng Point làm tâm hình tròn tại (150, 100)
center_point = Point(150, 100)

# Khởi tạo đối tượng Circle với tâm ở center_point và bán kính 75
my_circle = Circle(center_point, 75)

print(f"Đã tạo hình tròn tại tâm ({my_circle.center.x}, {my_circle.center.y}) với bán kính {my_circle.radius}.")
