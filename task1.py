def zvezda(text2):
  for character in text2:
    if character.isspace():
      text = text2.replace(" "," ")
    else:
      text2 = text2.replace(character,"*")
  return text2

text = input('Введите текст ')
print(zvezda(text))
