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

        if e == 0:
            value_of_hundred = reversed_large_number[0][::-1]
            total_number.append(n2w_hundreds(value_of_hundred))
        if e == 1:
            value_of_thousand = reversed_large_number[1][::-1]
            total_number.append(n2w_hundreds(value_of_thousand) + ' nghìn ')
        if e == 2:
            value_of_million = reversed_large_number[2][::-1]
            total_number.append(n2w_hundreds(value_of_million) + ' triệu ')
        if e == 3:
            value_of_billion = reversed_large_number[3][::-1]
            total_number.append(n2w_hundreds(value_of_billion) + ' tỷ ')

    if isNegative:
        total_number.append(' âm ')
    return ''.join(total_number[::-1]).strip()


if __name__ == '__main__':

    number = '-115205201211'
    print(n2w_large_number(number))
