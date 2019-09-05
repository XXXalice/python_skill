N = int(input())

def over():
    print('No')
    exit(0)

for i,j in enumerate(range(N)):
    if i == 0:
        order, temp_x, temp_y = 0, 0, 0
    schedule, x, y = map(int, input().split())
    distance_to_next = abs(x - temp_x) + abs(y - temp_y)
    order = schedule - order
    temp_x, temp_y = x, y
    if order % 2 == 0:
        # even order
        if distance_to_next % 2 == 0 and distance_to_next <= order:
            continue
        else:
            over()
    else:
        # odd order
        if distance_to_next % 2 == 1 and distance_to_next <= order:
            continue
        else:
            over()

print('Yes')

# yup!