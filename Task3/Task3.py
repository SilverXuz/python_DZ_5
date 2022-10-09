"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
"""
# Это не мой код. Вообще не понимаю почему такие задачи мы решаем самостоятельно, без схожих примеров!!! 

# Модуль сжатия
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

encoded_val = rle_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')
print(encoded_val)

# Модуль восстановления
# def rle_decode(data):
#     decode = ''
#     count = ''
#     for char in data:
#         if char.isdigit():
#             count += char
#         else:
#             decode += char * int(count)
#             count = ''
#     return decode

# decoded_val = rle_decode('6A1F2D7C1A17E')
# print(decoded_val)
