"""
**Exercise 3.2 ( 3.1 returns expected errro)*****
"""
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

repeat_lyrics()


"""
*****Exercise 3.3**********************
"""
def right_justify(str):
    num_spaces = 70 - len(str)
    for i in range(num_spaces):
        print '',
    print str

right_justify('allen') 


"""
******Exercise 3.4*********************
"""
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


"""
******Exercise 3.5***********************
"""
def horizontal():
    print '+','-','-','-','-',

def vertical():
    print '|',' ',' ',' ',' ',

def print_vertical_lines(col):
    for j in range(0,3):
        for i in range(0,col):
	    vertical()
        print '|'

def print_horizontal_lines(col):	
    for i in range(0,col):
        horizontal()
    print '+'

def print_last_vertical_line(col):
    for i in range(0,col):
        vertical()
    print '|'

def print_last_horizontal_line(col):
    for i in range(0,col):
        horizontal()
    print '+'

def print_grid_base(col):
    print_horizontal_lines(col)
    print_vertical_lines(col)
    print_last_vertical_line(col)
	
"Function to print the grid(row,col)"
def print_full_grid(row,col):
    for i in range(0,row):
        print_grid_base(col)	
    print_last_horizontal_line(col)

print "Grid of two rows and two columns"
print_full_grid(2,2)

print "\n"

print "Grid of four rows and four columns"
print_full_grid(4,4)

