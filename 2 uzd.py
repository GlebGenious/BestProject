number = []
text = input('text ' )
burts = input('burts ' )
index = text.find(burts)
start = 0
while index != -1:
    sub_string = text[start:]
    if sub_string.find(burts) == -1:
        break
    index = sub_string.find(burts)
    start = start + index + 1
    number.append(start + index)
print(number)
