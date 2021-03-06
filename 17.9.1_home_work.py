#!/usr/bin/env python
# coding: utf-8

# In[19]:


while True:
    try:
        set_of_numbers = list(map(int, input('Введите произвольный набор чисел через "пробел":').split(' ')))
    except Exception:
        print ("Ошибка ввода чисел")
    else:
        break
while True:
    try:
        number = list(map(int, input(f"Введите число от {min(list(set_of_numbers))} до {max(list(set_of_numbers))}: ").split(' ')))
        if min(list(number)) < min(list(set_of_numbers)) or max(list(number)) > max(list(set_of_numbers)):
            raise ValueError
    except ValueError:
            print ("Необхлодимо ввести число от {min(list(set_of_numbers))} до {max(list(set_of_numbers))}: ")
    else:
        break
        
array, num = list(map(int, set_of_numbers)),list(map(int, number))
array.extend(num)
print("Список чисел: ", array)

def sort_array(array):
    for i in range(1, len(array)):
        x = array[i]
        a = i
        while a > 0 and array[a - 1] > x:
            array[a] = array[a - 1]
            a -= 1
        array[a] = x
    return array
sort = sort_array(array)
print("Сортировка:", sort)


def double_search(sort, z, left, right):
    if left > right:  
        return False  

    middle = (right + left) // 2  
    if z == sort[middle]: 
        return middle  
    elif z < sort[middle]: 
       
        return double_search(sort, z, left, middle - 1)
    else:  
        return double_search(sort, z, middle + 1, right)

z = min(number) 
index = double_search(sort, z, 0, len(sort))


if z == max(sort):
    idx_z = index
elif z == min(sort):
    idx_z = "- не определён, так как введённое число минимальное"
else:
    idx_z = index - 1  #
    
print(f"Последний индекс в списке: {len(sort)-1}")
print(f"Предшествующий числу {z} индекс:", idx_z)


# In[ ]:





# In[ ]:




