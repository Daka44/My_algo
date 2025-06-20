import sys
input = sys.stdin.readline

y , m , d = map(int, input().split())
season = (y - 2015) * 4
if (1 <= m < 3):
    season += 1
if 3 <= m < 6:
    season += 2
elif 6 <= m < 9:
    season += 3
elif 9 <= m < 12:
    season += 4
elif (12 <= m) :
    season += 5


print(season)