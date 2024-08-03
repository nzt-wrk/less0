immutable_var = (1, 2, 3, 'string', 0.5, [1,3,5,7,9])
print(immutable_var)
# immutable_var[2] = 33 данная операция не может быть выполенена т.к. элементы кортежа являются константой и не меняются, при выполнении кода будет ошибка
print(immutable_var[-1][-2])

print()

mutable_list = immutable_var[-1]
print(mutable_list)
print(mutable_list[::-2])
mutable_list.append('first')
print(mutable_list)
print(mutable_list[-1])
mutable_list.extend(['second', 14])
print(mutable_list)
mutable_list.extend('third')
print(mutable_list)
mutable_list.remove(14)
print(mutable_list)
print(immutable_var[0] in mutable_list)
mutable_list[6]= '2nd'

print(mutable_list)
print(immutable_var)



