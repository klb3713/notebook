
char_count = {}
for line in open("level2code.txt"):
    for c in line:
        char_count.setdefault(c, 0)
        char_count[c] += 1

sorted_chars = sorted(char_count.items(), key=lambda x: x[1])
print sorted_chars

chars = ['a', 'e', 'i', 'l', 'q', 'u', 't', 'y']
all_str = "".join(open("level2code.txt"))
chars_ind = [(c, all_str.find(c)) for c in chars]
print ''.join([c[0] for c in sorted(chars_ind, key=lambda x: x[1])])