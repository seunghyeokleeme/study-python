i = 5

def f(arg=i):
    print(arg)
# default argument = 5

i = 6
f()

# 기본값 공유하지 않기 위한 방법 중 하나! None

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def parrot(voltage, state='a stiff', action='voom', type='Norewgian Blue'):
    print("-- This parrot would't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action='VOOOM')
parrot(action='VOOOOOM', voltage=100000)
parrot('a millon', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')


