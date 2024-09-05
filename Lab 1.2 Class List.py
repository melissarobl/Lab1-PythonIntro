# Write a program that asks for the names of all the classes you are taking this semester
# Save these class names in a list
#How will you know when the last class has been entered?
#Print all the items in the list, one per line

classlist = [] #make an empty list

class_name = input('Enter class name or press enter to stop: ')

while class_name:
    classlist.append(class_name)
    class_name = input('Enter class name or press enter to stop: ')

print(classlist)


print(f'You are taking these classes:')
for c in classlist:
    print(c)

for index, c in enumerate(classlist):
    print(f'{index+1}, {c}')

#num_classes = int(input("How many classes are you taking this semseter?")
        #for class_number in range (0, number):
        #class_name = input('enter class name or press enter to stop: ')
        #list_of_classes.append(class_name)


        # Adding random comment so posts to GitHub
