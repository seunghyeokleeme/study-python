words = ['cat', 'window', 'apple']
for w in words:
    print(w, len(w))

users = {'Hans': 'active', 'Eleonre': 'inactive', 'apple': 'active'}

# RuntimeError: dictionary changed size during iteration
# for user, status in users.items():
#     if status == 'inactive':
#         del users[user]

# 복사본 반복
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# 새로운 컬랙션 추가
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
