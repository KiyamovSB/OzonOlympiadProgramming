def is_first_view(s):
    return s[0].isalpha() and s[1].isdigit() and s[2].isdigit() and s[3].isalpha() and s[4].isalpha()

def is_second_view(s):
    return s[0].isalpha() and s[1].isdigit() and s[2].isalpha() and s[3].isalpha()


test_case_count = int(input())
for _ in range(test_case_count):
    s = input()
    flag = True
    position = 0
    answer = ''
    while flag:
        if position + 5 <= len(s):
            if is_first_view(s[int(position): int(position+5)]):
                answer += ' ' + s[int(position): int(position+5)]
                position += 5
            elif is_second_view(s[int(position): int(position+4)]):
                answer += ' ' + s[int(position): int(position+4)]
                position += 4
            else:
                answer = '-'
                flag = False
        elif position + 4 <= len(s):
            if is_second_view(s[int(position): int(position + 4)]):
                answer += ' ' + s[int(position): int(position + 4)]
                position += 4
            else:
                answer = '-'
                flag = False
        else:
            if position == len(s):
                flag = False
            else:
                answer = '-'
                flag = False

    if answer == '-':
        print(answer)
    else:
        print(answer[1:])







