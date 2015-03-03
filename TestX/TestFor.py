__author__ = 'firnice'

for i,value in enumerate(['A','B','C']):
    print i,value

import os#
print([d for d in os.listdir('.')])

d = {'x':'A','y':'B','z':'C','t':1}
for k,v in d.iteritems():
    print(k,'=',v)


print [k+'='+v.lower() for k,v in d.iteritems() if isinstance(v,str) ]


