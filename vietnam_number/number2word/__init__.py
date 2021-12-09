from vietnam_number.number2word.large_number import n2w_float_number, n2w_large_number
from vietnam_number.number2word.single import process_n2w_single
from vietnam_number.number2word.utils.base import pre_process_n2w


def n2w(number: str):
    clean_number = pre_process_n2w(number)
    if (clean_number.find(',') != -1):
        return n2w_float_number(clean_number)
    return n2w_large_number(clean_number)


def n2w_single(number: str):
    if number[0:3] == '+84':
        number = number.replace('+84', '0')

    clean_number = pre_process_n2w(number)

    return process_n2w_single(clean_number)
