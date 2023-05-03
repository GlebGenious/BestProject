dictionary = {}
name = input("Enter name: ")
dictionary['name'] = name
lastname = input("Enter lastname: ")
dictionary['lastname'] = lastname
favourite_food = []
while True:
    foodname = input("Enter food: ")
    if foodname == 'stop':
        break
    else:
        favourite_food.append(foodname)
dictionary['favourite_food'] = favourite_food
print('info')
print('name :' + dictionary["name"])
print('lastname :' + dictionary["lastname"])
print('favourite_food :' + ':'.join(dictionary["favourite_food"]))






