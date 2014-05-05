import re
all_str = "".join(open("level3code.txt"))
chars = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', all_str)
print "".join(chars)