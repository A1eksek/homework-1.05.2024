'''Первая задача'''
def multiplication_list(list1):
    multi_list = 1
    for i in list1:
        multi_list *= i
    return multi_list
# print(multiplication_list([1, 3, 4, 1]))
'''Вторая задача'''
def min_list(list1):
    return print(min(list1))
# min_list([5, 1, 7, 3, 9])
'''Вторая задача'''
def izi_num(list1):
    count = 0
    for num in list1:
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
    return count

# print(izi_num([11, 2, 3, 8, 37]))
'''Третья задача'''
def function(n,l):
    r = len(l)
    while True:
        if l.count(n) == 0:
            break
        l.remove(n)
    return r - len(l)
# print(function(5,[2,3,5,5,5,9,5,8,7]))

def set_spisok(l1, l2):
    l3 = set(l1) & set(l2)
    return l3
# print(set_spisok([1, 2, 3, 4, 5, 6],[4, 5, 6, 7, 8, 9]))

def stepen(l, n):
    l1 = []
    for i in range (len(l)):
        l1.append(l[i]*l[i])
    return l1
print(stepen([1, 2, 3, 4], 2))