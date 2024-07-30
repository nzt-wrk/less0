# задача 1
print('1st program')
print(9**0.5*5)
print()

# задача 2
print('2st program')
print(9.99 > 9.98 and 1000 != 1000.1)
print()

# задача 3
print('3rd program')
print(1234//10%100+5678//10%100)
print()

# задача 4
print('4rd program')
print(int(13.42) == 13 and int(42.13*100%100) == 13) # вариант 1
print(int(13.42) == int(42.13*100%100))  # вариант 2
print(int(13.42) == int(42.13*100%100) or int(13.42*100%100) == int(42.13)) # вариант 3
print()


# test
print(float(4213//100), 4213//100, int(4213//100), 4213/100)
print(float(4213%100), 4213%100, float(42.13%100))
