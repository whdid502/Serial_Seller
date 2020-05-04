a = '무료       '
a1 = '₩37,200      '
# if a != int:
#     a = 0
# if a1 != int:
#     a1 = 0
b = a.replace('₩', '', 1).strip().replace(',', '')
b1 = a1.replace('₩', '', 1).strip().replace(',', '')
# if b == str:
#     b = 0
# if b1 == complex:
#     b1 = 0
import os
print(a, type(a), a1, type(a1), b, type(b), b1, type(b1))
# print(os.path.abspath('python3'))
# c = int(a)
# print(a, b, a1, b1)