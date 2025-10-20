# student_manager.py

# Danh sách để lưu thông tin các sinh viên.
# Mỗi sinh viên là một dictionary.
student_list = []

def add_student(name, year_of_birth, address):
    """
    YÊU CẦU 1: Hoàn thiện hàm này.
    - Tạo một dictionary để lưu thông tin sinh viên.
    - Thêm dictionary đó vào danh sách `student_list`.
    - In ra thông báo "Da them sinh vien <ten> thanh cong."
    """
    # Tạo dictionary lưu thông tin sinh viên
    student = {
        "ten": name,
        "nam_sinh": year_of_birth,
        "dia_chi": address
    }

    # Thêm vào danh sách student_list
    student_list.append(student)

    # In ra thông báo
    print("Da them sinh vien", name, "thanh cong.")
    
def print_student_list():
    """
    In danh sách tất cả sinh viên.
    """
    print("--- DANH SACH SINH VIEN ---")
    if len(student_list) == 0:
        print("Danh sach trong.")
    else:
        for student in student_list:
            print(f" - Ten: {student['ten']}, Nam sinh: {student['nam_sinh']}, Dia chi: {student['dia_chi']}")

    
def search_student(search_name):
    """
    Tìm kiếm sinh viên theo tên (không phân biệt hoa thường).
    """
    print("--- KET QUA TIM KIEM ---")
    found = False
    for student in student_list:
        if search_name.lower() in student['ten'].lower():
            print(f" - Ten: {student['ten']}, Nam sinh: {student['nam_sinh']}, Dia chi: {student['dia_chi']}")
            found = True
    if not found:
        print("Khong tim thay sinh vien nao.")
