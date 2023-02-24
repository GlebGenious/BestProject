def replace_ind(text, index, symbol):
    new_text = ''   #создаем пустой стринг
    for i in range(len(text)):
        if i in index:
            new_text += symbol
        else:
            new_text += text[i]
    return new_text
text = input("Введите звёзды: ")
a = int(input('введите желаемый индекс1: '))
b = int(input('введите желаемый индекс2: '))
c = int(input('введите желаемый индекс3: '))
index = [a,b,c]
symbol = input("Введите символ для замены: ")
new_text = replace_ind(text, index, symbol)
print(new_text)
