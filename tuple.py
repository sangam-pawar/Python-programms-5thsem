values = input('Please enter some values :')

input_tuple = tuple(int(val) for val in values.split ())

print('tuple:',input_tuple)