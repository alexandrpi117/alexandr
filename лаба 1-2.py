print ("Общество в начале XXI века")
x=int(input("Введите свой возраст"))
if 1<=x<7:
    print("Вам в детский сад")
elif 7<=x<18:
    print("Вам в школу")
elif 18<=x<25:
    print ("Вам в профессиональное учебное заведение")
elif 25<=x<60:
    print ("Вам на работу")
elif 60<=x<120:
    print ("Вам предоставляется выбор")
else:
    for number in range(5):
        print("Ошибка!Это программа для людей!")
