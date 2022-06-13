import hashlib

salt = 1
cnt = 0
hex_value = ''

value = input('Введите строку: ')

while hex_value[-4:] != '0119':
    hex_value = hashlib.pbkdf2_hmac('sha256',
                                    value.encode('utf-8'),
                                    salt.to_bytes(16, byteorder='little'),
                                    10000,
                                    dklen=128).hex()
    salt += 1
    cnt += 1
    print(f'Количество итераций: {cnt}')
    print(f'Последние 4 символа хэша: {hex_value[-4:]}\n')

print(f'Полученный хэш: {hex_value}')
