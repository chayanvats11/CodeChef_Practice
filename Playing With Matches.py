t = int(input())

for i in range(t):
    A, B = map(int, input().split())

    sticks = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6,
    }

    C = A + B
    total = 0

    for i in str(C):
        total += sticks[int(i)]

    print(total)






