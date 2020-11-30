with open('1.txt') as f:
  lines_1 = f.readlines()
  lines_txt_1 = (len(lines_1))
  print(lines_txt_1)

with open('2.txt') as f:
  lines_2 = f.readlines()
  lines_txt_2 = (len(lines_2))
  print(lines_txt_2)

with open('3.txt') as f:
  lines_3 = f.readlines()
  lines_txt_3 = (len(lines_3))
  print(lines_txt_3)


with open('4.txt', 'a') as f:
  f.writelines(f'2.txt\n')
  f.writelines(f'{lines_txt_2}\n')
  f.writelines(f'{lines_2}\n')
  f.writelines(f'1.txt\n')
  f.writelines(f'{lines_txt_1}\n')
  f.writelines(f'{lines_1}\n')
  f.writelines(f'3.txt\n')
  f.writelines(f'{lines_txt_3}\n')
  f.writelines(f'{lines_3}')
