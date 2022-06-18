import hashlib
import pandas as pa

table = pa.read_excel('table.xlsx', sheet_name='hashes')
values = table['Строки'].tolist()

hex_value = ''
positions = [[252, 256], [222, 226], [192, 196], [162, 166], [132, 136],
             [102, 106], [72, 76], [42, 46], [12, 16], [0, 4]]

for n in range(10):
    for pos in positions:
        for value in values:
            iterations = []
            cnt = 0
            salt = 0
            print(f'Берем первую строку: {value}')
            while hex_value[pos[0]:pos[1]] != '0119':
                cnt += 1
                salt += 1
                hex_value = hashlib.pbkdf2_hmac('sha256',
                                                value.encode('utf-8'),
                                                salt.to_bytes(16, byteorder='little'),
                                                10000,
                                                dklen=128).hex()
                print(f'Количество итераций: {cnt} \n'
                      f'Хэш: {hex_value} \n'
                      f'4 символа: {hex_value[pos[0]:pos[1]]}')
            print(f'Полученный хэш: {hex_value}\n'
                  f'Количество итераций: {cnt}')
            iterations.append(cnt)
    iterations.append(sum(iterations) // len(iterations))
    table.insert(table.shape[1], f'{pos}', iterations)

table.to_excel('table.xlsx', sheet_name='hashes')
