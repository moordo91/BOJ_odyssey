import sys
input()
for l in sys.stdin:a,b=map(int,l.split());print(0if b%a or a==b else 1)