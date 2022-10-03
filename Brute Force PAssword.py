from itertools import permutations
#Код:
massive = 'abcdefghijklmnopqrstuvwxyz0123456789'
k=0
for i in permutations(massive,14):
    
    k+=1
    word = ''.join(i)
    print(k,'     ',word)

print('Всего коомбинаций: ',k)