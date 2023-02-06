def del_repeat_alpa_3(good):
    lastlast = ''
    last = ''
    good2 = ''
    for el in good:
        if  last == lastlast == el:
            pass
        else:
            good2 += el
            lastlast = last
            last = el

    return good2


test_case_count = int(input())
for _ in range(test_case_count):
    goods = set()
    good_count = int(input())
    for _ in range(good_count):
        good = input()
        goods.add(del_repeat_alpa_3(good))

    print(len(goods))

