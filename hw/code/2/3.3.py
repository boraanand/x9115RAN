def do_twice(f,a):
    f(a)
    f(a)

def print_twice(a):
    print a 

do_twice(print_twice,"spam")
