test_case_count = int(input())
for _ in range(test_case_count):
    last_value = -1
    flag = True
    deal_count = int(input())
    deals = map(int, input().split())

    checks = [0] * deal_count
    for deal in deals:
        checks[deal-1] += 1
        if checks[deal-1] > 1 and last_value != deal-1:
            flag = False
        last_value = deal - 1

    if flag:
        print('YES')
    else:
        print('NO')
