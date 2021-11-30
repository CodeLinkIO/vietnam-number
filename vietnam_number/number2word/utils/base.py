from vietnam_number.number2word.data import units
import re


def chunks(lst, n):
    """Hàm chia nhỏ danh sách đầu vào.

    Hàm dùng chia nhỏ danh sách đầu vào thành các nhóm danh sách con với số lượng các phần tử trong
    nhóm con là n

    Args:
        lst: Danh sách đầu vào.
        n: Số lượng phần tử trong một nhóm con.

    Returns:
        Danh sách các nhóm con có n phần tử.
    """
    chunks_lst = []
    for i in range(0, len(lst), n):
        chunks_lst.append(lst[i: i + n])

    return chunks_lst


def pre_process_n2w(number: str):
    """Hàm tiền xữ lý dữ liệu đầu vào.

    Args:
        number (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi số sau khi được tiền xữ lý.
    """
    char_to_replace = {
        ' ': '',
        '.': '',
        ',': '',
    }

    # xóa các ký tự đặt biệt
    for key, value in char_to_replace.items():
        number = number.replace(key, value)

    number_pattern = r'^-?[0-9]\d*$'
    # Kiểm tra tính hợp lệ của đầu vào
    if not re.match(number_pattern, number):
        raise ValueError('Đầu vào không hợp lệ!')

    return number


var = pre_process_n2w('-11')
print(var)
