def table_sort(table):

    return table

def table_print(table):
    for el1 in table:
        for el2 in el1:
            print(el2, end=' ')
        print()

def sort_col(i):
    return i[n]

test_case_count = int(input())
for _ in range(test_case_count):
    input()
    length, width = map(int, input().split())
    table = []

    for i in range(length):
        table.append(list(map(int, input().split())))

    sort_count = int(input())
    sorts = map(int, input().split())

    for sort in sorts:
        n = int(sort) - 1
        table.sort(key=sort_col)

    table_print(table)

