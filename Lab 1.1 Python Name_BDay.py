name = input('What is your name?')
letters_in_name = len(name)
birth_month = input("What is your birthday month?")
print(f'Hello, {name}!')
print(f'{name}, you have {letters_in_name} letters in your name')
# other option, but more cumbersome: print(f'{name}, you have {len(name)} letters in your name')

#check month with lower or capital letters
if birth_month.lower() == "august":
    print('Happy birthday month!')
else:
    print('Your birthday is not this month')



#To print today's date, month:
#from datetime import date
#today = date.today()
#print(today)
#this_month = today.month
#print(this_month)