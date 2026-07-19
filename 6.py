
s1 =  '5'
s2 = 'привет'

print(s1 + s2)
print(s1 * 5)

s3 = 'Future Step'
print(s3[0])
print(s3[-1])

print(s3[0:3])
print(s3[:3])

print(s3[7:11])
print(s3[7:])

print(s3[3:6:2]) # шаг индекса
print(s3[::-1]) # переворачивает строку

s4 = "Future Step"
s5 = "f"
if s5 in s4:
    print("есть")
else:
    print("нет")

s4 = "Future Step".lower()
print(s4)
s4 = "Future Step".upper()
print(s4)


s6 = "Future Step"
print(s6.index("S"))
print(s6.index("u",2))
print(s6.index("e",3,8))

s6 = "Future Step"
print(s6.find("t"))
print(s6.find("s"))
print(s6.find("Ste"))

s6 = "FutureStep"
print(s6.isalpha())
s6 = "1234"
print(s6.isdigit())
s6 = "FutureStep12"
print(s6.isalnum())


s7 = "one two three four"
print(s7.split(" "))
s7 = "1,2,3,4"
print(s7.split(","))

s8 = " admin admin "
print(s8.strip())
s8 = "***admin admin***"
print(s8.strip("*"))

s9 = "adsadasdasdas"
s9 = s9.replace("a","*")
print(s9)


#Пользователь вводит строку. Выведите первые три символа этой строки.
s = "uywagd"
print(s[0:3])

#Пользователь вводит строку. Выведите последние четыре символа этой строки.
s = "dawdaewqwer"
print(s[-4:])

#Пользователь вводит строку. Выведите всю строку, кроме первого и последнего символа.
s = "iuehweh"
print(s[1:-1])

#Пользователь вводит строку. Выведите строку в обратном порядке.
s = "wygdyu"
print(s[::-1])

#Пользователь вводит строку. Выведите каждый второй символ строки, начиная с первого.
s ="yuwefghygw"
print(s[::2])

#Напишите программу, которая выводит на экран количество символов в ведённой пользователем строке на экран
s ="iqwodj"
print(len(s))

#Пользователь вводит строку. Определите, есть ли в ней буква а.
s = "agga"

if "a" in s:
    print("есть")
else:
    print("нет")

#Пользователь вводит строку. Выведите индекс первого вхождения буквы о. Если буквы о нет, выведите сообщение об этом.
s = "adadok"
print(s.find("o"))








