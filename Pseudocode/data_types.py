"""
list.sort() sorts the list and save the sorted list,
while sorted(list) returns a sorted copy of the list,
without changing the original list.
"""
#myList1 = ['Sofía', 'Carlos', 'Mauricio', 'Rafa', 'Fabian']
#myList2 = ['Pepe', 'Lepu']

#size = len(myList)
#print(myList[int(size/2)])

#myList1.sort(reverse=True, key=len)
#print(myList1)
#print(sorted(myList1))
#print(myList1.pop(0))
#print([*myList1, *myList2])

def print_values(dictionary):
    for key in dictionary:
        print(dictionary[key])

my_second_dictionary = {
    'name': 'Saltie',
    'last_name': 'Villanueva'
}

my_fist_dictionary = {
    'name': 'Panfilo',
    'last_name': 'Membrillo',
    'age': '99',
    'phone': 12345,
    'books': ['Math', 'Arts'],
    'address': {
        'street': 'Real',
        'number': 17
    }
}
"""print(my_fist_dictionary['name'])
print(my_fist_dictionary)

for key in my_fist_dictionary:
    print(my_fist_dictionary[key])"""


#print(my_fist_dictionary['address']['street'])

print_values(my_fist_dictionary)
print_values(my_second_dictionary)