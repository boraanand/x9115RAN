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

