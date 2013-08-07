
def readNum(num_seq):
    next_num = ""
    index = 0
    cur = num_seq[index]
    index += 1
    while index < len(num_seq):
        while index < len(num_seq) and num_seq[index] == cur[0]:
            cur += num_seq[index]
            index += 1
        else:
            if index < len(num_seq):
                next_num += str(len(cur))+cur[0]
                cur = num_seq[index]
                index += 1
    else:
        next_num += str(len(cur))+cur[0]

    return next_num

a = ['1']
for i in range(30):
    a.append(readNum(a[i]))

print len(a[30])