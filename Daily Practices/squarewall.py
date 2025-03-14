n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print('*' * n)  # Top and bottom walls
    else:
        print('*' + ' ' * (n - 2) + '*')  # Middle rows with spaces