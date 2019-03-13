#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

start_a = input("Введите первую букву алфавита для определения раскладки ")

char1 = input ("Введите первую букву").lower() 
char2 = input ("Введите вторую букву").lower()

position1 = int(ord(char1) - ord(start_a) + 1)
position2 = int(ord(char2) - ord(start_a) + 1)
distance = abs(position2 - position1)

print ("Место первой буквы {}, место второй буквы {}". format(position1,position2))
print ("Между буквами {} букв". format(distance))
