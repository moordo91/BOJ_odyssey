import sys
input = sys.stdin.readline

def select_type(x):
    string = ['Fizz', 'Buzz', 'FizzBuzz']
    if x not in string:
        x = int(x)
    return x

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'FizzBuzz'
    elif x % 3 == 0:
        return 'Fizz'
    elif x % 5 == 0:
        return 'Buzz'
    else:
        return x

x = select_type(input().strip())
y = select_type(input().strip())
z = select_type(input().strip())
arr = [x, y, z]
for i, k in enumerate(arr):
    if isinstance(k, int):
        print(fizzbuzz(k + (3-i)))
        break
