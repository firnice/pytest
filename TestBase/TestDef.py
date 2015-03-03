__author__ = 'firnice'

def my_fun(x):
    if x>0:
        return x*x,x*x*x;
    else:
        return x;

print('111',my_fun(3),'111');

def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('Bob', 'M', 7)


def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2, 3]))
print(add_end([1, 2, 3]))
print(add_end())
print(add_end())



