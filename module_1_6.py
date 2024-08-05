# Словари
my_dict = {'Stepan':1986, 'Konstantin':1985, 'Olga':1989}
print('Dictionary:', my_dict)
print('Existing value: ', my_dict['Olga'])
print('Not existing value:', my_dict.get('Roman', 'Key dos\'nt exist'))
my_dict.update({'Vlad':2001, 'Valera':1955})
print('Deleted value:', my_dict.pop('Vlad'))
print('Modified dictionary:', my_dict)


# Множества
my_set = {1, 2, 3, 4.55, 'string', (1, 2), 1, 2, 'string'}
print('\nSet: ', my_set)
my_set.add(6)
my_set.update([7 ,8, 9, 10]) # добавление несокльих элементов
my_set.discard(9)
my_set.remove(8) # Выдаст ошибку, если элемент не будет найден во множестве
print('Modified set: ', my_set)

#test
print('\ntest', list(my_set).pop(0))
