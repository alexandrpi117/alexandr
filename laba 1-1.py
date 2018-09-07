x=int(input("Введите число от 1 до 9"))
if 1 <= x and x <= 3:
    s=str(input("Введите строку"))
    n=int(input("Введите количество повторов строки"))
    for y in range(n):
        print(s)
elif 4<=x and x<=6:
      m=int(input("Введите степень в которую нужно возвести чило"))
      print(x**m)
elif 7<=x and x<=9:
    for k in range(10):
        x=x+1
        print (x)
else:
    print ("Неправильный ввод")
    
