# birth_year = input('Birth year: ') # input function always take string as input
# TypeError: unsupported operand type(s) for -: 'int' and 'str'

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year) # 2022 = '2002' wrong
print(type(age))
print('age is',age)

weight_lbs = input('Weight lbs: ') # input function always take string as input
weight_kg = 0.45 * int(weight_lbs)
print('weight in kg is',weight_kg)