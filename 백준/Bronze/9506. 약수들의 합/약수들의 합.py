def sol(num):
    arr = [1]
    for i in range(2, num//2):
        if num // i in arr:
            break
        if num % i == 0:
            arr.append(i)
            arr.append(num // i)
    if sum(arr) != num:
        return f"{num} is NOT perfect."
    else:
        arr.sort()
        ans = f"{num} = 1"
        for i in range(1, len(arr)):
            ans += f" + {arr[i]}"
        return ans
    
while True:
    num = int(input())
    if num == -1:
        break
    else:
        print(sol(num))