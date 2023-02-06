def read_members_friends(members_friends, relation_count):
    for i in range(relation_count):
        member1, member2 = map(int, input().split())
        members_friends[member1 - 1].add(member2)
        members_friends[member2 - 1].add(member1)
    return members_friends

members_count, relation_count = map(int, input().split())
members_friends = [set() for i in range(members_count)]
members_perhaps_friends = [set() for i in range(members_count)]

members_friends = read_members_friends(members_friends, relation_count)

for i in range(len(members_friends)):
    max = 0

    perhaps_friends = set()
    for j in members_friends[i]:
        perhaps_friends.update(members_friends[j-1])
    perhaps_friends.difference_update({i+1}, members_friends[i])

    for perhaps_friend in perhaps_friends:
        if len(members_friends[i].intersection(members_friends[perhaps_friend-1])) == max and len(members_friends[i].intersection(members_friends[perhaps_friend-1])) > 0:
            members_perhaps_friends[i].update({perhaps_friend})
        if len(members_friends[i].intersection(members_friends[perhaps_friend-1])) > max:
            max = len(members_friends[i].intersection(members_friends[perhaps_friend-1]))
            members_perhaps_friends[i] = {perhaps_friend}

    if max == 0:
        members_perhaps_friends[i] = {0}


for el in members_perhaps_friends:
    print(' '.join(map(str, sorted(el)) ))
