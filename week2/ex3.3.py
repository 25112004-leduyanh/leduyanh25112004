# --- Câu 1: Hàm vẽ lưới 2x2 ---

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+', '- ' * 4, '+', '- ' * 4, '+')

def print_post():
    print('|', '  ' * 4, '|', '  ' * 4, '|')

def print_row():
    print_beam()
    do_four(print_post)

def draw_grid_2x2():
    do_twice(print_row)
    print_beam()


# --- Câu 2: Hàm vẽ lưới 4x4 ---

def print_beam4():
    print('+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+')

def print_post4():
    print('|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|', '  ' * 4, '|')

def print_row4():
    print_beam4()
    do_four(print_post4)

def draw_grid_4x4():
    do_four(print_row4)
    print_beam4()
