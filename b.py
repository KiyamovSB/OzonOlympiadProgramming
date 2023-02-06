test_case_count = int(input())
for _ in range(test_case_count):
    check_sizes = [4, 3, 2, 1]
    sizes = map(int, input().split())

    for size in sizes:
        check_sizes[size-1] -= 1

    if check_sizes[0] == 0 and check_sizes[1] == 0 and check_sizes[2] == 0 and check_sizes[3] == 0:
        print('YES')
    else:
        print('NO')