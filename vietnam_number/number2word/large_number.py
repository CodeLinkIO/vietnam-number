import re
from vietnam_number.number2word.hundreds import n2w_hundreds
from vietnam_number.number2word.utils.base import chunks


def n2w_large_number(numbers: str):
    """Hàm chuyển đổi các số có giá trị lớn.

    Hàm chuyển đổi các số có giá trị lớn từ 999 đến 999.999.999.999

    Args:
        numbers (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi chữ số đầu ra.

    """
    total_number = []

    isNegative = False
    if numbers[0] == '-':
        numbers = numbers[1:]
        isNegative = True

    reversed_large_number = numbers[::-1]

    reversed_large_number = chunks(reversed_large_number, 3)

    for e in range(0, len(reversed_large_number)):
        value = reversed_large_number[e][::-1]
        if e == 0:
            total_number.append(n2w_hundreds(value))
        if value == '000':
            continue
        if e == 1:
            total_number.append(n2w_hundreds(value) + ' nghìn ')
        if e == 2:
            total_number.append(n2w_hundreds(value) + ' triệu ')
        if e == 3:
            total_number.append(n2w_hundreds(value) + ' tỷ ')

    if isNegative:
        total_number.append(' âm ')
    return ''.join(total_number[::-1]).strip()


def n2w_float_number(numbers: str):
    """Hàm chuyển đổi các số thập phân

    Args:
        numbers (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi chữ đưỢc chuyển đổi.

    """
    output = []
    part = numbers.split(',')
    if len(part) < 2:
        return n2w_large_number(numbers)
    else:
        output.append(n2w_large_number(part[0]))
        zero_parts = ' phẩy '
        while (len(part[1]) > 0 and part[1][0] == '0'):
            zero_parts += 'không '
            part[1] = part[1][1:]
        if (len(part[1]) > 0):
            output.append(zero_parts)
            output.append(n2w_large_number(part[1]))
    return ''.join(output).strip()


if __name__ == '__main__':

    number = '9,'
    print('9, điểm tăng'.replace(number, n2w_float_number(number)))
