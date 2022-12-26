import sys; intput = sys.stdin.readline

string = input()
bomb = input()
stack = []

for c in string:
    stack.append(c)
    if c == bomb[-1] and stack[-len(bomb):] == list(bomb):
        del stack[-len(bomb):]

if stack == []:
    print("FRULA")
else:
    print(''.join(stack))
    