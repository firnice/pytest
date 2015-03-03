__author__ = 'firnice'

g = (x*x for x in range(9*9))

print(g)

print(g.next())
print(g.next())

for n in g:
    print(n)
