things = {"зонт": 500, "рубашка": 300, "зеркальце": 100, "карандаш": 20}
d = {}
flag = -1 
print ("Введите данные в формате предмет=вес, для завершения введите пустую строку: ")
while flag != 0:
    user_input = input()
    if user_input == "":
        flag =0
    else:
        item, weight = user_input.split("=")
        d [item] = int(weight)
things.update(d)
print("Новый словарь :", things)
