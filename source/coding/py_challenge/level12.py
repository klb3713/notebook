#! /usr/bin/env python
'''python challenge level 12
question url: http://www.pythonchallenge.com/pc/return/evil.html
answer url: http://www.pythonchallenge.com/pcc/return/.html
'''

f = open('evil2.gfx','rb')
content = f.read()
f.close()

for i in xrange(5):
    f = open('level12_%d.jpg' % i, 'wb')
    f.write(content[i::5])
    f.close()
