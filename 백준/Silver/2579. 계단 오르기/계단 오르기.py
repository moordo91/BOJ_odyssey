n = int(input())
score = [0 for _ in range(300)] # 각 계단까지 갈 때 얻을 수 있는 최대 점수를 원소로 갖는 리스트
steps = [0 for _ in range(300)] # 각 계단마다 할당된 점수를 원소로 갖는 리스트
for i in range(n):
    steps[i] = int(input())

# dp 문제이므로 초항을 생각해 본다.
score[0] = steps[0]
score[1] = steps[0] + steps[1]
score[2] = max(steps[0], steps[1]) + steps[2]

# 점화식을 생각한다. 마지막 항에 추가 조건이 있으므로 마지막 항을 기준으로 생각한다.
for i in range(3, n):
    score[i] = max(score[i-3] + steps[i-1], score[i-2]) + steps[i]

print(score[n-1])