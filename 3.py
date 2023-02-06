test_case_count = int(input())
for _ in range(test_case_count):
    developer_count = int(input())
    developers = list(map(int, input().split()))
    couples=[]

    for i in range(developer_count):
        if developers[i] == -1 :
                continue

        gap = 100
        teamer_developer = -1

        for j in range(i+1, developer_count):
            if developers[j] != -1 and gap > abs(developers[i] - developers[j]):
                gap = abs(developers[i] - developers[j])
                teamer_developer = j

        couples.append(str(i+1) + ' ' + str(teamer_developer+1))
        developers[teamer_developer] = -1

    for couple in couples:
        print(couple)
