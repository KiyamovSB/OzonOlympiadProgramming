def make_count_dict(goods):
    count_dict ={}

    for good in goods:
        if count_dict.get(good, False):
            count_dict[good] += 1
        else:
            count_dict[good] = 1

    return count_dict


def rebate(count_dict):
    for key, value in count_dict.items():
        value -= value//3
        count_dict[key] = value
    return count_dict


def count_dict_sum(count_dict):
    sum = 0
    for key, value in count_dict.items():
        sum += key * value
    return sum




test_case_count = int(input())
for _ in range(test_case_count):
    good_count = int(input())
    goods = map(int, input().split())

    count_dict = make_count_dict(goods)
    count_dict = rebate(count_dict)
    sum = count_dict_sum(count_dict)
    print(sum)