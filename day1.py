with open ("data/day1.txt", "r") as f:
    input = f.readlines()
    entries = []

    for line in input:
        data = int(line.strip())
        entries.append(data)

    entries.sort()
    smallest = entries[0]
    biggest = entries[len(entries) - 1]
    i = 0
    while not smallest + biggest == 2020:
        if smallest + biggest > 2020:
            biggest = entries[len(entries) - i - 1]
        else:
            smallest = entries[i]
        i += 1

    print("Part 1:\t" + str(smallest*biggest))

    add_set = dict()
    for i, e in enumerate(entries):
        for j in range(len(entries) - i):
            add_set[e + entries[j]] = (e, entries[j])

    a1, a2, a3 = [0]*3
    for e in entries:
        if (2020-e) in add_set:
            a1 = e
            a2, a3 = add_set[2020-e]
            break

    print("Part 2:\t" + str(a1*a2*a3))