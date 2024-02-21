# the range() function
# 일련의 숫자를 반복 한다면 range() 내장 함수를 사용 하는 것이 좋다

for i in range(5):
    print(i)

list0 = list(range(5, 10))
print(list0)

list1 = list(range(0, 10, 3))
print(list1)

list2 = list(range(-10, -100, -30))
print(list2)

# sequence의 index를 반복하려면 range()와 len()을 함께 사용
a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])
