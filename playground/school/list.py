member_id = [1, 2, 3, ]
member_id.insert(0, 999) # 0번째에 999를 추가
print(member_id)

member_id.append(4) # 마지막에 4를 추가
print(member_id)

vip_member = [5, 6, 7]
member_id.extend(vip_member) # vip_member의 모든 요소를 추가
print(member_id)

member_id.remove(999) # 999를 삭제
print(member_id)

""" member_id.remove(0) # 0을 삭제하려고 하면 에러 발생
ValueError: list.remove(x): x not in list
print(member_id) """

member_id.pop(2) # 2번째 요소를 삭제 3이 삭제됨
print(member_id)

member_id.pop() # 마지막 요소를 삭제 7이 삭제됨
print(member_id)

member_id.clear() # 모든 요소를 삭제
print(member_id)

member_id = [1, 2, 3, 4, 5]
print(member_id.index(3)) # 3이 있는 위치를 반환
print(member_id.count(3)) # 3이 몇개 있는지 반환

member_id.sort() # 오름차순 정렬
print(member_id)

member_id.sort(reverse=True) # 내림차순 정렬
print(member_id)

member_id.reverse() # 순서를 뒤집음
print(member_id)

member_id_copy = member_id.copy() # 복사본을 만듦
print(member_id_copy)

member_id_copy.clear()
print(member_id_copy) # 복사본을 삭제

member_id_copy = member_id # 복사본을 만들지 않고 같은 객체를 가리킴
member_id_copy.clear()
print(member_id) # 원본도 삭제됨

member_id_copy = member_id[:] # 복사본을 만들지 않고 같은 객체를 가리킴
member_id_copy.clear()
print(member_id) # 원본은 그대로 남아 있음

member_id_copy = list(member_id) # 복사본을 만들지 않고 같은 객체를 가리킴
member_id_copy.clear()
print(member_id) # 원본은 그대로 남아 있음
