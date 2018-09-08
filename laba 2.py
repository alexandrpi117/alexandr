from collections import Counter
x=str(input("Введите строку"))
print(x)
y = x.split()
f = 0
for i in range(1,len(y)):
    if len(y[f]) < len(y[i]):
        f = i
print(y[f])





f=0
g=str(input("Введите строку"))
print (g)
j=g.split(';')
for i in range(1,len(j)):
    if len(j[f])<len(j[i]):
        f=i
print (j[f])



a=str(input("Введите слово"))
p=str(input("Введите строку"))
if p.find(a)!=-1:
    print ("Такое слово есть")
else:
    print("Такого слова нет")






w=str(input("Введите предложение"))
d=w.split()
l=Counter(d)
print (len(l))
