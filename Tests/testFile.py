# algoritmo  "1038"


id = 0
q = 0
total = 0.0



id = float(input())
q = float(input())


if id ==  1:total = 4.00 * q
elif id ==  2:total = 4.50 * q
elif id ==  3:total = 5.00 * q
elif id ==  4:total = 2.00 * q
elif id ==  5:total = 1.50 * q


print("Total: R$",total)


for i in range(1,10,1):
    print(i)