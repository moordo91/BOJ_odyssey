def sol(arr, abc):
    arr = sorted(arr)
    dic = {
        'A': arr[0],
        'B': arr[1],
        'C': arr[2],
    }
    print(dic[abc[0]], dic[abc[1]], dic[abc[2]])

arr = list(map(int, input().split()))
abc = input()

sol(arr, abc)
