age = int(input('age: '))

age_names = ('kid', 'teenager', 'adult', 'older', 'undefined')
if 6 > age >= 0:
    print(age_names[0])
elif 6 <= age < 18:
    print(age_names[1])
elif 18 <= age < 60:
    print(age_names[2])
elif age >= 60:
    print([age_names[3]])
else:
    print(age_names[4])
