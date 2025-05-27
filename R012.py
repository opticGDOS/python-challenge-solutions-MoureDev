str1 = input()
str2 = input()
out1 = ''
out2 = ''

for char in str1:
    if char not in str2:
        out1 += char

for char in str2:
    if char not in str1:
        out2 += char

print(f'{out1}\n{out2}')
