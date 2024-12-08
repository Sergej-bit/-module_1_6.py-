my_dict = {'Anton': 2001, 'Max': 1999, 'Sam': 2000, 'Jon': 1995}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Alex'))
my_dict['Mindi'] = 2008
print(my_dict)
my_dict.update({'Gala': 1991,
                'Herman': 1993})
print(my_dict)
del my_dict['Sam']
print(my_dict)
my_set = {1, 2, 3, 4, 5, 1, 3, 4, 6, 'Max', 'Folse', 'Max', 2, 4}
print(my_set)
print(my_set.update({'coconate', 43}))
print(my_set)
print(my_set.discard(4))
print(my_set)