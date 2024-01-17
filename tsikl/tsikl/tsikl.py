#1
''' pervij
mitu=0
for k in range(1,16):
    n=float(input("Sisesta "+str(k)+". arv"))
    if int(n)== float(n):
        mitu+=1
print("Täisarvude kogus: ",mitu)
'''
''' vtoroj
k=0
while True:
    k+=1
    n=float(input("Sisesta arv nr." +str(k)))
    if int(n)==float(n):
        mitu+=1
        if k==15: break
        '''
''' tretij
k=0
mitu=0
while k<15:
    k+=1
    n=float(input("Sisesta arv nr." +str(k)))
    if int(n)==float(n):
        mitu+=1
        '''
#16
'''
n=9
i=1
while i<=n:
    j=1
    while j <=n:
        if i==j:
            print(i, end="")
        else:
            print(0, end="")
        j+=1
    print()
    i+=1


for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print(i, end="")
        else:
            print(0, end="")
    print()




n=9
i=1
while True:
    j = 1
    while j <= n:
        if i == j:
            print(i, end="")
        else:
            print(0, end="")
        j += 1
    print()
    i += 1

    if i > n:
        break
        '''


#2
'''
A = int(input("Введите число A: "))
sum = 0
i = 1

while i <= A:
    sum += i
    i += 1

print(f"Сумма всех натуральных чисел от 1 до {A}: {sum}")






A = int(input("Введите число A: "))
sum_while = 0
i = 1

while True:
    sum_while += i
    i += 1
    if i > A:
        break

print(f"Сумма всех натуральных чисел от 1 до {A}: {sum_while}")






A = int(input("Введите число A: "))
sum_for = 0

for i in range(1, A + 1):
    sum_for += i

print(f"Сумма всех натуральных чисел от 1 до {A}: {sum_for}")
'''
#3
'''
a = 1
b = 0

while b < 8:
    c = float(input("Введите число: "))
    if c > 0:
        a *= c
        b += 1

print(f"Произведение положительных чисел : {a}")


a_while = 1
b_while = 0

while True:
    c_while = float(input("Введите число: "))
    if c_while > 0:
        a_while *= c_while
        b_while += 1
    if b_while == 8:
        break

print(f"Произведение положительных чисел : {a_while}")


a_for = 1

for i in range(8):
    c_for = float(input("Введите число: "))
    if c_for > 0:
        a_for *= c_for

print(f"Произведение положительных чисел : {a_for}")
'''


#4
'''
num = 10

while num <= 20:
    square = num ** 2
    print(f"Квадрат числа {num}: {square}")
    num += 1


num_while = 10

while True:
    square_while = num_while ** 2
    print(f"Квадрат числа {num_while}: {square_while}")
    num_while += 1

    if num_while > 20:
        break


for num_for in range(10, 21):
    square_for = num_for ** 2
    print(f"Квадрат числа {num_for}: {square_for}")

    '''