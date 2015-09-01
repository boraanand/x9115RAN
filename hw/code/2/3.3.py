def right_justify(str):
    num_spaces = 70 - len(str)
    for i in range(num_spaces):
        print '',
    print str

right_justify('allen') 
