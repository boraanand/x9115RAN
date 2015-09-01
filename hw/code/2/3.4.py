def do_twice(f,num):
    f(num)
    f(num)

def do_four(f,num):
    do_twice(f,num)
    do_twice(f,num)

def print_twice(a):
    print a 
    print a

"""Print twice"""
do_twice(print_twice,'spam')
print ' '

"""Print four times"""
do_four(print_twice,'spam')
