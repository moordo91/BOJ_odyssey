m_e = list(input())
stk = []
ans = ""

for i in m_e:
    if i.isalpha():
        ans += i
    else:
        if i == '(':
            stk.append(i)
        elif i == '*' or i == '/':
            if stk and (stk[-1] == '*' or stk[-1] == '/'):
                ans += stk.pop()
            stk.append(i)
        elif i == '+' or i == '-':
            while stk and stk[-1] != '(':
                ans += stk.pop()
            stk.append(i)
        else:
            while stk and stk[-1] != '(':
                ans += stk.pop()
            stk.pop()

while stk:
    ans += stk.pop()

print(ans)
