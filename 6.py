def read_time_table():
    row_count = int(input())
    time_table = []
    for _ in range(row_count):
        time_table.append(list(map(str, input().split('-'))))
    return time_table

def is_chronology(time1, time2):
    return time1 <= time2

def is_strong_chronology(time1, time2):
    return time1 < time2

def is_correct_time(time):
    hour, minute, second = map(int, time.split(':'))
    return hour < 24 and minute < 60 and second < 60


test_case_count = int(input())
for _ in range(test_case_count):
    flag = True

    time_table = read_time_table()
    time_table.sort()

    for i in range(len(time_table)):
        if is_correct_time(time_table[i][0]) and is_correct_time(time_table[i][1]) and is_chronology(time_table[i][0], time_table[i][1]):
            pass
        else:
            flag = False

    for i in range(len(time_table)-1):
        if is_strong_chronology(time_table[i][1], time_table[i+1][0]):
            pass
        else:
            flag = False

    if flag:
        print('YES')
    else:
        print('NO')
