print('Hello capstone!')

# variables
school = 'MCTC' #MCTC inferred to be a string
gpa = 3.7 #number inferred
students_in_class = 22 #snake_case used in Python

# if-statements
if gpa == 4:
    print('WOW!')
elif gpa > 3:
    print('Awesome!')
else:
    print('Cool!')
# if-elif-else

# lists
schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']
if 'MCTC' in schools:
    print('MCTC is one of the schools in the list.')
# in operator



# strings
class_name = "Software Development Capstone"
print(class_name.upper())
print(len(class_name))
print(class_name.split())
print(class_name.split('o'))  #split by letter 'o'

if 'Capstone' in class_name:
    print('This must be the capstone')

schools.sort()
print(schools)
schools.append('Century College')
print(schools)

schools.reverse()
print(schools)

# loops - for loops over range
for x in range(10):
    print(x)

# loops - for loops over sequence
for s in schools:
    print(s.upper())

for letter in school:
    print(letter * 10) #print every letter in school name on separate line x number of times

    data = [0] * 10 # make empty list of 10 items
    print(data)

more_data = [None] #10
print(more_data)


# while loops
name = input('Enter your name: ')
while len(name) == 0:
    print ('Please enter at least one character ')
    name = input('Enter your name: ')

name = input('Enter your name: ')
while not name: # same as !name in other languages
    print ('Please enter at least one character ')
    name = input('Enter your name: ')


# True and False and None
start_of_semester = True
winter = False

if winter:  # no need for True or False since it is Boolean
    print('brr!')
else:
    print('it is not winter')


# Dictionaries
class_codes = { 2905: 'Capstone', 2560: 'Web', 2545: 'Java'}

print(class_codes[2560])

for code in class_codes:
    print(code)
    print(class_codes[code]) #print values

for code, name in class_codes.items():
    print('The class code is ' + str(code) + ' and the name is ' + name)

for code, name in class_codes.items():
     print(f'The class code is  + {code} and the name is  + {name}') # in {} can be anything - not just string


# Slicing strings, lists
schools_slicing = ['MCTC', 'DCTC', 'North Hennepin Technical College']
first_two = schools_slicing[0:2]
# or first_two = schools_slicing[:2] and start of list is assumed
print(first_two)

last_school = schools_slicing[-1] #last position in the list
print(last_school)

last_two_schools = schools[-2:]  #starts at end and counts in
print(last_two_schools)


school_name = 'Minneapolis Community and Technical College'
city = school_name[11]
print(city)

# File IO
with open('data.txt') as f:
    print(f.read())
with open('schools.txt', 'w') as f:
    print(f.writelines(schools))  #written all on one line- how to split

# Functions
def get_name():
    print('Hello, please enter your name!')
    name = input('Your name is: ')
    return name

name = get_name()