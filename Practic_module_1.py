grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Сортируем студентов
s_studets = sorted(list(students))
print(s_studets)

# ВЫчисляем средний балл
average_grades = [(sum(grades[0])/len(grades[0])),
                  (sum(grades[1])/len(grades[1])),
                  (sum(grades[2])/len(grades[2])),
                  (sum(grades[3])/len(grades[3])),
                  (sum(grades[4])/len(grades[4]))
                  ]
print(average_grades)

# Формируем словарь из отсортированого списка студентов и среднего балла

dict_students = dict(zip(s_studets, average_grades))
print(dict_students)