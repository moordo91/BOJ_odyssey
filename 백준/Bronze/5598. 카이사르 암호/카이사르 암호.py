word = input()
for i in word:
    if ord(i) >= 68:
        print(chr(ord(i)-3), end='')
    else:
        print(chr(ord(i)+23), end='')
