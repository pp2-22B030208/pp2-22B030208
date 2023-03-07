'''#1
def gene(dad):
    for i in range(dad):
        yield i**2


for i in gene(int(input())):
    print(i) '''

'''#2

def gene(n):
    for i in range(n):  
        if i%2==0:
            yield i
        elif n%2==0 and i==n-1:
            yield ''
        else:
            yield ','


for i in gene(int(input())):
    print(i ,end='') '''

'''#3
def gene(n):
    for i in range(n):  
        if i%3==0 and i%4==0:
            yield i


for i in gene(int(input())):
    print(i) '''
'''

'''#4
def gene(n,k):
    for i in range(n,k):  
        yield i**2


for i in gene(int(input()),int(input())):
    print(i) '''
    
'''#5
    def gen(n):
    i=0
    while n>i:
        yield n
        n=n-1

for i in gen(int(input())):
    print(i) '''
    
