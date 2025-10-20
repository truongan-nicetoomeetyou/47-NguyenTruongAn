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