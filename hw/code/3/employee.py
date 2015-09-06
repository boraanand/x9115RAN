from __future__ import print_function, division

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Name: {} | Age: {}'.format(self.name, self.age)

    def __lt__(self, other):
        return self.age < other.age

if __name__ == '__main__':
    print('#'* 50)
    print('Pretty print name and age:')
    e1 = Employee('Nirmesh', 23)
    print(e1)

    print('\n')
    print('#'*50)
    print('Sort the list of class based on age:')
    employee_list = [Employee('Nirmesh', 21), Employee('Anand', 20), Employee('Ravi', 23)]
    print('-'*30)
    print('Unsorted Employee list:')
    print(*employee_list, sep='\n')
    print('-'*30)
    print('Sorted list:')
    print(*sorted(employee_list), sep='\n')