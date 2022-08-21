def mat_pow(mat1, mat2):
    ans = [[0, 0], [0, 0]]
    ans[0][0] = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    ans[0][1] = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    ans[1][0] = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    ans[1][1] = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]
    return ans

def mat_return(a, c):
    return [[a[0][0] % c, a[0][1] % c], [a[1][0] % c, a[1][1] % c]]

def power(a, b, c):
    if b == 1:
        return mat_return(a, c)
    else:
        tmp = power(a, b//2, c)
        tmp_pow = mat_pow(tmp, tmp)
        if b % 2 == 0:
            return mat_return(tmp_pow, c)
        else:
            return mat_return(mat_pow(tmp_pow, a), c)

mat = [[1, 1],
       [1, 0]]

n = int(input())
c = 1_000_000_007
print(power(mat, n, c)[1][0])
